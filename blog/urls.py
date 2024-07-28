from django.urls import path
from .import views

urlpatterns = [
  path('', views.index_views, name="index"),
  path('list_views/',views.list_views, name="page1"),
  path('details/<int:id>/', views.details_views, name="page2"),
  path('create_article/', views.create_article, name="page3"),
  path('article/update/<int:id>/',views.update_article, name="page4"),
  path('delete_article/<int:id>/', views.delete_article, name="delete_article"),
]