import random
start = input('請決定隨機數字範圍的開始值: ')
end = input('請決定隨機數字範圍的結束值: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
while True:
	count += 1 # count = count + 1
	n = input('請猜數字: ')
	n = int(n)
	if n == r:
		print('恭喜答對! 你共猜了', count, '次')
		break
	elif n < r:
		print('比', n, '大')
	elif n > r:
		print('比', n, '小')
	else:
		print('請輸入數字')
	print('這是你猜的第', count, '次')