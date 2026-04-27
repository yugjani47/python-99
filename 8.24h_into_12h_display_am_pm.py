hours=float(input("enter hours in limit of 24 ="))

if hours>24:
    print("hours are not limited")

hours=hours-12
if hours<0:
    print(f"hours are nagativ so convert in positiv and convert into 12 hours format={-hours} a.m.")
else:
 print(f"hours are positiv so convert into 12 hours format={hours} p.m.")    
#-3-12 so hours<12 so hours are in a.m. otherwise (17-12 hours>12) in p.m.
