#write a program to convert 24 hours time formet into 12 hours time formet and display with am or pm
time=int(input("enter hours"))
if time<0 or time>24:
    print("time is invalid")
else:
    if time>12:
        time=time-12
        print(f"{time}pm")
    else:
        if time<12:
            print(f"{time}am")
