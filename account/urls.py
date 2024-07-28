from django.urls import path
from .import views


urlpattern = [
  path('login', views.login_views, name="login"),
]