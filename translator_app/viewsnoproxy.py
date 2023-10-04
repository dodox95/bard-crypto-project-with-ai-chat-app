from django.http import JsonResponse
from bardapi import Bard
import os
import time
from django.shortcuts import render


# Ustawienie klucza API BARD
os.environ['_BARD_API_KEY'] = "YgheGCDGmTk7_p6awlJPpdvqJ4mlq1JdwOsHe-5wwMMNMW78clB5a6IwmLF4fei6QPGKyA."

# Inicjalizacja instancji Bard
bard = Bard()

def chat(request):
    if request.method == 'GET':
        # Pobranie pytania od użytkownika
        user_input = request.GET.get('question', '')

        # Wywołanie funkcji get_answer z Bard API
        response = bard.get_answer(user_input)

        # Odpowiedź wysyłana do użytkownika
        answer = response.get('choices', [{}])[0].get('content', '')
        
        return JsonResponse({"answer": answer})

    return JsonResponse({"error": "Invalid request"}, status=400)

def login(request):
    return render(request, 'login.html')

def main(request):
    return render(request, 'main.html')
    
def chat_page(request):
    # Your view logic here
    return render(request, 'chat_page.html')