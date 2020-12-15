from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .forms import ProductFrom
from .models import Product


# Create your views here.


def index(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})


def prod(request):
    if request.method == "POST":
        form = ProductFrom(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/shop/show')
            except:
                pass
    else:
        form = ProductFrom()
    return render(request, 'index.html', {'form': form})


def show(request):
    products = Product.objects.all()
    return render(request, 'show.html', {'products': products})


def edit(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'edit.html', {'product': product})


def update(request, id):
    product = Product.objects.get(id=id)
    form = ProductFrom(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect("/shop/show")
    return render(request, 'edit.html', {'product': product})

    # obj = get_object_or_404(Product, id=id)
    # #product = Product.objects.get(id=id)
    # form = ProductFrom(request.POST or None, instance=obj)
    # # form = ProductFrom(request.POST, instance=product)
    # if form.is_valid():
    #     form.save()
    #     return HttpResponseRedirect("/shop/show")
    # return render(request, 'edit.html', {'product': obj})


def destroy(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("/shop/show")

