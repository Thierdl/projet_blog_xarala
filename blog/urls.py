from django.urls import path
from .import views

urlpatterns = [
  path('page1/',views.list_views, name="list of articles"),
  path('page2/', views.details_views, name="details article"),
  path('page3/', views.create_article, name="create article"),

]