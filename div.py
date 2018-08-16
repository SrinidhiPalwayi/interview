from math import log,ceil,pow, floor
import sys
def answer(n):
    n = long(n)
    count = 0
    while(n>1):
        power2 = log(n,2)
        if(power2 == int(power2)):
            return int(count + power2)
        else:
            count+=1
            if(n%2 == 0):
                n = n/2
            elif(n!= 3 and n%4 == 3):
                print("came in ")
                n = n+1
            else:
                n = n +1

"""
def min_num_steps(n, cur_min, cur_num_step):
    higher = int(ceil(log(n,2)))
    add_count = ((1<<higher) - n)
    if(cur_num_step> cur_min):
        return cur_min
    if(n == 1 or add_count == 0):
        return cur_min
    add_count+=higher
    lower = int(floor(log(n,2)))
    sub_count = (n - (1<<lower)) + lower
    cur_min = min(add_count + cur_num_step, sub_count + cur_num_step, cur_min)
    cur_num_step+=1
    if(n%2 == 0):
        return min_num_steps(n/2, cur_min, cur_num_step)
    elif(add_count>= sub_count):
        return min_num_steps(n-1, cur_min, cur_num_step)
    else:
        return min_num_steps(n+1, cur_min, cur_num_step)
    """
print(answer(15))