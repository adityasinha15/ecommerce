from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact
from math import ceil

def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/4) - (n//4))
    #params = {'products':products, 'nSlides':nSlides, 'range':range(1, nSlides)}
    #all_prods = [[products, range(1, nSlides), nSlides],
                # [products, range(1, nSlides), nSlides]]
    all_prods = []
    catprods = Product.objects.values('category')
    cats = {item['category'] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        all_prods.append([prod, range(1, nSlides), nSlides])

    params = {'all_prods': all_prods}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method == 'GET':
        return render(request, 'shop/contact.html')
    else:
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return render(request, 'shop/contact.html', {'msg': 'Succesfully Submitted'})

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request, myid):
    product = Product.objects.filter(id = myid)
    return render(request, 'shop/prodview.html', {'product': product[0]})

def checkout(request):
    return render(request, 'shop/checkout.html')