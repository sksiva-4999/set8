s=int(input())
sum1=0
for i in range(2,s//2):
    if s%i==0:
        sum1=sum1+1
if(sum1>0):
    print("yes")
else:
    print("no")
