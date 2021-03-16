def power (x:float,i:float):
    if i == 0:
        return 1
    else:
        answer=x
        for t in range (1,i):
            answer=answer*x
    return answer
def factor (i:float):
    if i<1:
        return 1
    else:
        answer=i
        for x in range(1,i):
            answer*=x
    return answer

                    
def exponent (x:float):
    answer =1
    for i in range(1,100):
        answer+=(power(x,i)/factor(i))
    return answer

def absulu(x:float):
    if x>0:
        return x
    else:
        return x*-1
    
def odds (x:float):
    if x%2 != 0:
        return True
    else:
        return False
    
def ln(x:float):
    if x<=0:
        return 0.0
    answer =x-1.0
    temp =0
    while absulu(temp-answer)>0.001:
        temp=answer
        answer=answer+2*((x-exponent(answer))/(x+exponent(answer)))
    return answer
def XtimesY (x:float,y:float):
    if x<0:
        return 0.0
        
    if y==0:
        return 1.0
    elif y==1:
        return float(x)
    else:
        answer =exponent(y*ln(x))
        return answer

def sqrt (x:float,y:float):
    if y==0:
        return 0.0
    if y<0 and odds(x):
        answer=XtimesY(-y, 1/x)
        return answer*-1
    answer=XtimesY(y, 1/x)
    return answer


def calculate(x:float):
    answer=exponent(x)*XtimesY(7, x)*XtimesY(x, -1)*sqrt(x,x)
    return float('%0.6f' % answer)


