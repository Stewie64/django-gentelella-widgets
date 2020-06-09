import json

from django.forms import (PasswordInput as DJPasswordInput, FileInput as DJFileInput,
                          ClearableFileInput as DJClearableFileInput, Textarea as DJTextarea,
                          DateInput as DJDateInput, DateTimeInput as DJDateTimeInput,
                          TimeInput as DJTimeInput, CheckboxInput as DJCheckboxInput, Select as DJSelect,
                          SplitHiddenDateTimeWidget as DJSplitHiddenDateTimeWidget,
                          CheckboxSelectMultiple as DJCheckboxSelectMultiple, SelectMultiple as DJSelectMultiple,
                          SelectDateWidget as DJSelectDateWidget, SplitDateTimeWidget as DJSplitDateTimeWidget)
from django.forms.widgets import Input as DJInput
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext as _
from django import forms
from django.forms.utils import flatatt
from django.template.defaultfilters import force_escape
from django.template.loader import render_to_string
from django.utils.encoding import force_text
from django.utils.module_loading import import_string
from django.utils.safestring import mark_safe
from django.conf import settings
from djgentelella import registry


def _media(self):
    js = ['admin/js/jquery.init.js']

    # Unless AJAX_SELECT_BOOTSTRAP == False
    # then load include bootstrap which will load jquery and jquery ui + default css as needed
    if getattr(settings, "AJAX_SELECT_BOOTSTRAP", True):
        js.append('ajax_select/js/bootstrap.js')

    js.append('ajax_select/js/ajax_select.js')

    return forms.Media(css={'all': ('ajax_select/css/ajax_select.css',)}, js=js)

def update_kwargs(attrs, widget, base_class='form-control '):
    if attrs is not None:
        attrs = attrs.copy()

    if attrs is None:
        attrs = {}
    if 'class' in attrs:
        attrs.update({'class':  base_class + attrs['class']})
    else:
        attrs.update({'class': base_class })
    attrs['data-widget'] = widget
    return attrs

class Input(DJInput):
    """
    Base class for all <input> widgets.
    """
    template_name = 'gentelella/widgets/input.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class TextInput(Input):
    input_type = 'text'
    template_name = 'gentelella/widgets/text.html'


class NumberInput(Input):
    input_type = 'number'
    template_name = 'gentelella/widgets/number.html'
    # min_value y max_value
    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, extraskwargs=extraskwargs)

"""
class NumberKnobInput(Input):
    input_type = 'number'
    template_name = 'gentelella/widgets/number.html'
    # min_value y max_value
    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='')
        if 'max_value' in attrs:
            attrs['data-max'] = attrs['max_value']
        if 'min_value' in attrs:
            attrs['data-min'] = attrs['min_value']
        super().__init__(attrs, extraskwargs=extraskwargs)
"""
class EmailInput(Input):
    input_type = 'email'
    template_name = 'gentelella/widgets/email.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, extraskwargs=extraskwargs)

class URLInput(Input):
    input_type = 'url'
    template_name = 'gentelella/widgets/url.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        attrs['placeholder'] = 'https://'
        super().__init__(attrs, extraskwargs=extraskwargs)

class PasswordInput(DJPasswordInput):
    input_type = 'password'
    template_name = 'gentelella/widgets/password.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)
#Fixme: do upload view
class FileInput(DJFileInput):
    input_type = 'file'
    needs_multipart_form = True
    template_name = 'gentelella/widgets/file.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='djgentelella-file-input form-control')
        if 'data-href' not in attrs:
            attrs.update({'data-href': reverse_lazy('upload_file_view')})
        if 'data-done' not in attrs:
            attrs['data-done'] = reverse_lazy('upload_file_done')
        super().__init__(attrs)


class ClearableFileInput(DJClearableFileInput):
    template_name = 'gentelella/widgets/file.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)


class Textarea(DJTextarea):
    template_name = 'gentelella/widgets/textarea.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='resizable_textarea form-control')
        attrs['rows']='3'
        super().__init__(attrs)

class TextareaWysiwyg(DJTextarea):
    template_name = 'gentelella/widgets/wysiwyg.html'

    def __init__(self, attrs=None, extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='form-control')

        super().__init__(attrs)

