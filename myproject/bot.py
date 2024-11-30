from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot.models import Product

def start(update: Update,CommandHandler, CallbackContext):
    update.message.reply_text("Сәлем /product командасын теріп,тауарларды көріңіз")

def products(update: Update,CommandHandler, CallbackContext):
    products = Product.objects.all()
    if not products:
        update.message.reply_text("Қазіргі уақытта тауарлар жоқ")
        return
    
    reponse = "Қол жетімді тауарлар :\n\n"
    for product in products:
        reponse += f"{product.name}\n Бағасы: {product.price}теңге\n\n"
    update.message.reply_text(reponse)


def run_bot(token: str):
    updater = Updater(token)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("Start",start))
    dispatcher.add_handler(CommandHandler("products",products))

    updater.start_polling()
    updater.idle()