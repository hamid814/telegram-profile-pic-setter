from telethon.sync import TelegramClient
from telethon.tl.functions.photos import UploadProfilePhotoRequest, DeletePhotosRequest
from telethon.tl.types import InputPhoto
from telethon.tl.functions.account import UpdateProfileRequest
import time
from decouple import config

client_name = 'hamid'
API_ID = config('API_ID')
API_HASH = config('API_HASH')

client = TelegramClient(client_name, API_ID, API_HASH)

client.start()

n = 0

':::::::::::::::::::'
'::::____::::___::::'
':::/::::\::/:::\:::'
'::|::::::\/:::::|::'
':::\:::::::::::/:::'
'::::\:::::::::/::::'
':::::\:::::::/:::::'
'::::::\:::::/::::::'
':::::::\:::/:::::::'
'::::::::\_/::::::::'
':::::::::::::::::::'

msgs = [
  'hello',
  'i want',
  'to tell u',
  'i can do this'
]

dest = 'me'
message = client.send_message(dest, 'hello')


# repeat_to_length
# def r(string_to_expand, length):
#   return (string_to_expand * (int(length/len(string_to_expand))+1))[:length]

# message = None

n = 1

# 🔵🔴
# 🔴🔵

# 😐😶

# 😮😮😲😲

# 🔒🔓

# 🤬😡

# 🥱😴

# 😀😃

# 🤢🤢🤮🤮

# 😓😓😥😥

# 🥰🥰😘😘

# 😊😊☺️☺️

# 😗😗😙😙

# 😦😧😯😮😲😵





el = [
  '🕐','🕑','🕒','🕓','🕔','🕕','🕖','🕗','🕘','🕙','🕚','🕛'
]

el = [
  '0⃣','1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟'
]

el = [
  '🌇','🌆','🏙','🌃'
]

el = [
  '🛫🛬🛫🛬🛫🛬','🛬🛫🛬🛫🛬🛫'
]

el = [
  '🏀','🎾','⚽️','🏐','🎱','🥎','⚾️'
]

el = [
  '😶😶😶😶😶',
  '😐😐😐😐😐',
  '😑😑😑😑😑',
  '😐😐😐😐😐',
]

el = [
  '😐😐😐😐😐',
  '😑😑😑😑😑',
]

# el = [
#   '😂😂',
#   '🤣🤣'
# ]

# el = [
#   '🖕🏻',
#   '🖕🏼',
#   '🖕🏽',
#   '🖕🏾',
#   '🖕🏿',
#   '🖕🏾',
#   '🖕🏽',
#   '🖕🏼',
# ]

# el = [
#   '💀💀','☠️☠️'
# ]

# el = [
#   '🔴🔵',
#   '🔵🔴',
# ]


el = [
  '🔴🔵🔵🔵🔵🔵🔵🔵🔵',
  '🔵🔴🔵🔵🔵🔵🔵🔵🔵',
  '🔵🔵🔴🔵🔵🔵🔵🔵🔵',
  '🔵🔵🔵🔴🔵🔵🔵🔵🔵',
  '🔵🔵🔵🔵🔴🔵🔵🔵🔵',
  '🔵🔵🔵🔵🔵🔴🔵🔵🔵',
  '🔵🔵🔵🔵🔵🔵🔴🔵🔵',
  '🔵🔵🔵🔵🔵🔵🔵🔴🔵',
  '🔵🔵🔵🔵🔵🔵🔵🔵🔴',
]

el = [
  '😐😐😐😐😐',
  '😑😑😑😑😑',
]

# el = [
#   '😦😦',
#   '😧😧',
#   '😯😯',
#   '😮😮',
#   '😲😲',
#   '😵😵',
#   '😲😲',
#   '😮😮',
#   '😯😯',
#   '😧😧',
# ]

n = 0

while True:
  if n == len(el):
    n = 0
    client.edit_message(message, el[n])
    n += 1
  else:
    client.edit_message(message, el[n])
    n += 1
    
  time.sleep(0.9)

# for line in msgs:
#   end = len(line)
#   current = 0
#   for n in range(end):
#     n = n+1
#     if n == 1:
#       message = client.send_message(dest, line[0])
#     else:
#       try:
#         client.edit_message(message, line[0:n])
#       except Exception as e:
#         print(e)

#     time.sleep(1)

# n = 1
# while True:
#   if n == 11:
#     n = 1
#     text = 'finish'
#     pass
#   else:
#     firstPart = r('-', n-1)
#     lastPart = r('-', 10-n)

#     text = firstPart + '|' + lastPart
#     n += 1
  
#   client.edit_message(message, text)
#   time.sleep(1)
