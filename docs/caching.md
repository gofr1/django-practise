# Caching

To cache something is to save the result of an expensive calculation, so that you don’t perform it the next time you need it. Following is a pseudo code that explains how caching works:

    given a URL, try finding that page in the cache
    
    if the page is in the cache:
       return the cached page
    else:
       generate the page
       save the generated page in the cache (for next time)
       return the generated page

Django comes with its own caching system that lets you save your dynamic pages, to avoid calculating them again when needed. The good point in Django Cache framework is that you can cache:

- The output of a specific view.
- A part of a template.
- Your entire site.

To use cache in Django, first thing to do is to set up where the cache will stay. The cache framework offers different possibilities - cache can be saved in database, on file system or directly in memory. Setting is done in the settings.py file of your project.

## Setting Up Cache in Database

Just add the following in the project `settings.py` file

    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
            'LOCATION': 'cache_tbl',
        }
    }

For this to work and to complete the setting, we need to create the cache table `cache_tbl`. For this, you need to do the following:

    python3 manage.py createcachetable


## Setting Up Cache in File System

Just add the following in the project `settings.py` file:

    CACHES = {
       'default': {
          'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
          'LOCATION': '/var/tmp/django_cache',
       }
    }

## Setting Up Cache in Memory

This is the most efficient way of caching, to use it you can use one of the following options depending on the Python binding library you choose for the memory cache:

    CACHES = {
       'default': {
          'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
          'LOCATION': '127.0.0.1:11211',
       }
    }

Or

    CACHES = {
       'default': {
          'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
          'LOCATION': 'unix:/tmp/memcached.sock',
       }
    }

## Caching a View

If you don’t want to cache the entire site you can cache a specific view. This is done by using the cache_page decorator that comes with Django. Let us say we want to cache the result of the `viewArticles` view:

    from django.views.decorators.cache import cache_page
    
    @cache_page(60 * 15) # 15 minutes
    def searchArticle(request, article_id):
       article = Article.objects.get(article_id = article_id)
       return render(request, 'show-article.html', {'article': article})

As you can see `cache_page` takes the number of seconds you want the view result to be cached as parameter. In our example above, the result will be cached for 15 minutes.

Note - As we have seen before the above view was map to:

    urlpatterns = [
        re_path(r'^article/(.*)/', av.searchArticle)
    ]

Since the URL is taking parameters, each different call will be cached separately. For example, request to `/articles/A0001` will be cached separately to `/articles/A0002`.

## Caching a Template Fragment

You can also cache parts of a template, this is done by using the cache tag. 

    {% load cache %}
    {% extends "main.html" %}
    {% block title %}Some title{% endblock %}

    {% cache 500 content %}
    {% block content %}
    ...
    {% endblock %}
    {% endcache %}

As you can see above, the cache tag will take 2 parameters − the time you want the block to be cached (in seconds) and the name to be given to the cache fragment.