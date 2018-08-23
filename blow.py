from math import floor
def answer(M, F):
    m = long(M)
    f = long(F)
    count = 0
    while((m > 1  or f > 1) and (m!= 0 and f != 0) and m!=f):
        if(f==1):
            count += m -1
            m =1
        elif(m ==1):
            count+= f-1
            f =1
        elif(f-m > 0):
            count+= f/m
            f = f- (m * (f/m))
        else:
            count += m/f
            m = m - (f *(m/f))
    if(m == 1 and f == 1):
        return count
    else:
        return "impossible"

print(answer(4,7))