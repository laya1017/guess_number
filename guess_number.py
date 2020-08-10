import random
r = random.randint(1,100)
while True :
	num = input('請猜數字： ')
	num = int(num)
	if num == r:
		print('猜對囉！')
		break
	elif num > r:
		print('猜錯了！你猜的比答案大')
	elif num < r:
		print('猜錯了！你猜的比答案小')