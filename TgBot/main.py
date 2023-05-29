import telebot
import requests

TOKEN='6067999162:AAGl0AcjbV232zp9nZHp2wYwaUiZP1wz0a4'
bot=telebot.TeleBot(TOKEN)
values={
    'Евро':'EUR',
    'Доллар':'USD',
    'Рубль':'RUB'
}



@bot.message_handler(commands=['start','help'])
def start(message):
    text="Привет,это бот-конвертер валют. Чтобы начать работу введите команду в бот в следующем формате " \
         "\n<валюта> <валюта в которую хотите перевести> <количесто валюты>.\nЧтобы узнать доступные валюты нажмите /values"
    bot.send_message(message.chat.id,text)
@bot.message_handler(commands=['values'])
def help_value(message):
    text=''
    for i in values.values():
        text+=i+'\n'
    bot.send_message(message.chat.id,text)

@bot.message_handler(content_types=['text'])
def exchange(message):
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    qoute,base,amount=message.text.split(' ')
    bot.send_message(message.chat.id, int(amount)*data['Valute'][qoute]['Value']/data['Valute'][base]['Value'])

bot.polling(none_stop=True)
