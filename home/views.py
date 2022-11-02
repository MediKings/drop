from django.shortcuts import get_object_or_404, render, redirect
from .models import Product, Category, SubCategory
from django.contrib.auth.decorators import login_required


def Home(request):
    products = Product.objects.all().order_by('-date')[:8]
    cats = Category.objects.all()
    template_name = 'home/index.html'
    context = {
        'products': products,
        'cats': cats,
        }
    return render(request, template_name, context)


def Detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    products = Product.objects.filter(category=product.category).exclude(id=product.id)
    template_name = 'home/detail.html'
    context = {
        'product': product,
        'products': products,
        }
    return render(request, template_name, context)


def Contact(request):
    template_name = 'home/contact.html'
    context = {}
    return render(request, template_name, context)