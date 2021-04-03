from django.http import HttpResponse
from datetime import date, datetime
from django.shortcuts import render

from random import randint

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
   
   articles = [
      {
         'title': 'Lorem ipsum',
         'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. '
      },
      {
         'title': 'Sed ut perspiciatis',
         'text': 'Sed ut perspiciatis, unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam eaque ipsa, quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt, explicabo. Nemo enim ipsam voluptatem, quia voluptas sit, aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos, qui ratione voluptatem sequi nesciunt, neque porro quisquam est, qui dolorem ipsum, quia dolor sit, amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt, ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit, qui in ea voluptate velit esse, quam nihil molestiae consequatur, vel illum, qui dolorem eum fugiat, quo voluptas nulla pariatur? At vero eos et accusamus et iusto odio dignissimos ducimus, qui blanditiis praesentium voluptatum deleniti atque corrupti, quos dolores et quas molestias excepturi sint, obcaecati cupiditate non provident, similique sunt in culpa, qui officia deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi optio, cumque nihil impedit, quo minus id, quod maxime placeat, facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet, ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis doloribus asperiores repellat. '
      }]
   return render(request, "content.html", {"today" : today, "articles" : articles})