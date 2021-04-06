from django import forms
from app.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        fields= ["article_id", "title", "text"]
