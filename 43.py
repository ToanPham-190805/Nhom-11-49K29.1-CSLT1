denomination=str(input("The denomination of the bank note is "))

individual="George Washington"


if denomination=="$1":
    individual="George Washington"
    print("The name on the note is ", individual)
elif denomination=='$2':
    individual="Thomas Jefferson"
    print("The name on the note is ", individual)
elif denomination=='$5':
    individual="Abraham Lincoln"
    print("The name on the note is ", individual)
elif denomination=='$10':
    individual="Alexander Hamilton"
    print("The name on the note is ", individual)
elif denomination=='$20':
    individual="Andrew Jackson"
    print("The name on the note is ", individual)
elif denomination=='$50':
    individual="Ulysses S. Grant"
    print("The name on the note is ", individual)
elif denomination=='$100':
    individual="Benjamin Franklin"
    print("The name on the note is ", individual)
else:
    print( " Such note does not exist")