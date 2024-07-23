from django.shortcuts import render

# Create your views here.

def list_views(request):
  return render(request, "page_s/list_articles.html")


def details_views(request):
  return render(request, "page_s/details_article.html")


def create_article(request):
  return render(request, "page_s/create_article.html")


def update_article(request):
  return render(request, "page_s/update_article.html")


def delete_article(request):
  return render(request, "page_s/delete_article.html")





