from django.urls import path
from . import views
urlpatterns = [
path("login/", views.login, name = "login"),
path("", views.homepage, name ="homepage"),
path("login/create/", views.create, name ="create"),
]