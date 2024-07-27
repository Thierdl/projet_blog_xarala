from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.

def index_views(request):
  return render(request, "index.html")


def list_views(request):
  return render(request, "page_s/list_articles.html")


def details_views(request):
  articles = Article.objects.all()
  #article = get_or_404()
  return render(request, "page_s/details_article.html", context={'articles':articles})


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
    return redirect("page2")

  return render(request,"page_s/create_article.html")



def update_article(request, id):

  article = get_object_or_404(Article, id=id)
  if request.method == "POST":
    title = request.POST['title']
    summary = request.POST['summary']
    content = request.POST['content']
    author = request.POST['author']

    Article.objects.filter(id=article.id).update(
      title=title,
      summary=summary,
      content=content,
      author=author
    )

    """
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
    article.title = request.POST.get('title')
    article.summary = request.POST.get('summary')
    article.content = request.POST.get('content')
    article.author = request.POST.get('author')

    article.save()
    """
    return redirect('page2')
    
  return render(request, "page_s/update_article.html", {'article':article})



def delete_article(request, id):
  article = get_object_or_404(Article, id=id)
  if request.method == "POST":
    article = Article.objects.filter(id=article.id)
    article.delete()
    return redirect("page2")

  return render(request, "page_s/delete_article.html")







