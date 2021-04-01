from django.http import HttpResponse
from datetime import date, datetime
from django.shortcuts import render

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