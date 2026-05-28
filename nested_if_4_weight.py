#write a program to find out highest wight by user given 3 person's weight
w1=int(input("enter the weight of first person"))
w2=int(input("enter the weight of second person"))
w3=int(input("enter the weight of third person"))

if w1>w2 and w1>w3:
    print(f"the highest weight is {w1}")
else:
    if w2>w1 and w2>w3:
        print(f"the highest weight is {w2}")
    else:
        print(f"the highest weight is {w3}")
