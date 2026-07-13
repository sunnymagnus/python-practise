num = int(input("Enter a number to count digits :"))
n=int(num)
count=int(0)
while n>0 :
    n=n//10
    count+=1

print(f"the number of digits in {num} are {count}")