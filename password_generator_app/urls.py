from django.urls import path

from password_generator_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("password", views.password, name="password"),
]
