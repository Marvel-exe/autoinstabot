import telebot
import time

bot_token = '1028915212:AAGqKGbhyNyrCjS7zflG5KoxPCdFVy4QG6g'

bot = telebot.TeleBot(token=bot_token)

def find_at(msgs):
    for text in msgs:
        if '@' in text:
            return text

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.reply_to(message, 'welcome!')

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.reply_to(message, 'To use this bot, send a username!')

@bot.message_handler(func=lambda msg: msg.text is not None and '@' in msg.text)
def at_message(message):
    texts = message.text.split()
    at_text = find_at(texts)

    bot.reply_to(message, f'https://instagram.com/{at_text[1:]}/')

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)