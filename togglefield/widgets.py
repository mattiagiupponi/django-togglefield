from django import forms


class ToggleSwitchWidget(forms.RadioSelect):
    input_type = 'radio'
    template_name = 'django/forms/widgets/radio.html'

    def render(self, name, value, attrs=None, renderer=None):
        attrs = {**{"class": "django-toggle-field"}, **attrs}
        return super(ToggleSwitchWidget, self).\
            render(name, value, attrs, renderer)
