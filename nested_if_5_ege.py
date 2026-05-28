#write a program to find out most young person by user given 4 person's age
age1=int(input("enter the age of first person"))
age2=int(input("enter the age of second person"))
age3=int(input("enter the age of third person"))
age4=int(input("enter the age of fourth person"))

if age1<age2 and age1<age3 and age1<age4:
    print(f"the yougest person is {age1} year old")
else:
    if age2<age1 and age2<age3 and age2<age4:
        print(f"the yougest person is {age2} year old")
    else:
        if age3<age2 and age3<age1 and age3<age4:
            print(f"the yougest person is {age3} year old")
        else:
            print(f"the yougest person is {age4} year old")
