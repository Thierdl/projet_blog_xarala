from django.urls import path
from .import views

urlpatterns = [
  path('', views.index_views, name="index"),
  path('list_article/',views.list_views, name="page1"),
  path('details_article/', views.details_views, name="page2"),
  path('create_article/', views.create_article, name="page3"),
  path('article/<int:id>/update/',views.update_article, name="page4"),

]