class DateInput(DJDateInput):
    """
    .. warning::
        Set in settings

            USE_L10N = False

            DATE_INPUT_FORMATS=[ '%Y-%m-%d','%d/%m/%Y','%d/%m/%y']

        By limitation on js datetime widget format conversion
    """
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'gentelella/widgets/date.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)




class DateTimeInput(DJDateTimeInput):
    """
    .. warning::
        Set in settings

            USE_L10N = False

            DATETIME_INPUT_FORMATS=[ '%m/%d/%Y %H:%M %p' ]

        By limitation on js datetime widget format conversion
    """

    format_key = 'DATETIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/datetime.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)



class TimeInput(DJTimeInput):
    format_key = 'TIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/time.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)
        self.format = format or "%H:%M:%S"

class CheckboxInput(DJCheckboxInput):
    input_type = 'checkbox'
    template_name = 'gentelella/widgets/checkbox.html'


    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__, base_class='flat ')
        super().__init__(attrs)
        self.format = format or None

class YesNoInput(DJCheckboxInput):
    input_type = 'checkbox'
    template_name = 'gentelella/widgets/checkyesno.html'


    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__, base_class='js-switch')

        super().__init__(attrs)
        self.format = format or None


class Select(DJSelect):
    input_type = 'select'
    template_name = 'gentelella/widgets/select.html'
    option_template_name = 'gentelella/widgets/select_option.html'
    add_id_index = False
    checked_attribute = {'selected': True}
    option_inherits_attrs = False

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='select2_single form-control ')
        super().__init__(attrs,  choices=choices)

class SelectWithAdd(Select):
    template_name = 'gentelella/widgets/addselect.html'
    option_template_name = 'gentelella/widgets/select_option.html'


    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                                  base_class='form-control ')
        if 'add_url' not in attrs:
            raise ValueError('SelectWithAdd requires add_url in attrs')
        super().__init__(attrs,  choices=choices, extraskwargs=False)

class SelectTail(DJSelect):
    input_type = 'select'
    template_name = 'gentelella/widgets/select.html'
    option_template_name = 'gentelella/widgets/select_option.html'
    add_id_index = False
    checked_attribute = {'selected': True}
    option_inherits_attrs = False

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__, base_class='select2_single form-control ')
        super().__init__(attrs,  choices=choices)

class SelectMultiple(DJSelectMultiple):
    allow_multiple_selected = True

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='select2_multiple form-control ')
        super(SelectMultiple, self).__init__(attrs, choices=choices)

class SelectMultipleAdd(SelectMultiple):
    allow_multiple_selected = True
    template_name = 'gentelella/widgets/addselect.html'
    option_template_name = 'gentelella/widgets/select_option.html'

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='select2_multiple form-control ')
        super(SelectMultipleAdd, self).__init__(attrs, choices=choices, extraskwargs=False)

class SelectMultipleTail(DJSelectMultiple):
    allow_multiple_selected = True

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='form-control ')
        super().__init__(attrs, choices=choices)



class RadioSelect(Select):
    input_type = 'radio'
    template_name = 'gentelella/widgets/radio.html'
    option_template_name = 'gentelella/widgets/attrs.html'

    def __init__(self, attrs=None, choices=(), extraskwargs=True):
        if extraskwargs:
            attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, choices=choices, extraskwargs=extraskwargs)

class NullBooleanSelect(RadioSelect):

    def __init__(self, attrs=None, choices = (
                                    ('unknown', _('Unknown')),
                                    ('true', _('Yes')),
                                    ('false', _('No')),
                                    )):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, choices=choices, extraskwargs=False)

    def format_value(self, value):
        try:
            return {
                True: 'true', False: 'false',
                'true': 'true', 'false': 'false',
                # For backwards compatibility with Django < 2.2.
                '2': 'true', '3': 'false',
            }[value]
        except KeyError:
            return 'unknown'

    def value_from_datadict(self, data, files, name):
        value = data.get(name)
        return {
            True: True,
            'True': True,
            'False': False,
            False: False,
            'true': True,
            'false': False,
            # For backwards compatibility with Django < 2.2.
            '2': True,
            '3': False,
        }.get(value)




class CheckboxSelectMultiple(DJCheckboxSelectMultiple):
    input_type = 'checkbox'
    template_name = 'gentelella/widgets/checkbox_select.html'
    option_template_name = 'gentelella/widgets/checkbox_option.html'

    def __init__(self, attrs=None, check_test=None):
        attrs = update_kwargs(attrs, self.__class__.__name__,
                              base_class='flat ')
        super().__init__(attrs)

