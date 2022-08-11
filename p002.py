val1=str();
val2=str();
val3=str();
def calc(y,c,z):
    if c=="*":
        return(y*z)
    else:
        if c=="/":
            return(y/z)
        else:
            if c=="+":
                return(y+z)
            else:
                if c=="-":
                    return(y-z)
                else:
                    return(0)
def spliter(formu):
    L=len(formu)
    if formula.find('*')>1:
        k=formula.find('*')
    else:
        if formu.find('/')>1:
            k=formu.find('/')
        else:
            if formu.find('+')>1:
                k=formu.find('+')
            else:
                if formu.find('-')>1:
                            k=formu.find('-')
    val1=formu[0:k]
    val2=formu[k]
    val3=formu[k+1:L]
    return(float(val1),str(val2),float(val3))
formula=str(input("Enter your task(Like 22*33 Or 45/12 Or 33-22 Or 79+45):"))
y,c,z=spliter(formula)
print("Result is ",calc(y,c,z))
