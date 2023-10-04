# skrypt "urls.py"
from django.urls import path
from .views import login, chat_page, chat, main, whitepaper, roadmap
urlpatterns = [
    path('login/', login, name='login'),
    path('chat/', chat, name='chat'),
    path('chat_page/', chat_page, name='chat_page'),
    path('/', main, name='main'),
    path('whitepaper/', whitepaper, name='whitepaper'),
    path('roadmap/', roadmap, name='roadmap'),
    
]