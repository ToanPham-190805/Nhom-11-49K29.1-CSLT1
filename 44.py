month=input('Month: ')
day =int(input('Day: '))
holiday=''
if month=='January' and day==1 :
    print('New years day')
elif month=='July' and day==1 :
    print('Canada day')
elif month=='December' and day==25 :
    print('Christmas day')
else:
    print('Month and day do not correspond to a fixed-date holiday.')