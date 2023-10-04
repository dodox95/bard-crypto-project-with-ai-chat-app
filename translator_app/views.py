#skrypt "views.py"
from django.core.cache import cache
from django.http import JsonResponse
from django.utils import timezone
from bardapi import Bard
import os
from django.shortcuts import render, redirect
from .models import ChatHistory, WalletUser
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.decorators import login_required

#os.environ['_BARD_API_KEY'] = "YghS9MRVAnzp6OktHqm1pq77E737VGFtUVvstwSuNfyO0WaNvWFcldjtBGQjaZZWfVJvqw."
#bard = Bard()

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        user_input = request.POST.get('question', '')
        wallet_address = request.POST.get('walletUser', '')
        if not wallet_address:
            return JsonResponse({"error": "No wallet address provided"}, status=400)
        if request.session.session_key is None:
            request.session.create()
        user_key = 'questions_count:' + request.session.session_key
        first_question_time_key = 'first_question_time:' + request.session.session_key
        questions_count = cache.get(user_key, 0)
        first_question_time = cache.get(first_question_time_key)
        if questions_count >= 100:
            wait_time = 60 - (timezone.now() - first_question_time).total_seconds() / 60
            wait_time = max(0, wait_time)  # zapewnienie, że czas oczekiwania nie jest ujemny
            return JsonResponse({"answer": f"You can only ask 100 questions per hour, please try later in {wait_time:.0f} minutes"})
        questions_count += 1
        if questions_count == 1:
            cache.set(first_question_time_key, timezone.now(), 60 * 60)  # cache na 1 godzinę
        cache.set(user_key, questions_count, 60 * 60)  # cache na 1 godzinę
        response = bard.get_answer(user_input)
        user, _ = WalletUser.objects.get_or_create(wallet_address=wallet_address)
        answer = response.get('choices', [{}])[0].get('content', '')
        ChatHistory.objects.create(user=user, message="You: " + user_input)
        ChatHistory.objects.create(user=user, message="Bot: " + ' '.join(answer) if isinstance(answer, list) else answer)
        return JsonResponse({"answer": answer})
    return JsonResponse({"error": "Invalid request"}, status=400)

def login(request):
    return render(request, 'login.html')

def main(request):
    return render(request, 'main.html')

#@login_required
def chat_page(request):
    walletUser = request.GET.get('walletUser')
    sessionWalletUser = request.session.get('walletUser')
    if walletUser and sessionWalletUser and walletUser == sessionWalletUser:
        user, _ = WalletUser.objects.get_or_create(wallet_address=walletUser)
        chat_history = ChatHistory.objects.filter(user=user).order_by('timestamp')
        return render(request, 'chat_page.html', {'chat_history': chat_history, 'walletUser': walletUser})
    else:
        return redirect('login')

def whitepaper(request):
    return render(request, 'whitepaper.html')

def roadmap(request):
    return render(request, 'roadmap.html')
