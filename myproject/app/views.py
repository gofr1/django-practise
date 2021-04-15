from django.http import HttpResponse, HttpResponseRedirect
from datetime import date, datetime
from django.shortcuts import render, redirect
from django.template import RequestContext
from random import randint
from app.models import Article, Images
from app.forms import ArticleForm, NameForm, PictureUploadForm, LoginForm
from django.views.decorators.cache import cache_page
from django.shortcuts import render

from django.views.generic import TemplateView

class StaticView(TemplateView):
   template_name = 'static.html'

class HomePageView(TemplateView):
    template_name = 'generic.html'

def hello(request):
   text = """<h1>Welcome to my app!</h1>"""
   return HttpResponse(text)

def viewNumber(request, number):
   text = f'Number: {number}'
   return HttpResponse(text)

def viewDate(request, year, month, day):
   try:
      y, m, d = int(year), int(month), int(day)
      input_date = date(y, m, d)
      text = f'Input: {year}-{month}-{day}'
   except ValueError as v:
      if hasattr(v, 'message'):
         text = v.message
      else:
         text = 'Incorrect date'
   return HttpResponse(text)

def viewCurrentTime(request):
   today = datetime.now().date()
   return render(request, 'today.html', {"today" : today})

def viewString(request, string):
   return render(request, 'string.html', {"string" : string})

def viewTagsIf(request):
   random_number = randint(1,1000)
   return render(request, 'if-case.html', {"random_number" : random_number})

def viewContent(request):
   today = datetime.now().date()
   articles = Article.objects.all()
   return render(request, "content.html", {"today" : today, "articles" : articles})

def showForm(request):
   if request.method == 'POST':
      form = ArticleForm(request.POST)
      if form.is_valid():
         form.save()
      return render(request, 'thanks.html')
   else:
      form = ArticleForm()
      return render(request, 'article.html', {'form': form})

def mainPage(request):
   return redirect(hello)

@cache_page(60 * 15) # 15 minutes
def searchArticle(request, article_id):
   article = Article.objects.get(article_id = article_id)
   return render(request, 'show-article.html', {'article': article})
    
def get_name(request):
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = NameForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
         # process the data in form.cleaned_data as required
         return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
   else:
      form = NameForm()

   return render(request, 'name.html', {'form': form})

def thanksPage(request):
   return render(request, 'thanks.html')

def SavePicture(request):
   saved = False
   
   if request.method == "POST":
      #Get the posted form
      MyPictureUploaForm = PictureUploadForm(request.POST, request.FILES)
      
      if MyPictureUploaForm.is_valid():
         uploads = Images()
         uploads.name = MyPictureUploaForm.cleaned_data["name"]
         uploads.picture = MyPictureUploaForm.cleaned_data["picture"]
         uploads.save()
         saved = True
   else:
      MyPictureUploaForm = PictureUploadForm()
		
   return render(request, 'saved.html', locals())

def formView(request):
   #if request.session.has_key('username'):
   #   username = request.session['username']
   #   return render(request, 'loggedin.html', {"username" : username})
   #else:
   #   return render(request, 'login.html', {})
   if 'username' in request.COOKIES and 'last_connection' in request.COOKIES:
      username = request.COOKIES['username']
      
      last_connection = request.COOKIES['last_connection']
      last_connection_time = datetime.strptime(last_connection[:-7], "%Y-%m-%d %H:%M:%S")
      
      if (datetime.now() - last_connection_time).seconds < 30: # after 30 second you will need to login again
         return render(request, 'loggedin.html', {"username" : username})
      else:
         return render(request, 'login.html', {})
			
   else:
      return render(request, 'login.html', {})
      
def login(request):
   username = 'not logged in'
   
   if request.method == 'POST':
      MyLoginForm = LoginForm(request.POST)
      
      if MyLoginForm.is_valid():
         username = MyLoginForm.cleaned_data['username']
         request.session['username'] = username
      else:
         MyLoginForm = LoginForm()
			
   #return render(request, 'loggedin.html', {"username" : username})
   response = render(request, 'loggedin.html', {"username" : username})
   
   response.set_cookie('last_connection', datetime.now())
   response.set_cookie('username', username)
	
   return response 

def logout(request):
   response = HttpResponse("<strong>You are logged out.</strong>")
   response.delete_cookie('last_connection')
   response.delete_cookie('username')
   return response
   try:
      del request.session['username']
   except:
      pass
   return HttpResponse("<strong>You are logged out.</strong>")
