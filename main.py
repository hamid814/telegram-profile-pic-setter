from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
import time
import random
from decouple import config

sleep_time = 15 * 60

client_name = 'hamid'
API_ID = config('API_ID')
API_HASH = config('API_HASH')

client = TelegramClient(client_name, API_ID, API_HASH)

client.start()

prevNum = 0

while True:
  # clear current photo
  pics = client.get_profile_photos('me')

  if len(pics) != 0:
    pic = pics[0]
    
    client(DeletePhotosRequest(
      id=[InputPhoto(
        id = pic.id,
        access_hash = pic.access_hash,
        file_reference = pic.file_reference
      )]
    ))

  
  # get new random number
  newNum = random.randrange(1,33)
  
  # prevent repetetive pics
  if newNum == prevNum:
    continue
  
  client(UploadProfilePhotoRequest(
    client.upload_file(f'./pics/{newNum}.jpg')
  ))

  prevNum = newNum
  time.sleep(sleep_time + random.random())