def prim(n):
    flg=0
    for i in range(2,int(n/2)+1):
        if n%i==0:
            flg=1
            return(0)
    if flg==0:
        return(n)
n=int(input("Enter a Number:"))
x=4
np=6
while x<=n:
    if(prim(x)!=0):
        np*=prim(x)
    x+=1
print("N-p=",np)

