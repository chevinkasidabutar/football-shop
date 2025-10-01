from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Q
from main.forms import ProductForm
from main.models import Product
from django.db.models import Q
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
# Baris 'from django import template' telah dihapus
from .models import Product
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# main/views.py
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

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
        if p.can_edit:
            p.edit_form = ProductForm(instance=p)
        p.color_list = [c.strip() for c in (p.color or "").replace(";", ",").split(",") if c.strip()]

    popular_list = list(Product.objects.select_related("user").order_by("-views", "-created_at")[:2])
    categories = list(Product.objects.order_by().values_list("category", flat=True).distinct())

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
            return redirect("main:show_main")
    else:
        form = ProductForm(instance=product)
    return render(request, "edit_product.html", {"form": form, "product": product})

@login_required(login_url='/login/')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)

    if request.method == "POST":
        product.delete() 
        messages.success(request, "Produk berhasil dihapus.")
        return redirect('main:show_main')
    return render(request, "confirm_delete.html", {'product': product})

@login_required(login_url='/login/')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    # asumsi kamu punya method ini di model:
    if hasattr(product, "increment_views"):
        product.increment_views()
    return render(request, "products_detail.html", {'product': product})


def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    json_data = serializers.serialize("json", product_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product_obj = Product.objects.get(pk=product_id)
        json_data = serializers.serialize("json", [product_obj])
        return HttpResponse(json_data, content_type="application/json")
    except Product.DoesNotExist:
        return HttpResponse(status=404)