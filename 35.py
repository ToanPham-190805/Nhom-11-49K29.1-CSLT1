humage = int(input('Input a dog age in human years: '))

if humage < 0:
	print('Age must be positive number')
	
elif humage <= 2:
	doage = humage * 10.5
else:
	doage = 21 + (humage - 2)*4

print('The dog age is', doage)