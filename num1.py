n,n1=map(int,input().split())
l=list(map(int,input().split()))
for i in range(1,n+1):
    if i==n1:
        print(l[i-1])
