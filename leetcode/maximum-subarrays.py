from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        m=nums[0]
        c=0
        for i in nums:
            if c<0:
                c=0
            c=c+i
            if c>m:
                m=c
        return m          
if __name__== "__main__":
    s=Solution()
    nums=[-2,1,-3,4,-1,2,1,-5,4]
    res=s.maxSubArray(nums)
    print(res)




#Tracing 3rd one:
m=5,9,15,23
c=9,8,15,23

# #output:
# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
