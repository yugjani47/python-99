#write a program to display if bater's scored a 100 or above 100 runs tipe congratulation massage
runs=int(input("enter runs"))

if runs<0:
    print("runs are invalide")
else:
    if runs>=0 and runs<50:
        print("you must be inproving your batting")
    else:
        if runs>=50 and runs<100:
            print("congratulation you scored a half century")
        else:
            if runs>=100:
                print("congratulation you scored century")