from django.test import TestCase
from django.contrib.auth.models import User
from .models import Article

class TestArticleModels(TestCase):
    def setUp(self):
      #creer un user
      self.user = User.objects.create_user(username="albert", password="12345")

      #creer un article
      self.data_article = Article.objects.create(
        title="xarala",
        summary="xarala2025",
        content="xaralatech",
        author=self.user
        )

    def test_content_article(self):
        self.assertEqual(self.data_article.title, "xarala")
        self.assertEqual(self.data_article.summary, "xarala2025")
        self.assertEqual(self.data_article.content, "xaralatech")
        self.assertEqual(self.data_article.author, self.user)


        
"""
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


"""

















"""
class ArticleModelTest(TestCase):
    def setUp(self):
        # Créez un utilisateur pour l'auteur
        self.user = User.objects.create_user(username="testuser", password="password123")
        
        # Créez un article de test
        self.article = Article.objects.create(
            title="Test Article",
            summary="This is a test summary.",
            content="This is the content of the test article.",
            author=self.user
        )

    def test_article_content(self):
        # Vérifiez que les champs contiennent les bonnes données
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.summary, "This is a test summary.")
        self.assertEqual(self.article.content, "This is the content of the test article.")
        self.assertEqual(self.article.author, self.user)
        self.assertIsNotNone(self.article.date_create)
        self.assertIsNotNone(self.article.date_updat)

    def test_article_str_representation(self):
        # Vérifiez la méthode __str__
        expected_str = f"{self.article.title} {self.article.author} {self.article.date_create}"
        self.assertEqual(str(self.article), expected_str)

"""