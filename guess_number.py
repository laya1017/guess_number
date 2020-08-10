import random
start = int(input('請輸入猜測數字範圍的起始值： '))
end = int(input('請輸入猜測數字範圍的結束值： '))
r = random.randint(start,end)
count = 1
while True :
	count += 1
	num = input('請猜數字： ')
	num = int(num)
	if num == r:
		print('猜對囉！')
		print('這你猜的第', count,'次')
		break
	elif num > r:
		print('猜錯了！你猜的比答案大')
	elif num < r:
		print('猜錯了！你猜的比答案小')
	print('這你猜的第', count,'次')
