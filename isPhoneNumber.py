import re

def is_phone_number(text):
 if len(text) != 12:
  return False

 for i in range(0,3):
  if not text[i].isdecimal():
   return False
  
 if text[3] != '-':
  return False

 for i in range(4,7):
  if not text[i].isdecimal():
   return False

 if text[7] != '-':
  return False

 for i in range(8,12):
  if not text[i].isdecimal():
   return False

 return True  
#print('415-555-4242は電話番号')
#print(is_phone_number('415-555-4242'))
#print('Moshi moshiは電話番号')
#print(is_phone_number('Moshi moshi'))

message = "123-456-7891 199-999-9999です。"

for i in range(len(message)):
  chunk = message[i:i+12]
  phone_number_regex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
  mo = phone_number_regex.search(chunk)
  if mo:
   print(mo.groups())



