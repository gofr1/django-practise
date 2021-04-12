"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework.routers import SimpleRouter
from django.views.generic import ListView, TemplateView

from post.views import PostViewSet
import app.views as av
from app.models import Article

router = SimpleRouter()
router.register('posts', PostViewSet)

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('appstaff/', admin.site.urls),
    #path('', include(router.urls)),
    path('', av.mainPage),
    path('api-auth/', include('rest_framework.urls')),
    path('hello/', av.hello),
    re_path(r'^number/(\d+)/', av.viewNumber),
    re_path(r'^date/(\d{1,5})/(\d{1,2})/(\d{1,2})', av.viewDate),
    path('today/', av.viewCurrentTime),
    re_path(r'^string/(.*)/', av.viewString),
    path('random/', av.viewTagsIf),
    path('articles/', av.viewContent),
    path('postarticle/', av.showForm),
    re_path(r'^article/(.*)/', av.searchArticle),
    path('your-name/', av.get_name),
    path('thanks/', av.thanksPage),
    path('statics/', av.StaticView.as_view()),
    #path('articles-generic/', ListView.as_view(model = Article, template_name = 'content-generic.html')),
    path('articles-generic/', ListView.as_view(model = Article, template_name = 'content-generic.html', context_object_name = 'articles_objects')),
    path('upload/', TemplateView.as_view(template_name = 'picture-upload.html')),
    path('saved/', av.SavePicture),
    path('connection/',av.formView),
    path('login/', av.login),
    path('logout/', av.logout),
]