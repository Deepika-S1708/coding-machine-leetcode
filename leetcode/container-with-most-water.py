
from typing import List

class Solution:
    def cw(self,height: List[int])->int:
        l=0
        r=len(height)-1
        area=0
        while(height[l]<height[r]):
            dis= r-l
            min_height=min(height[l],height[r])
            max_area=dis*min_height
            max_area=max(area,max_area)
            if height[l]<height[r]:

                l=l+1
            else:
                r=r-1
        return max_area

if __name__== "__main__":
    s=Solution()
    height=[1,8,6,2,5,4,8,3,7]
    res=s.cw(height)


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
#  In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1    






