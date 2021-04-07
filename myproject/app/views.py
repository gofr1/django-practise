from django.http import HttpResponse
from datetime import date, datetime
from django.shortcuts import render, redirect

from random import randint
from app.models import Article
from app.forms import ArticleForm

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
   # if this is a POST request we need to process the form data
   if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = ArticleForm(request.POST)
      # check whether it's valid:
      if form.is_valid():
         form.save()
      return render(request, 'thanks.html')
   else:
      form = ArticleForm()
      return render(request, 'article.html', {'form': form})

def mainPage(request):
   return redirect(hello)

def searchArticle(request, article_id):
   article = Article.objects.get(article_id = article_id)
   return render(request, 'show-article.html', {'article': article})