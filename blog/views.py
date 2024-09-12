from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden


# Create your views here.


def index_views(request):
  return render(request, "index.html")


def list_views(request):
  articles = Article.objects.all()
  paginator = Paginator(articles, 9)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return render(request, "page_s/list_articles.html", {"page_obj":page_obj})


def details_views(request, id):
  article = get_object_or_404(Article, id=id)
  return render(request, "page_s/details_article.html", {"article":article})


@login_required(login_url="/login/")
def create_article(request):
  if request.method == "POST":
    title = request.POST.get("title")
    summary = request.POST.get("summary")
    content = request.POST.get("content")
    image = request.FILES.get("image")

    article = Article.objects.create(
      title=title,
      summary=summary,
      content=content,
      
      author=request.user,
      image=image,
    )

    article.save()
    return redirect("page1")

  return render(request,"page_s/create_article.html")



@login_required(login_url="/login/")
def update_article(request, id):

  articles = get_object_or_404(Article, id=id)

  if request.user != articles.author:
        return HttpResponseForbidden("Vous n'êtes pas autorisé à modifier cet article.")

  if request.method == "POST":
    title = request.POST.get("title")
    summary = request.POST.get("summary")
    content = request.POST.get("content")
    image = request.FILES.get("image")

    articles.title = title
    articles.summary = summary
    articles.content = content
    if image:
        articles.image = image

    articles.save()

    return redirect('page1')
    
  return render(request, "page_s/update_article.html", {'articles':articles})


#delete
@login_required(login_url="/login/")
def delete_article(request, id):
  article = get_object_or_404(Article, id=id)

  if request.user != article.author:
    return HttpResponseForbidden("Vous n'êtes pas autorisé à supprimer cet article.")

  if request.method == "POST":
    article = Article.objects.filter(id=article.id)
    article.delete()
    return redirect("page1")
  
  return render(request, "page_s/delete_article.html", {"article": article})

#paginator
def article_list(request):
    articles = Article.objects.all()  # Récupé toration de tous les articles
    paginator = Paginator(articles, 10)  # Limitation à 10 articles par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'votre_template.html', {'page_obj': page_obj})




