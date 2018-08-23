from math import log
def answer(n):
    count = 0#number of operations
    while n != '1':
        count+=1
        if(int(n[-1])%2 == 0):
            n = division(n)
        else:
            n = subtract(n)
    return count
                
def division(n):   
    answer = ""
    index = 0
    sub_number = 0
    
    while(index< len(n)):
        sub_number = (sub_number%2)*10 + int(n[index])
        answer+= str(sub_number/2)
        index+=1
    return answer.lstrip('0')

def subtract(n):
    if(int(n[-1]) == 0):   
        for index, dig in enumerate(n[::-1]):
            if(dig!='0'):
                return (n[:-index -1]+str(int(dig)-1) + ('9'* (index))).lstrip('0')
    else:
        last_dig = int(n[-1]) - 1
        return n[:-1] + str(last_dig)

def add(n):
    if(int(n[-1]) == 9):
        for index, dig in enumerate(n[::-1]):
            if(dig!='9'):
                return (n[:-index-1]+str(int(dig)+1) + ('0'* (index)))
        return (str(int(n[0])+1) + ('0'* (len(n) -1)))
    else:
        last_dig = int(n[-1]) + 1
        return n[:-1] + str(last_dig)

def is_power2(n):
    #checks if the number is a power of 2 by finding the binary value
    #and checking if there's only one of the number one
    binary = ''
    num_one = 0
    while(n != ''):
        if int(n[-1])%2 == 0:
            binary = '0' + binary
        else:
            num_one +=1
            binary = '1' + binary
        n = division(n)
    if num_one == 1:
        return True
    else:
        return False

from math import log
def answer(n):
    n = long(n)
    count =0
    while n!=1:
        count +=1
        if n%2 == 0:
            n = n/2
        else:
            if(((n-1)&(n-2))==0):
                n = (n-1)
            elif(((n+1)&(n)) == 0):
                n = n+1
            else:
                n = n-1
    return count
