# Template System

## The Render Function

Django makes it possible to separate python and HTML, the python goes in views and HTML goes in templates. To link the two, Django relies on the render function and the Django Template language.
The Render Function

This function takes three parameters:

- `Request` - The initial request.

- `The path to the template` - This is the path relative to the `TEMPLATE_DIRS` option in the project `settings.py` variables.

- `Dictionary of parameters` - A dictionary that contains all variables needed in the template. This variable can be created or you can use `locals()` to pass all local variable declared in the view.

## Django Template Language (DTL)

Django’s template engine offers a mini-language to define the user-facing layer of the application.

A variable looks like this: `{{variable}}`. The template replaces the variable by the variable sent by the view in the third parameter of the render function. 

## Filters

They help you modify variables at display time. Filters structure looks like the following: `{{var|filters}}`

Some examples:

- `{{string|truncatewords:80}}` - This filter will truncate the string, so you will see only the first 80 words.

- `{{string|lower}}` - Converts the string to lowercase.

- `{{string|escape|linebreaks}}` - Escapes string contents, then converts line breaks to tags.

You can also set the default for a variable.

## Tags

Tags lets you perform the following operations: 

- if condition, 
- for loop, 
- template inheritance 

and more.