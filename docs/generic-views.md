# Generic Views

In some cases, writing views, as we have seen earlier is really heavy. Imagine you need a static page or a listing page. Django offers an easy way to set those simple views that is called generic views.

Unlike classic views, generic views are classes not functions. Django offers a set of classes for generic views in django.views.generic, and every generic view is one of those classes or a class that inherits from one of them.

There are 10+ generic classes:

    >>> import django.views.generic
    >>> dir(django.views.generic)
    
    ['ArchiveIndexView', 'CreateView', 'DateDetailView', DayArchiveView', 'DeleteView', 'DetailView', 'FormView', 'GenericViewError', 'ListView', 'MonthArchiveView', 'RedirectView', 'TemplateView',     'TodayArchiveView', 'UpdateView', 'View', 'WeekArchiveView', 'YearArchiveView',     '__builtins__', '__doc__', '__file__', '__name__', '__package__', '__path__', 'base',     'dates', 'detail', 'edit', 'list']

## Static Pages

Let's publish a static page from the `static.html` template.

    <html>
       <body> 
          This is a static page!!! 
       </body>
    </html>

> If we did that the way we learned before, we would have to change the > `views.py` to be:
> 
>     from django.shortcuts import render
>     
>     def static(request):
>        return render(request, 'static.html', {})
> 
> and `urls.py` to be:
> 
>     from django.conf.urls import patterns, url
>     
>     urlpatterns = re_path(r'^statics/', 'static', name = 'static'),)

The best way is to use generic views. For that, our `views.py` will become:

    from django.views.generic import TemplateView
    
    class StaticView(TemplateView):
       template_name = "static.html"

And our `urls.py` we will be:

    from app.views import StaticView
    
    urlpatterns = re_path(r'^statics/$', StaticView.as_view())

For the same result we can also, do the following:

No change in the `views.py` change the `urls.py` file to be:

    from django.views.generic import TemplateView
    from django.conf.urls import patterns, url
    
    urlpatterns = re_path(r'^statics/',TemplateView.as_view(template_name = 'static.html'))

## List and Display Data from DB

We are going to list all entries in our `Article` model. It is easy to do by using the `ListView` generic view class. 

`urls.py`

    from django.views.generic import ListView
    
    urlpatterns = [
       ...
       path('articles-generic/', ListView.as_view(model = Article, template_name = 'content-generic.html')),
    ]

The associated template

`content-generic.html`

    {% extends "main.html" %}
    {% block title %}Articles generic{% endblock %}
    {% block content %}
    
    {% for article in object_list %}
    <div>
       <h3>{{article.article_id}} - {{article.title}}</h3>
       <p>{{article.text}}</p>
    </div>
    
    {% endfor %}
    {% endblock %}

Important to note at this point is that the variable pass by the generic view to the template is `object_list`. If you want to name it yourself, you will need to add a `context_object_name` argument to the `as_view` method.

`urls.py`

    from django.views.generic import ListView
    
    urlpatterns = [
       ...
       path('articles-generic/', ListView.as_view(model = Article, template_name = 'content-generic.html', context_object_name = 'articles_objects')),
    ]

The associated template

`content-generic.html`

    {% extends "main.html" %}
    {% block title %}Articles generic{% endblock %}
    {% block content %}
    
    {% for article in articles_objects %}
    <div>
       <h3>{{article.article_id}} - {{article.title}}</h3>
       <p>{{article.text}}</p>
    </div>
    
    {% endfor %}
    {% endblock %}