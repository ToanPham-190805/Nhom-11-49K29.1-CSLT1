note = input("Nhập tên nốt: ") 
chu=note[0]  
so=int(note[1])
if chu=="C":
  tanso=261.63
elif chu=="D":
  tanso=293.66
elif chu=="E":
  tanso=329.63
elif chu=="F":
  tanso=349.23
elif chu=="G":
  tanso=392.00
elif chu=="A":
  tanso=440.00
elif chu=="B":
  tanso=493.88
tanso=tanso/(2**(4 - so))
print(note,"có tần số là:",tanso)