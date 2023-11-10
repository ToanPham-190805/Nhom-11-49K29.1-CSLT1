decibels = float(input("Enter the number of decibels: "))
	
if decibels > 0 and decibels < 40:
    print('Quieter than a quiet room.')
		
elif decibels == 40:
    print('Quiet room.')
	
elif decibels > 40 and decibels < 70:
    print('Between Quiet room and Alarm clock')
elif decibels == 70:
    print('Alarm clock')
		
elif decibels > 70 and decibels < 106:
    print('Between Alarm clock and Gas lawnmower')
	
elif decibels == 106:
    print('Gas lawnmower')
	
elif decibels > 106 and decibels < 130:
    print(" Between Gas lawnmower and Jackhammer")
		
elif decibels == 130:
    print('Jackhammer')
		
elif decibels > 130:
    print('Louder than Jackhammer')
		
else:
    print('You entered a correct data value.')
		
  
