print('1 задание')
x = 2**3
y = 3**2
if(x>y):
	print(x)
elif(x<y):
	print(y)
else:
	print ('x==y')

print('2 задание')
x = int(input('Введите число: '))
y = int(input('Введите число: '))
z = int(input('Введите число: '))
print('Самое большое число')
if x>y :
	print(x) if x>z else print(z)
else:
	print(y) if y>z else print(z)
print('Самое маленькое число')
if x<y:
	print(x) if x<z else print(z)
else:
	print(y) if y<z else print(z)



print('3 задание')
x = 17391%17
y = 546%17
z = 934%17
if x>y:
	print(x) if x>z else print(z)
else:
	print(y) if y>z else print(z)





print('4 задание')
x = 13**2
y = x**2
if x<172:
	print(172)  if x>172 else print(y)




print('5 задание')
x = int(input('Введите число: '))
if x % 2 == 0:
	print('Четное число')
else:
	print('Нечетное число')
if x % 3 == 0:
	print('Делится без остатка')
else:
	print('Не делится без остатка')
if x ** 2 > 1000:
	print('Больше 1000')
else:
	print('Меньше 1000')
