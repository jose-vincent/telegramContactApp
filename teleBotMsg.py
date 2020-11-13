# importing all required libraries 
import telebot 
from telethon.sync import TelegramClient 
from telethon.tl.types import InputPeerUser, InputPeerChannel 
from telethon import TelegramClient, sync, events 

# Remember to use your own values from my.telegram.org!
api_id = env.int("API_ID")
api_hash = env.str("API_HASH")
phone = env.str("PHONE_NUMBER")
token = env.str("TOKEN")

client = TelegramClient('session', api_id, api_hash) 

client.connect() 

message = "This is a test message"

if not client.is_user_authorized():
	client.send_code_request(phone) 
	client.sign_in(phone, input('Enter the code: ')) 


try: 
	receiver = InputPeerUser(user_id = '+607827978', access_hash)
	client.send_message(receiver, message, parse_mode='html')


except Exception as e:
	print(e); 


client.disconnect() 
print("Done")


# import requests
# token = '1469940265:AAF-I5Ky_oJkFug9F7MhXZMkpcvLPQ5qm-c'
# url = f'https://api.telegram.org/bot{token}/sendMessage'
# data = {'chat_id': 603546190, 'text': 'python msg'}
# requests.post(url, data).json()

# import telegram
# import sys
# import os

# CHAT_ID = 410625567
# def send_message():
#     bot = telegram.Bot(token=TOKEN)
#     bot.sendMessage(chat_id = CHAT_ID, text = 'Hey there!')

# send_message()    