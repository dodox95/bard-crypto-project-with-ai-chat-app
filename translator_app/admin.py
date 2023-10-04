from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import WalletUser, ChatHistory

admin.site.register(WalletUser)
admin.site.register(ChatHistory)
