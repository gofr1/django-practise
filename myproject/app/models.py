from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator

class Article(models.Model):
    article_id = models.CharField(primary_key=True, max_length=30, validators=[MinLengthValidator(5)])
    title = models.CharField(max_length=250)
    text = models.CharField(max_length=4096)

    def __str__(self):
        return self.article_id + " - " + self.title + " - " +self.text

class Images(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = 'uploads'

# import sqlite3
# db = sqlite3.connect('db.sqlite3')
# db.execute("SELECT * FROM uploads;").fetchall()
#* [(1, 'a', 'pictures/a.png')]
