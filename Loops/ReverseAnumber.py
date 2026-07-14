num = int(input("Enter a Number to reverse it :"))

r=int(0)
n=int(num)
rev=int(0)

while n>0 :
    r=n%10
    n=n//10
    rev=rev*10+r

print(f"The reverse of {num} is {rev}")