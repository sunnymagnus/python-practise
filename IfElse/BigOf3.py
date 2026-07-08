a,b,c = map(int,input("enter three numbers").split())

if a>b:
    if a>c :
        print(f"{b} is big among three")
    else :
        print(f"{c} is big among three")
else :
    if b>c :
        print(f"{b} is big among three") 
    else :
        print(f"{c} is big among three")
