num = int(input("Enter a number to find Factorial : "))
fact=int(1)
for i in range(1,num+1):
    fact*=i

print(f"The factorial of {num} is {fact}")