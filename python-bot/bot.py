# This is my example to create my own python bot
# My first example

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# Handler to say hello
async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Kitty significa hola demonio")



# Token API
tkn_api = ""

# First read de token
with open("mytokenapi.env", "r", encoding="utf-8") as archivo:
    tkn_api = archivo.readline()

# Create the app bot
application = ApplicationBuilder().token(tkn_api).build()

# Add handlers
application.add_handler(CommandHandler("hello", say_hello))

# add polling 
application.run_polling(allowed_updates=Update.ALL_TYPES)
