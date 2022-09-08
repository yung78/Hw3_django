from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phone.objects.all()
    sort = request.GET.get("sort", '')
    if sort == 'name':
        phone_objects = Phone.objects.order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.order_by('-price')
    context = {
        'phones': phone_objects
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phone.objects.filter(slug=slug)
    context = {
        'phone': phone_objects[0]
    }

    return render(request, template, context)
