hiii=int(raw_input())
abhi=[]
for i in range(1, hiii + 1):
       if hiii % i == 0:
           abhi.append(i)
print(" ".join(str(n) for n in abhi))
