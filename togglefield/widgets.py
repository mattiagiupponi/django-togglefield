from django import forms


class ToggleWidget(forms.RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):
        attrs = {**{"class": "django-toggle-field"}, **}
        return super(ToggleWidget, self).\
            render(name, value, attrs, renderer)
