from django.urls import path

from city_app import views


urlpatterns = [
    path("catalog/", views.catalog_view, name="home"),
    path("", views.choose_city_view, name="city"),
]
