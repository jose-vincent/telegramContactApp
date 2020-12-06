import os
from telethon import TelegramClient
import time
from environs import Env

env = Env()
env.read_env()

# Remember to use your own values from my.telegram.org!
api_id = env.int("API_ID")
api_hash = env("API_HASH")
sleepTime = 5



# api_id = 2068371
# api_hash = 'deb6a6be219f67f3e3d082b014d1503b'
client = TelegramClient('send_msg', api_id, api_hash)

ids =[676464356,1469940265,663339140,607827978,603546190]
# ids = [410625567]
user_names = ['gokul_ravi',
			'Shazam199991',
			'prodigalS0N',
			]

file_location = (os.getcwd()) + '/sample.pdf'
async def send_message():
    await client.send_message(id, 'Test msg')
    await client.send_file(id, file_location)
    time.sleep(sleepTime)

# entity = []
# async def get_entity():
#     contact = await client.get_entity(id)
#     entity.append(contact)

with client:
    for id in user_names:
        try:
            client.loop.run_until_complete(send_message())
        except Exception as e:
            print(f"Message not sent to {id}")
            print(e)


# for id in ids:
#     with client:
#         try:
#             client.loop.run_until_complete(get_entity())
#         except Exception as e:
#             print(e)  

# print(entity)
print('Done !')