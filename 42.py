tanso=float(input("Nhap tan so:"))
if tanso-1<=261.63<=tanso+1:
    print("Note C4")
elif tanso-1<=293.66<=tanso+1:
    print("Note D4")
elif tanso-1<=329.63<=tanso+1:
    print("Note E4")
elif tanso-1<=349.23<=tanso+1:
    print("Note F4")
elif tanso-1<=392.00<=tanso+1:
    print("Note G4")
elif tanso-1<=440.00<=tanso+1:
    print("Note A4")
elif tanso-1<=493.88<=tanso+1:
    print("Note B4")
else:
    print("Tần số không tương ứng với nốt nhạc nào")