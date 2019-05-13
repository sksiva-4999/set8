str12=input()
if (len(str12)%2==0):
    n=len(str12)//2
    print(str12[:n-1]+'*'+'*'+str12[n+1:])
else:
    n=len(str12)//2
    print(str12[:n]+'*'+str12[n+1:])
