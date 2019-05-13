import math
s,m=map(int,input().split())
l=math.sqrt(s*m)
if (l-int(l)==0.0):
    print("yes")
else:
    print("no")  
