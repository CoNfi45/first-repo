import telebot
from config import BOT_TOKEN
from os import listdir
from random import choice
import requests

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    text = (
       f'привет, {message.from_user.first_name}! я бот, который по команде отправляет мемы по команде!\n\n' 
       'отправь команду /mem, чтобы получить мемасик'

    )

    bot.send_message(chat_id, text)    

@bot.message_handler(commands=['mem'])
def send_mem(message):
    random_mem = choice(listdir('фоточки'))
    with open(f'фоточки/{random_mem}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

    def get_duck_image_url():    
        url = 'https://random-d.uk/api/random'
        res = requests.get(url)
        data = res.json()
        return data['url']
    
    
    @bot.message_handler(commands=['duck'])
    def duck(message):
        '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)

    
bot.infinity_polling()