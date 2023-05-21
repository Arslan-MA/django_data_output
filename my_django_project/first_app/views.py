from django.shortcuts import render
from first_app.models import Product, Pharmacies, User


def project_concept(request):
    return render(request, 'index.html')


def product(request):
    data_product = Product.objects.all()
    context_dict = {"data_product": data_product}
    return render(request, 'index_1.html', context=context_dict)


def pharmacies(request):
    data_pharmacies = Pharmacies.objects.all()
    context_dict = {"data_pharmacies": data_pharmacies}
    return render(request, 'index_2.html', context=context_dict)


def user(request):
    data_user = User.objects.all()
    context_dict = {"data_user": data_user}
    return render(request, 'index_3.html', context=context_dict)
