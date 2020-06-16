from django.urls import reverse_lazy

from djgentelella.widgets.core import Select, update_kwargs


class AutoCompleteBase:
    def get_autocomplete_base(self):
        class AutocompleteSelectBase(Select):
            template_name = 'gentelella/widgets/autocomplete_select.html'
            option_template_name = 'gentelella/widgets/select_option.html'
            baseurl = None

            def __init__(self, attrs=None, choices=(), extraskwargs=True, multiple=None):
                if extraskwargs:
                    attrs = update_kwargs(attrs, 'AutocompleteSelect', base_class='form-control ')
                if self.baseurl is None:
                    raise ValueError('Autocomplete requires baseurl to work')
                else:
                    self.baseurl = self.baseurl

                if multiple:
                    attrs['multiple'] = "multiple"
                super().__init__(attrs,  choices=choices, extraskwargs=False)

            def get_context(self, name, value, attrs):
                context = super().get_context(name,value,attrs)
                context['url'] = reverse_lazy(self.baseurl)
                return context
        return AutocompleteSelectBase

    def get_autocomplete_multiple(self):
        class AutocompleteSelectMultipleBase(self.get_autocomplete_base()):
            baseurl = None
            allow_multiple_selected = True

            def __init__(self, attrs=None, choices=(), extraskwargs=True):
                if extraskwargs:
                    attrs = update_kwargs(attrs, 'AutocompleteSelectMultiple',  base_class='form-control ')
                super().__init__(attrs, multiple=True, choices=choices, extraskwargs=False)
        return AutocompleteSelectMultipleBase


autocompletes = AutoCompleteBase()


def AutocompleteSelect(baseurl):
    klass = autocompletes.get_autocomplete_base()
    klass.baseurl= baseurl
    return klass


def AutocompleteSelectMultiple(baseurl):
    klass = autocompletes.get_autocomplete_multiple()
    klass.baseurl = baseurl
    return klass