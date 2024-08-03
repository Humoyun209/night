from django.urls import path

from news import views


urlpatterns = [
    path("", views.get_home_page, name="news_home"),
    path("add-comment/", views.add_comment, name="add_comment"),
    path("post/<slug:slug>/", views.get_single_post, name="article_detail"),
]
