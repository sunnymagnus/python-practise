side1,side2,side3 = map(float,input("Enter three sides:").split())

if side1+side2>side3 or side1+side3>side2 or side2+side3>side1 :
    print("The above lenths are allowed to be a triangle!")
else :
    print("The above lenghts cant be a triangle!")