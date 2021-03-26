# RESTfull API Django Installation

Install using `pip`:

    pip install djangorestframework
    pip install markdown
    pip install django-filter

Add `rest_framework` to your `INSTALLED_APPS` in `setting.py`.

    INSTALLED_APPS = [
        ...
        'rest_framework',
    ]

Add the following to your root `urls.py` file.

    urlpatterns = [
        ...
        path('api-auth/', include('rest_framework.urls'))
    ]