class SplitDateTimeWidget(DJSplitDateTimeWidget):
    template_name = 'gentelella/widgets/splitdatetime.html'
    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class SplitHiddenDateTimeWidget(DJSplitHiddenDateTimeWidget):
    template_name = 'gentelella/widgets/splithiddendatetime.html'
    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class SelectDateWidget(DJSelectDateWidget):
    template_name = 'gentelella/widgets/select_date.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class PhoneNumberMaskInput(TextInput):
    input_type = 'text'
    template_name = 'gentelella/widgets/phone_number_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)

        super().__init__(attrs)

class DateMaskInput(DJDateInput):
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'gentelella/widgets/date_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class DateTimeMaskInput(DJDateTimeInput):
    format_key = 'DATETIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/datetime_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs)

class EmailMaskInput(TextInput):
    template_name = 'gentelella/widgets/email_input_mask.html'

    def __init__(self, attrs=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)

        super().__init__(attrs)

class DateRangeTimeInput(DJDateTimeInput):
    format_key = 'DATETIME_INPUT_FORMATS'
    template_name = 'gentelella/widgets/daterangetime.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)


class DateRangeInput(DJDateInput):
    format_key = 'DATE_INPUT_FORMATS'
    template_name = 'gentelella/widgets/daterange.html'

    def __init__(self, attrs=None, format=None):
        attrs = update_kwargs(attrs, self.__class__.__name__)
        super().__init__(attrs, format=format)

json_encoder = import_string(getattr(settings, 'AJAX_SELECT_JSON_ENCODER',
                                     'django.core.serializers.json.DjangoJSONEncoder'))


class AutocompleteWidget(TextInput):

    channel = None
    help_text = ''
    html_id = ''

    def __init__(self,
                 channel,
                 help_text='',
                 show_help_text=True,
                 plugin_options=None,
                 *args,
                 **kwargs):
        self.plugin_options = plugin_options or {}
        super(TextInput, self).__init__(*args, **kwargs)
        self.channel = channel
        self.help_text = help_text
        self.show_help_text = show_help_text

    def render(self, name, value, attrs=None, renderer=None, **_kwargs):
        value = value or ''

        final_attrs = self.build_attrs(self.attrs)
        final_attrs.update(attrs or {})
        final_attrs.pop('required', None)
        self.html_id = final_attrs.pop('id', name)

        current_repr = ''
        initial = None
        lookup = registry.get(self.channel)
        if value:
            objs = lookup.get_objects([value])
            try:
                obj = objs[0]
            except IndexError:
                raise Exception("%s cannot find object:%s" % (lookup, value))
            current_repr = lookup.format_item_display(obj)
            initial = [current_repr, obj.pk]

        if self.show_help_text:
            help_text = self.help_text
        else:
            help_text = ''

        context = {
            'name': name,
            'html_id': self.html_id,
            'current_id': value,
            'current_repr': current_repr,
            'help_text': help_text,
            'extra_attrs': mark_safe(flatatt(final_attrs)),
            'func_slug': self.html_id.replace("-", ""),
            'add_link': self.add_link,
        }
        context.update(
            make_plugin_options(lookup, self.channel, self.plugin_options, initial))
        templates = (
            'ajax_select/autocompleteselect_%s.html' % self.channel,
            'ajax_select/autocompleteselect.html')
        out = render_to_string(templates, context)
        return mark_safe(out)

    def value_from_datadict(self, data, files, name):
        return data.get(name, None)

    def id_for_label(self, id_):
        return '%s_text' % id_


def make_plugin_options(lookup, channel_name, widget_plugin_options, initial):
    """ Make a JSON dumped dict of all options for the jQuery ui plugin."""
    po = {}
    if initial:
        po['initial'] = initial
    po.update(getattr(lookup, 'plugin_options', {}))
    po.update(widget_plugin_options)
    if not po.get('source'):
        po['source'] = reverse('ajax_lookup', kwargs={'channel': channel_name})

    # allow html unless explicitly set
    if po.get('html') is None:
        po['html'] = True

    return {
        'plugin_options': mark_safe(json.dumps(po, cls=json_encoder)),
        'data_plugin_options': force_escape(
                json.dumps(po, cls=json_encoder)
        )
    }
