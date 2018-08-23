def jumps(nums):
    jumps = 0
    index = 0
    while(index < len(nums) -1):
        val = nums[index]
        if(index + nums[index] > len(nums) - 1):
            return jumps+1
        max_val = 0
        next_index = index
        i = 1
        while(i <= val and (i + index < len(nums))):
            if(i+ nums[i+index] > max_val):
                max_val = i + nums[index+i]
                next_index = index+i
            i+=1
        index = next_index
        jumps+=1
    return jumps

print(jumps([3,2,1]))