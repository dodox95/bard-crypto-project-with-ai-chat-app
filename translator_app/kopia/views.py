from django.shortcuts import render
import openai
from .forms import TranslationForm  # upewnij się, że istnieje plik forms.py i ma w sobie TranslationForm

openai.api_key = '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'  # Replace this with your actual API key

def index(request):
    translation = ''
    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text_to_translate']
            target_language = form.cleaned_data['language']
            prompt = f"Translate the following English text to {target_language}: '{text}'"
            response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=60)
            translation = response.choices[0].text.strip()
    else:
        form = TranslationForm()
    return render(request, 'index.html', {'form': form, 'translation': translation})
