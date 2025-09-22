from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=300)
    price = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=200)
    is_featured = models.BooleanField(default=False)

    stock = models.PositiveBigIntegerField(default=0)
    color = models.CharField(max_length=40, blank=True)
    size = models.CharField(max_length=5,
        choices=[('S','S'),('M','M'),('L','L'),('XL','XL')],
        blank=True
    )
    sold_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    @property
    def is_in_stock(self) -> bool:
        return self.stock > 0

    @property
    def short_description(self) -> str:
        return (self.description[:80] + '...') if len(self.description) > 80 else self.description

    def sell(self, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("qty must be >= 1")
        if self.stock < qty:
            raise ValueError("insufficient stock")
        self.stock -= qty
        self.sold_count += qty
        self.save(update_fields=['stock', 'sold_count', 'updated_at'])

    def restock(self, qty: int = 1) -> None:
        if qty < 1:
            raise ValueError("qty must be >= 1")
        self.stock += qty
        self.save(update_fields=['stock', 'updated_at'])
