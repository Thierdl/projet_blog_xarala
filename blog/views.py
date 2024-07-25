from django.shortcuts import render, redirect
from .models import Article

# Create your views here.

def index_views(request):
  return render(request, "index.html")


def list_views(request):
  return render(request, "page_s/list_articles.html")


def details_views(request):
  return render(request, "page_s/details_article.html")


#def create_article(request):
#  return render(request, "page_s/create_article.html")

def create_article(request):
  if request.method == "POST":
    title = request.POST["title"]
    summary = request.POST["summary"]
    content = request.POST["content"]
    author = request.POST["author"]

    article = Article.objects.create(
      title=title,
      summary=summary,
      content=content,
      author=author,
    )

    article.save()
    #return redirect("page_s/list_articles.html")

  return render(request,"page_s/create_article.html")


def update_article(request):
  return render(request, "page_s/update_article.html")


def delete_article(request):
  return render(request, "page_s/delete_article.html")







