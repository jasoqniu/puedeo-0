n = int(input("Batas = "))
sum = 0
for x in range(1,n+1):
    sum = sum + x
    print(x,end="")
    if(x!=n):
        print("+",end="")
print("=",sum)
    
    