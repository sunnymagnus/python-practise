num = int(input("Enter for which number do you want to write multiplication table :"))

ran = int(input("Enter range :"))

for i in range(1,ran+1):
    print(f"{num} * {i} = {num*i}")
