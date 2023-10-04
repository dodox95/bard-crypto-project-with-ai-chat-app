# models.py
from django.db import models

class WalletUser(models.Model):
    wallet_address = models.CharField(max_length=42, unique=True)
    def __str__(self):
        return self.wallet_address
class ChatHistory(models.Model):
    MESSAGE_TYPES = [
        ('QUESTION', 'Question'),
        ('ANSWER', 'Answer'),
        ('ERROR', 'Error'),
    ]
    user = models.ForeignKey(WalletUser, on_delete=models.CASCADE)
    message = models.TextField()
    message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES, default='ANSWER')
    timestamp = models.DateTimeField(auto_now_add=True)

