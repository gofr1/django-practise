from django.http import HttpResponse
from datetime import date, datetime
from django.shortcuts import render

from random import randint
from app.models import Article


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