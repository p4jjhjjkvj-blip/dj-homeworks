from django.shortcuts import get_object_or_404, redirect, render

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    phones = Phone.objects.all()
    sort_order = request.GET.get('sort')

    if sort_order == 'name':
        phones = phones.order_by('name')
    elif sort_order == 'min_price':
        phones = phones.order_by('price')
    elif sort_order == 'max_price':
        phones = phones.order_by('-price')

    return render(request, 'catalog.html', {'phones': phones})


def show_product(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, 'product.html', {'phone': phone})
