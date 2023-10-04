from django import forms
from django.utils.translation import gettext as _


LANGUAGES = [
    ('ar', _('Arabic')),
    ('de', _('German')),
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
    ('italian', _('Italian')),
    ('ja', _('Japanese')),
    ('nl', _('Dutch')),
    ('pl', _('Polish')),
    ('pt', _('Portuguese')),
    ('ru', _('Russian')),
    ('zh', _('Chinese')),
    # Dodaj tutaj więcej języków
]

class TranslationForm(forms.Form):
    text_to_translate = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=LANGUAGES)