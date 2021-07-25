from django import forms


class ToggleFieldWidget(forms.RadioSelect):
    def render(self, name, value, attrs=None, renderer=None):
        return super(ToggleFieldWidget, self).\
            render(name, value, attrs, renderer)
