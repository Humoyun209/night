from django.urls import path

from city_app import views


urlpatterns = [
    path("", views.home_view, name="home"),
]
