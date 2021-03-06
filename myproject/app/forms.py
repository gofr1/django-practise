from django import forms
from app.models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model= Article
        fields= ["article_id", "title", "text"]
   
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class PictureUploadForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField()

class LoginForm(forms.Form):
   username = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())

class EmailAdmins(forms.Form):
   subject = forms.CharField(max_length = 50)
   message = forms.CharField(max_length = 1024)