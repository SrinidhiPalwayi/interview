from math import log,ceil,pow
import sys
def answer(n):
    n = long(n)
    count =0
    cur_min = 10
  
    higher = ceil(log(n,2))
    add_count = ((1<<higher) - n) + higher
    lower = floor(log(n,2))
    sub_count = (n - (1<<lower)) + lower
    cur_min = min(add_count, sub_count, cur_min)
    return cur_min


print(answer('15'))