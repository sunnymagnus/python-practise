# programs on variable creation and initialization 

"""
in python we don't declare the type.
we just assign the value and the python itself adjusts the datatype 
we can see that in below examples...

-----Index-----

1. Basic Variable Creation
2. Changing Variable Value
3. Changing Variable Data Type
4. Dynamic Typing
5. Multiple Variable Assignment
6. One Value to Multiple Variables
7. Swapping Variables
8. Swapping Using Temporary Variable
9. Swapping String Variables
10. Printing Multiple Variables
11. Printing Variables with Text
12. Using f-Strings
13. Checking Data Type (`type()`)
14. Boolean Data Type
15. Type Conversion (`int()`, `float()`, `str()`)

"""
# 1. basic intialization of variable
age = 20
print(age)
# 2. here we initialize the same variable with a name 
age = "adarsh"
print(age)
# 3. we change it 
age= 20.5
print(age)

# 4. we can change the variable value and datatype any time in python.
age=12
print(age)
age="hello"
print(age)
age= 12.5
print(age)

# 5. in the below code we will see multiple assignment

name , age , city = "sunny","19","hyderabad"

print(name)
print(age)
print(city)

# 6. assign one value to multiple variables

a=b=c=100

print(a)
print(b)
print(c)

# 7. in c we use call by reference method to swap values here we can swap easily

a,b=12,20
print( a )
print(b )

a,b=b,a

print( a )
print( b )

# 8. using temp
a = 10
b = 20
temp = a
a = b
b = temp
print(a)
print(b)

# 9. for strings
n1 = "Ram"
n2 = "Shyam"

n1, n2 = n2, n1

print(n1)
print(n2)

# 10. print variables together 

name = "Sunny"
age = 19
print(name, age)

# 11. printing variables with text

name = "Sunny"
print("Name is", name)

# 12. using f-string method
phone = "17 pro"
cost = 65000
print(f"The {phone} costs {cost} rupees.")

# 13. displaying datatype 
name = "Sunny"
print(type(name))

# 14. boolean datatype
result = True
print(type(result))

# 15. type conversion => converting 1 datatype to another datatype

a=10
b= float(a)

print(f"the dataype is {type(b)} and the value is {b}")

