from string import ascii_lowercase
mapping = list()
def numDecodings( s):
        if (len(s) == 0):
            return 0
        index = 0
        count = 0
        while(index < len(s)):
            if(s[index] == '0'):
                return 0
            elif(s[index] == '1'):
                if(index == len(s) -1 or s[index +1] == '0'):
                    index +=1
                elif(index <= len(s) - 3 and (s[index:index+3] == '110' or s[index:index+3] == '120')):
                    index +=2
                else:
                    print("in the one")
                    count +=1
            elif(s[index] == '2'):
                if(index == len(s) -1 or s[index +1] == '0'):
                    index+=1
                elif(s[index+1]!='7' and s[index+1]!='8'and s[index+1]!='9'):
                    print("came in ")
                    count +=1
            index +=1
        count+=1
        return count


print(numDecodings("1212"))