from django.db import models
from django.conf import settings
from django.urls import reverse
from likes.models import Like

class Article(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE,
    )

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})
    
    def likes_count(self):
        return Like.objects.filter(
            content_type__app_label='articles',
            content_type__model='article',
            object_id=self.id
        ).count()

class Comment(models.Model): # new
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    def __str__(self): 
        return self.comment
    def get_absolute_url(self):
        return reverse("article_list")
