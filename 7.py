language = input('Язык программорвания: ')
age = int(input('Возраст: '))
experience = int(input('Опыт работы: '))
pay = int(input('Желаемая зарплата: '))
if language=='python' or language=='java' or language=='javascript':
	if age>=18 and age<=65:
		if experience>=3:
			if pay<=60000:
				print('Вы подходите')
			else:
				print('Вы не подходите')
		else:
			print('Вы не подходите')			
	else:
		print('Вы не подходите')
else:
	print('Вы не подходите')
