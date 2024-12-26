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
