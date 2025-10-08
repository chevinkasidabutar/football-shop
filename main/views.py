from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.db.models import Q
import datetime

from .models import Product
from .forms import ProductForm


@login_required
def show_main(request):
    q = request.GET.get("q", "").strip()
    filter_type = request.GET.get("filter", "all")
    selected_category = request.GET.get("category", "")
    is_home = not (q or selected_category or filter_type == "my")

    qs = Product.objects.select_related("user").order_by("-created_at")
    if filter_type == "my":
        qs = qs.filter(user=request.user)
    if selected_category:
        qs = qs.filter(category=selected_category)
    if q:
        qs = qs.filter(Q(name__icontains=q) | Q(description__icontains=q))

    product_list = list(qs)
    for p in product_list:
        p.can_edit = (p.user_id == request.user.id)

    popular_list = list(Product.objects.select_related("user").order_by("-views", "-created_at")[:2])
    categories = list(Product.objects.order_by().values_list("category", flat=True).distinct())

    # prev/next (opsional)
    prev_next_map = {}
    for i, p in enumerate(product_list):
        prev_id = product_list[i - 1].id if i > 0 else None
        next_id = product_list[i + 1].id if i < len(product_list) - 1 else None
        prev_next_map[p.id] = {"prev": prev_id, "next": next_id}

    context = {
        "is_home": is_home,
        "query": q,
        "filter_type": filter_type,
        "selected_category": selected_category,
        "categories": categories,
        "popular_list": popular_list,
        "product_list": product_list,
        "last_login": request.user.last_login,
        "prev_next_map": prev_next_map,
        "fixed_name": "Chevinka Queen Cilia Sidabutar",
        "npm": "2406437376",
        "kelas": "PBP F",
    }
    return render(request, "main.html", context)


def logout_user(request):
    logout(request)
    resp = redirect("main:login_user")
    resp.delete_cookie("last_login")
    return resp


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created. You can log in.")
            return redirect("main:login_user")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
    else:
        form = AuthenticationForm(request)
    return render(request, 'login.html', {'form': form})


@login_required(login_url='/login/')
def create_product(request):
    form = ProductForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')
    return render(request, "create_products.html", {'form': form})


@login_required
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id, user=request.user)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Produk berhasil diperbarui.")
            return redirect("main:show_main")
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form, "product": product})


@login_required(login_url='/login/')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if request.method == "POST":
        if product.user_id != request.user.id:
            return JsonResponse({"detail": "Forbidden"}, status=403)
        product.delete()
        messages.success(request, "Produk berhasil dihapus.")
        return redirect('main:show_main')
    return render(request, "confirm_delete.html", {'product': product})


@login_required(login_url='/login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if hasattr(product, "increment_views"):
        try:
            product.increment_views()
        except Exception:
            pass
    return render(request, "product_detail.html", {'product': product})


# ================== Data (JSON / XML) ==================
def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")


def show_json(request):
    product_list = Product.objects.select_related('user').all().order_by('-created_at')
    data = [
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'size': p.size,
            'color': p.color,
            'price': p.price,
            'is_featured': p.is_featured,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user_id else None,
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'views': getattr(p, 'views', 0),
        }
        for p in product_list
    ]
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, product_id):
    try:
        product_qs = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_qs)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)


def show_json_by_id(request, product_id):
    try:
        p = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': p.id,
            'name': p.name,
            'price': p.price,
            'description': p.description,
            'category': p.category,
            'thumbnail': p.thumbnail,
            'size': p.size,
            'color': p.color,
            'is_featured': p.is_featured,
            'views': getattr(p, 'views', 0),
            'created_at': p.created_at.isoformat() if p.created_at else None,
            'user_id': p.user_id,
            'user_username': p.user.username if p.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


# ================== AJAX: CRUD ==================
@login_required
@require_POST
def add_products_entry_ajax(request):
    from django.utils.html import strip_tags
    name = strip_tags(request.POST.get("name", "").strip()) or "(No Name)"
    description = strip_tags(request.POST.get("description", "").strip()) or "(No Description)"
    category = strip_tags(request.POST.get("category", "").strip())
    price = request.POST.get("price")
    size = strip_tags(request.POST.get("size", "").strip())
    color = strip_tags(request.POST.get("color", "").strip())
    thumbnail = strip_tags(request.POST.get("thumbnail", "").strip())
    is_featured = request.POST.get("is_featured") == "on"

    if not price:
        return JsonResponse({"error": "Price cannot be empty."}, status=400)

    product = Product(
        name=name, description=description, category=category, price=price,
        size=size, color=color, thumbnail=thumbnail, is_featured=is_featured,
        user=request.user
    )
    product.save()
    return JsonResponse({"success": True, "id": product.id}, status=201)


@login_required
@require_POST
def update_product_ajax(request, id):
    from django.utils.html import strip_tags
    product = get_object_or_404(Product, pk=id)
    if product.user_id != request.user.id:
        return JsonResponse({"error": "Forbidden"}, status=403)

    product.name = strip_tags(request.POST.get("name", product.name).strip()) or product.name
    product.description = strip_tags(request.POST.get("description", product.description).strip()) or product.description
    product.category = strip_tags(request.POST.get("category", product.category).strip())
    product.price = request.POST.get("price", product.price)
    product.size = strip_tags(request.POST.get("size", product.size or "").strip())
    product.color = strip_tags(request.POST.get("color", product.color or "").strip())
    product.thumbnail = strip_tags(request.POST.get("thumbnail", product.thumbnail or "").strip())
    product.is_featured = (request.POST.get("is_featured") == "on") if ("is_featured" in request.POST) else product.is_featured

    product.save()
    return JsonResponse({
        "success": True,
        "product": {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'size': product.size,
            'color': product.color,
            'price': product.price,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'views': getattr(product, 'views', 0),
        }
    }, status=200)


@login_required
@require_POST
def delete_product_ajax(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user_id != request.user.id:
        return JsonResponse({"error": "Forbidden"}, status=403)
    product.delete()
    return JsonResponse({"success": True}, status=200)


# ================== AJAX: Auth ==================
@require_POST
def login_ajax(request):
    username = request.POST.get("username", "").strip()
    password = request.POST.get("password", "").strip()
    user = authenticate(request, username=username, password=password)
    if user is None:
        return JsonResponse({"success": False, "error": "Invalid credentials"}, status=400)
    login(request, user)
    resp = JsonResponse({"success": True, "redirect": reverse("main:show_main"), "username": user.username})
    resp.set_cookie('last_login', str(datetime.datetime.now()))
    return resp


@require_POST
def register_ajax(request):
    form = UserCreationForm(request.POST)
    if not form.is_valid():
        return JsonResponse({"success": False, "errors": form.errors}, status=400)
    user = form.save()
    login(request, user)
    return JsonResponse({"success": True, "redirect": reverse("main:show_main"), "username": user.username})


@login_required
@require_POST
def logout_ajax(request):
    logout(request)
    return JsonResponse({"success": True, "redirect": reverse("main:login_user")})
