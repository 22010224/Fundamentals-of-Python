from translate.py import translate
import telebot

TOKEN = "6239234378:AAFu9PIoTRRZy3ljVNeOCL08iZrnpgxHqHA"
tarjimonbot = telebot.Telebot(token=TOKEN)

#/start commmand
@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu alaykum, Translator Samandar botiga xush kelibsiz!"
    xabar += '\nMatningizni yuboring'
    tarjimonbot.reply_to(message, xabar)
    # function for texts
    @tarjimonbot.message_handler(func=lambda msg:  msg.text is not None)
    def tarjima(message):
        msg = message.text
    tarjimonbot.reply_to(message, translate(msg))

#starting the bot
tarjimonbot.polling()