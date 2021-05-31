import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1
	n = input('請猜數字: ')
	n = int(n)
	if n == r:
		print('恭喜答對')
		break
	elif n < r:
		print('比', n, '大')
	elif n > r:
		print('比', n, '小')
	else:
		print('請輸入數字')
	print('這是你猜的第', count, '次')