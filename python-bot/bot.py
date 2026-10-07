# This is my example to create my own python bot
# My first example

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


START_MESSAGE_TO_SHOW = """
Hola este es un bot creado con el proposito de aprender a usar los telegram bots

Los comandos son los siguientes:
/start /help - muestra ayuda
/hello_kitty - muestra un mensaje sorpresa
/hello  - muestra solo un saludo

"""


# Handler for help
async def start_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(START_MESSAGE_TO_SHOW)

# Handler to say hello kitty
async def say_hello_kitty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Kitty significa hola demonio")

# Handler to say hello
async def say_hello(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Get the user
    user = update.effective_user

    # get the user name 
    name = user.first_name

    # send the message
    await update.message.reply_text(f"Hello {name}!")



# Token API
tkn_api = ""

# First read de token
with open("mytokenapi.env", "r", encoding="utf-8") as archivo:
    tkn_api = archivo.readline()

# Create the app bot
application = ApplicationBuilder().token(tkn_api).build()

# Add handlers
application.add_handler(CommandHandler(["start","help"], start_message))
application.add_handler(CommandHandler("hello_kitty", say_hello_kitty))
application.add_handler(CommandHandler("hello", say_hello))

# add polling 
application.run_polling(allowed_updates=Update.ALL_TYPES)
