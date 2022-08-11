x=int(input("Enter a Number:"))
y=x
fact=1
while y>1:
    fact=fact*y
    y-=1
print(x,"!=",fact)