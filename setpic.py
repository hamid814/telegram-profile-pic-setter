from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
from telethon.tl.functions.account import UpdateProfileRequest
import time
from telethon.errors.rpcerrorlist import FloodWaitError
from decouple import config

client_name = 'hamid'
API_ID = config('API_ID')
API_HASH = config('API_HASH')

numberOfPics = 120

client = TelegramClient(client_name, API_ID, API_HASH)

client.start()

n = 1

# while n < numberOfPics:
#   pics = client.get_profile_photos('me')

#   p = pics[0]

#   client(DeletePhotosRequest(
#       id=[InputPhoto(
#           id=p.id,
#           access_hash=p.access_hash,
#           file_reference=p.file_reference
#       )]
#   ))

#   n += 1

# while numberOfPics >= 1:
#   try:
#     client(UploadProfilePhotoRequest(
#       client.upload_file(f'./pics/{numberOfPics}.png')
#     ))

#     time.sleep(1)
#     numberOfPics -= 1
#   except Exception as e:
#     if type(e) == FloodWaitError:
#       print(f'sleeping for {e.seconds} seconds')
#       time.sleep(e.seconds)


client(UploadProfilePhotoRequest(
  client.upload_file(f'./p.jpg')
))