from django import forms

from .models import Urls


class UrlsForm(forms.ModelForm):

    long_url = forms.URLField(
        widget=forms.URLInput(
            attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Your URL to shorten',
            }
        )
    )

    class Meta:
        model = Urls

        fields = ('long_url',)
