from django.db import models

# Create your models here...........models are nothing but the filed of database

class ArticleList(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    body = models.CharField(max_length=100)
    date_of_publish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    