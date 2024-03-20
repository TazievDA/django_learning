from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting_param = request.GET.get('sort', '')
    if sorting_param == '':
        context = {
            'phones': Phone.objects.all()
        }
    elif sorting_param == 'min_price':
        context = {
            'phones': Phone.objects.all().order_by('price')
        }
    elif sorting_param == 'max_price':
        context = {
            'phones': Phone.objects.all().order_by('-price')
        }
    else:
        context = {
            'phones': Phone.objects.all().order_by(sorting_param)
        }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug)[0]
    }
    return render(request, template, context)
