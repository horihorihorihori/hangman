import os

total = 0

for filename in os.listdir('/home/user01/hangman'):
	total += os.path.getsize(os.path.join('/home/user01/hangman',filename))

print(total)
