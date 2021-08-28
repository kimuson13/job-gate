from django.db import models
from django.conf import settings
from django.utils import timezone


# class Post(models.Model):
#     author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     title = models.CharField("タイトル", max_length=200)
#     content = models.TextField('本文')
#     created = models.DateField('作成日', default=timezone.now)

#     def __str__(self):
#         return self.title

class User(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return '('+self.id+')', self.name

