# Django’s forms

Django’s form functionality can simplify and automate vast portions of this work, and can also do it more securely than most programmers would be able to do in code they wrote themselves.

Django handles three distinct parts of the work involved in forms:

- preparing and restructuring data to make it ready for rendering
- creating HTML forms for the data
- receiving and processing submitted forms and data from the client

It is possible to write code that does all of this manually, but Django can take care of it all for you.

We’ve described HTML forms briefly, but an HTML <form> is just one part of the machinery required.

In the context of a Web application, `form` might refer to that HTML <form>, or to the Django Form that produces it, or to the structured data returned when it is submitted, or to the end-to-end working collection of these parts.

# Building a form in Django

## The Form class

We already know what we want our HTML form to look like. Our starting point for it in Django is this:

`forms.py`

    from django import forms
    
    class NameForm(forms.Form):
        your_name = forms.CharField(label='Your name', max_length=100)

## The view

Form data sent back to a Django website is processed by a view, generally the same view which published the form. This allows us to reuse some of the same logic.

To handle the form we need to instantiate it in the view for the URL where we want it to be published:

`views.py`

    from django.http import HttpResponseRedirect
    from django.shortcuts import render
    
    from .forms import NameForm
    
    def get_name(request):
        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            form = NameForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required
                # ...
                # redirect to a new URL:
                return HttpResponseRedirect('/thanks/')
    
        # if a GET (or any other method) we'll create a blank form
        else:
            form = NameForm()
    
        return render(request, 'name.html', {'form': form})

## The template

We don’t need to do much in our `name.html` template:

    <form action="/your-name/" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
    </form>