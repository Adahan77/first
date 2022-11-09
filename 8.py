name = input('Введите название марки: ')
year = int(input('Введите год выпуска: '))
mileage = int(input('Введите пробег авто: '))
color = input('Введите цвет авто: ')
rudder = int(input('Выберите руль 1 - Левый руль \t2 - Правый руль: '))
owner = int(input('Максимум владельцев: '))
price = int(input('Введите стоимость: '))
if name == 'toyota' or name == 'lexus':
	if year >= 2004:
		if mileage <= 200000:
			if color == 'white' or color == 'grey':
				if rudder == 1:
					if owner <= 2:
						if price <= 10000 :
							print('Мы нашли такую машину')
						else:
							print('Мы не нашли такую машину')
					else:
						print('Мы не нашли такую машину')
				else:
					print('Мы не нашли такую машину')
			else:
				print('Мы не нашли такую машину')
		else:
			print('Мы не нашли такую машину')
	else:
		print('Мы не нашли такую машину')
else:
	print('Мы не нашли такую машину')
