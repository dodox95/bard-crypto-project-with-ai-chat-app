# Generated by Django 4.2.3 on 2023-07-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator_app', '0002_chathistory_message_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletuser',
            name='wallet_address',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
