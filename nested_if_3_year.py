#write a program to findout that user given year lipe year or not
year=int(input("enter the year"))
day=365
if year%4==0 and year%100!=0 and year%400!=0 and day+1 or year%4==0 and year%400==0:
    print(f"this year is the leap year and it has {day+1} days")
else:
    print(f"this is not the leap year and it has {day} days")
        