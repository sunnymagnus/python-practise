num = int(input("Enter a number to Find its factors :"))

print("The Factors are :")
for i in range(1,num+1) :
    if num%i==0 :
        print(i,end=" ")
    
