import telebot
from config import TOKEN,values
from extensions import APIException,ValuesConverter

bot=telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start','help'])
def start(message):
    text="Привет,это бот-конвертер валют. Чтобы начать работу введите команду в бот в следующем формате " \
         "\n<валюта> <валюта в которую хотите перевести> <количесто валюты>.\nЧтобы узнать доступные валюты нажмите /values"
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands=['values'])
def help_value(message):
    text=''
    for i in values.keys():
        text+=i+'\n'
    bot.send_message(message.chat.id,text)

@bot.message_handler(content_types=['text'])
def exchange(message):
    try:
        text = message.text.split(' ')
        if len(text) != 3:
            raise APIException('Неверное количество параметров,их должно быть 3')
        qoute, base, amount = text
        answer = ValuesConverter.get_price(qoute, base, amount)
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:

        bot.send_message(message.chat.id,answer)

bot.polling(none_stop=True)
