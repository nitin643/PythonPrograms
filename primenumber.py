n=int(input("enter the number that you want to check that it is prime or not:"))
count=0
i=1
while(i<=n):
    if(n%i==0):
        count=count+1
    i=i+1
if(count==2):
    print("primr number")
else:
    print("composite number ")    
