from togglefield.widgets import ToggleWidget
from togglefield.forms import ToggleFormField
from django.db import models # noqa


class ToggleField(models.BooleanField):
    default_error_messages = {
        'invalid': ("'%s' is not a Boolean.")
    }

    def __init__(self, *args, **kwargs):
        super(ToggleField, self).__init__(*args, **kwargs)
        self.validate(self.get_default(), None)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': ToggleFormField,
            'widget': ToggleWidget
        }
        defaults.update(**kwargs)
        return super(ToggleField, self).formfield(**defaults)
