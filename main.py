n=list(map(int,input().split()))
ct=0
for i in range(len(n)):
    l=1
    h=int(pow(n[i],1/3))
    while (l<=h):
        c=(l**3)+(h**3)
        if c==n[i]:
            ct+=1
            break
        elif c<n[i]:
            l+=1
        else:
            h-=1
print(ct)


    

