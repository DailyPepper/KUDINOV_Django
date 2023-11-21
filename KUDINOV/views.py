from typing import Dict
from django.shortcuts import render, redirect
from .models import Product, Customer, Review
from .forms import CustomerForm
from .forms import ReviewForm



def index(request):
    return render(request, 'KUDINOV/index.html')


def contact(request):
    error = ''
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            error = 'Форма была неверной'

    form = ReviewForm()

    data: dict[str, ReviewForm] = {
        'form': form,
        'error': error
    }

    return render(request, 'KUDINOV/contact.html', data)


def about(request):
    error = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        else:
            error = 'Форма была неверной'

    form = CustomerForm()

    data: dict[str, CustomerForm] = {
        'form': form,
        'error': error
    }

    return render(request, 'KUDINOV/auto.html', data)


def my_view(request):
    # Создание объектов и их связывание
    product1 = Product.objects.create(name='Product 1')
    product2 = Product.objects.create(name='Product 2')

    customer = Customer.objects.create(first_name='John', last_name='Doe', email='john@example.com', gender='M')
    customer.products.add(product1, product2)

    # Получение связанных объектов
    related_products = customer.products.all()

    # Остальной код представления
    return render(request, 'my_template.html', {'related_products': related_products})




