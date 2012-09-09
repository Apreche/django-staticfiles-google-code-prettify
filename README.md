django-staticfiles-google-code-prettify
=======================================

Easily include google-code-prettify in your django apps

Installation
------------

Install this package using pip

    pip install django-staticfiles-google-code-prettify


Make sure your django project is configured to use staticfiles, then add this to your INSTALLED_APPPS

    INSTALLED_APPS += ['django-staticfiles-google-code-prettify',] 


Usage
-----

You can use this in two different ways in your templates.

### STATIC_URL

    <link href="{{ STATIC_URL }}google-code-prettify/css/prettify.css" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="{{ STATIC_URL }}google-code-prettify/js/prettify.js"></script>

### static template tag

    {% load static from staticfiles %}
    <link href="{% static "google-code-prettify/css/prettify.css" %}" type="text/css" rel="stylesheet" />
    <script type="text/javascript" src="{% static "google-code-prettify/js/prettify.js" %}"></script>
