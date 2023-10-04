from django.contrib import admin
from django.urls import path
from translator_app.views import login, chat_page, chat, main, whitepaper, roadmap

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('login/', login, name='login_again'),
    path('chat_page/', chat_page, name='chat_page'),
    path('chat/', chat, name='chat'),
    path('/', main, name='main'),
    path('', main, name='main'),
    path('whitepaper/', whitepaper, name='whitepaper'),
    path('roadmap/', roadmap, name='roadmap'),
    
]

