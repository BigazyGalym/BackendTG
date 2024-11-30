import os 
from django.core.management.base import BaseCommand
from  myproject.bot import run_bot

class Command(BaseCommand):
    help = "Telegram ботты іске қосу"

    def handle(self , *args , **kwargs):
        token  = os.getenv("7864276086:AAG4HSa9MfHQBAgzTlhKRK6nJt-Wb0J9SgE")
        if not token:
            self.stderr.write("7864276086:AAG4HSa9MfHQBAgzTlhKRK6nJt-Wb0J9SgE қате")
            return
        self.stdout.write("Бот іске қосылуда...")
        run_bot(token)
        