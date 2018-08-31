#! python3
# pw.py - パスワード管理プログラム


PASSWORD = {'n-horiuchi@za.biglobe.co.jp':'201807Horiuchi',
            'bazar80':'Noahito_201807',
            '26293':'201807Horiuchi'}
			
import sys
import pyperclip

if len(sys.argv) < 2:
	print('使い方: python pw.py[アカウント名]')
	print('パスワードをクリップボードにコピーします')
	sys.exit()

account = sys.argv[1]

if account in PASSWORD:
	pyperclip.copy(PASSWORD[account])
	print(account + 'のパスワードをクリップボードにコピーしました')
else:
	print(account + 'というアカウント名はありません')
	


