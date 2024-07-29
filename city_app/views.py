from django.http.request import HttpRequest
from django.shortcuts import render


def catalog_view(request: HttpRequest):
    return render(request, "city_app/home.html")


def choose_city_view(request: HttpRequest):
    return render(request, "city_app/index.html")
