from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

class Article(models.Model):
    article_id = models.CharField(primary_key=True, max_length=30, validators=[MinLengthValidator('5')])
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=4096)

    def __str__(self):
        return self.article_id + " - " + self.title + " - " +self.text