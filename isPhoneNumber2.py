import re

message = "123-456-7891 199-999-9999です。"

phone_number_regex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')
mo = phone_number_regex.search(message)
print(mo.groups())



