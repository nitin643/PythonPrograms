n=int(input("enter the number:"))
orig=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if(orig==sum):
    print("armstong number ")
else:
    print("not armstrong number ")    
