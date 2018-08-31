cat_name = []

while True:
	print("猫" + str(len(cat_name) + 1) + "名前を入力してください" + "終了する時はenterキーを押してください")
	
	name = input()
	if name == '':
		break
	cat_name = cat_name + [name]

print("猫の名は次の通り：")
for name in cat_name:
	print(" " + name)
	
