from django.http.request import HttpRequest
from django.shortcuts import render


def home_view(request: HttpRequest):
    return render(request, "city_app/home.html")
