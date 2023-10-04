from django import forms

LANGUAGES = [
    ('en', 'Angielski'),
    ('zh', 'Chiński mandaryński'),
    ('hindi', 'Hindi'),
    # Dodaj tutaj więcej języków
]

class TranslationForm(forms.Form):
    text_to_translate = forms.CharField(widget=forms.Textarea)
    language = forms.ChoiceField(choices=LANGUAGES)
