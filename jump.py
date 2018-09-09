def canJump( nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    index = 0
    
    while(index< len(nums)):
        if(index +nums[index] >= len(nums)):
            return True
        if(nums[index] == 0):
            return False
        if( index + nums[index] < len(nums) and nums[index + nums[index]] != 0):
            index = index + nums[index]
        else:
            between = 1
            while(between < nums[index]):
                if(index + between < len(nums) and nums[index + between] == 0):
                    between+=1
                else:
                    break
            if(between == nums[index]):
                return False
            index = index + between
    return True

print(canJump([0,1]))