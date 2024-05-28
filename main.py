import telebot
from telebot.types import Message
from tokens import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


# -- BOT ROUTES --

@bot.message_handler()
def start(message: Message):
    user_id = message.from_user.id
    bot.send_message(user_id, message.text)


@bot.message_handler(commands=['start'])
def start(message: Message):
    user_id = message.from_user.id
    bot.send_message(user_id, "Privet")


# -- --

if __name__ == '__main__':
    print("Starting Polling... ")
    bot.infinity_polling()
