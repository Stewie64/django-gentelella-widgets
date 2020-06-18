Django Gentelella widgets
############################

This app helps you to integrate Django apps with `Gentelella <https://colorlib.com/polygon/gentelella/index.html>`_ building extra widgets for forms and speciall methods to render forms in templates.

Installation
________________

Installing from repository (not in pip yet).

.. code:: bash

   pip install git+https://github.com/luisza/django-gentelella-widgets.git#egg=djgentelella

When pip is ready you can do

.. code:: bash

   pip install djgentelella

Configure your settings

.. code:: bash

    INSTALLED_APPS = [ ..
        'djgentelella',
        'mptt',
    ]

Run migrations 

.. code:: bash

    python manage.py migrate

Create statics files downloading from internet (you need to install requests for this step).

.. code:: bash

     pip install requests
     python manage.py loaddevstatic
     
Usage
_________


In forms 

.. code:: python

    from djgentelella.forms.forms import CustomForm
    from djgentelella.widgets import core as genwidgets

    class myform(CustomForm, forms.ModelForm):
        class Meta:
            model = MyObject
            fields = '__all__'
            widgets = {
                'name': genwidgets.TextInput,
                'borddate': genwidgets.DateInput,
                'email': genwidgets.EmailMaskInput
            }

In templates working with forms

.. code:: html

     {{ form.as_plain }}
     {{ form.as_inline }}
     {{ form.as_horizontal }}

In templates using base template

.. code:: html

    {% extends 'gentelella/base.html' %}
    
Take a look this file to note the template block that you can overwrite

Usage of AutocompleteSelect and AutocompleteSelectMultiple
__________________________________________________________

Use almost same format of other widgets except they need a registered url to work with,
the registered url must be send via widget initialization as the example below

.. code:: python

    from djgentelella.forms.forms import CustomForm
    from djgentelella.widgets import core as genwidgets

    class myform(CustomForm, forms.ModelForm):
        class Meta:
            model = MyObject
            fields = '__all__'
            widgets = {
                'field_name': genwidgets.AutocompleteSelect('url'),
                'field_name': genwidgets.AutocompleteSelectMultiple('url'),
            }

To make a url available for usage we need to create a class with the next requirements:

- Import register_lookups decorator and GModelLookup class, both elements work together to make crud routes in a simple way and expose those routes with the given names used in decorator
- Then create a class that inherits from GModelLookup, inside the class proceed to edit model and fields params, the first to give a model to work and the second is a list of fields in that model that user want to be used as filter
- Finally, add a @register_lookups decorator to the class with the params prefix needed by the class and basename which is required by the class to format the urls created dynamically
- In below example we create a lookup with Person model and use name as field filter, so we give the prefix person to represent the class and for basename we use personbasename but any meaningful name could be used.

.. code:: python


        from djgentelella.groute import register_lookups
        from djgentelella.select_view import GModelLookup


        @register_lookups(prefix="person", basename="personbasename")
        class PersonGModelLookup(GModelLookup):
            model = Person
            fields = ['name']

widgets
__________

There are several widgets implemented this is a list of what you can use

- TextInput
- NumberInput
- EmailInput
- URLInput
- PasswordInput
- Textarea
- TextareaWysiwyg (not working yet)
- DateInput
- DateTimeInput
- TimeInput
- CheckboxInput
- YesNoInput
- Select  (jquery select2)
- SelectMultiple (jquery select2)
- SelectTail
- SelectMultipleTail
- RadioSelect
- NullBooleanSelect
- CheckboxSelectMultiple
- SplitDateTimeWidget (not ready)
- SplitHiddenDateTimeWidget (not ready)
- SelectDateWidget (not ready)
- PhoneNumberMaskInput
- DateMaskInput
- DateTimeMaskInput
- EmailMaskInput
- DateRangeTimeInput
- DateRangeInput
- AutocompleteSelect
- AutocompleteSelectMultiple


