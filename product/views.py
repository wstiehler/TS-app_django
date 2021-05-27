from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def product(request):
    return render(request, 'product.html')


def product_form(request):
    return render(request, 'product_form.html')