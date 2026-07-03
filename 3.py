"""
taking input from the user 

"""

# sample input program
name = input("enter name: ")
print(f"your name is {name}")

# read integers

number =int(input("enter a integer"))
print(f"number :{number}")


# collecting detailss of a stutendt 

print("-- enter student details--")
sname = input("enter name of the student :")
rnum  = int(input("enter mobile umber       :")) # mobile number can be a string 
fname = input("enter mothers name        :")
mname = input("enter your mother name    :")
cname = input("enter your college name   :")
mail = input("enter mail of the student  :")
print()
print("-------STUDENT DETAILS-------")
print(f"student name :{sname}")
print(f"roll number  :{rnum}")
print(f"father name  :{fname}")
print(f"mother name  :{mname}")
print(f"college name :{cname}")
print(f"mail id      :{mail}")


# reading floats 

wt = float(input("enter weight of sugar: "))
print(f"the price is {30 * wt}")

# taking multiple inputs and splitting 

a , b = map(int ,input("enter two numbers ").split())

print(a)
print(b)
