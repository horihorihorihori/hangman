cat_name = ["A","mely","io","mm","zz","bb"]
cat_name.insert(1,"queue")
cat_name.sort(key=str.lower)
name = ''

print("ペットの名前を入力してください")
name = input()

if name not in cat_name:
	print("含まれておりません")
else:
	print("飼っています ",cat_name)
