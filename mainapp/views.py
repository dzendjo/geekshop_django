from django.shortcuts import render
import time
from mainapp.models import ProductCategory, Product

top_menu = [
    {'url': 'main', 'text': 'HOME'},
    {'url': 'products:index', 'text': 'PRODUCTS'},
    {'url': 'contact', 'text': 'CONTACT'}
]

# Create your views here.
def main(request):
    context = {
        'title': 'Главная',
        'top_menu': top_menu
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)
    context = {
        'title': 'Каталог',
        'date': time.strftime("%d %b %Y", time.gmtime()),
        'top_menu': top_menu,
        'products': ProductCategory.objects.all().order_by('name'),
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    locations = [
        {
            'phone': '223-221',
            'email': 'ddd@Ddd.ss',
            'address': 'Django street, 11',
            'state': 'Moscow',

        },
        {
            'phone': '223-222',
            'email': 'ddd@Ddd.ss',
            'address': 'Django street, 11',
            'state': 'Piter',

        },
        {
            'phone': '223-223',
            'email': 'ddd@Ddd.ss',
            'address': 'Django street, 11',
            'state': 'Kazan',

        }
    ]
    context = {
        'title': 'Контакты',
        'locations': locations,
        'top_menu': top_menu
    }
    return render(request, 'mainapp/contact.html', context)

