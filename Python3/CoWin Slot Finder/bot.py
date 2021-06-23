from main import SlotFinder
import requests
import telebot

API_KEY="1898794612:AAGFGfq805ICAZ7Nwr5H3omG9Vlk2oNFwME"

bot=telebot.TeleBot(API_KEY)
request_uri="https://api.telegram.org/bot"+API_KEY+"/getUpdates"
response_json=requests.get(url=request_uri)
print(response_json.json())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(commands=['status'])
def getStatus(message):
    s=SlotFinder()
    s.generateParams()
    message_string=f"Found {s.getFoundSession()} sessions!"
    if s.getFoundSession() > 0:
        message_string+=s.getFoundString()
    if s.getStatusCode()!=200:
        message_string+=f"\n{s.getStatusCode()} received!"
    bot.reply_to(message,message_string)

@bot.message_handler(commands=['all'])
def getStatusAll(message):
    s=SlotFinder()
    s.generateParams()
    message_string=f"Found {s.getFoundSession()} sessions!"
    message_string+=s.getLogString()
    if s.getStatusCode()!=200:
        message_string+=f"\n{s.getStatusCode()} received!"
    bot.reply_to(message,message_string)

bot.polling()
