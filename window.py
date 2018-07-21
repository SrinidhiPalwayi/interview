class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        dictS = dict()
        for c in t:
            if c in dictS:
                dictS[c] += 1
            else:
                dictS[c] = 1
        
        new_dict = dict.fromkeys(dictS.keys(),0)        
        best_left = 0
        best_right = sys.maxint
        
        
        left = 0
        right = 0
        old_list = list(dictS.values())
        first = True
        
        firstLeft = 0
        length = len(list(dictS.keys()))
        for a in s:            
            print a 
            if a in new_dict:
                if first:
                    first = False
                    left = firstLeft
                new_dict[a] += 1
                new_list = list(new_dict.values())
                true_list = [True for new, old in zip(new_list, old_list) if new >= old]                
                if(len(true_list) == length or new_dict[a] > dictS[s[left]]):
                    c = s[left]
                    if c in new_dict:
                        new_dict[c] -= 1                         
                    count = 0;
                    newL = False
                    while (left + count < len(s) - 1) and not newL:
                        count = count + 1
                        c = s[left + count]
                        if c in new_dict:
                            newL = True                                       
                    if (len(true_list) == length and (right- left) < (best_right - best_left)):
                        best_right = right
                        best_left = left
                    left += count
            right +=1
            firstLeft += 1
            print left , right, "left right"
        
        while(left <= right - len(t)):
            if s[left] in new_dict:      
                print "came in "
                true_list = [True for new, old in zip(new_dict.values(), old_list) if new >= old]
                print true_list
                if (len(true_list) != length):
                    break
                if(right-left < best_right - best_left):
                    best_right = right
                    best_left = left   
                    print new_list
                    print old_list, "old "
                new_dict[s[left]] -= 1
            left = left + 1
        
        if best_right == sys.maxint:
            return ""
        else:
            return s[best_left:best_right +1]
                
            
        