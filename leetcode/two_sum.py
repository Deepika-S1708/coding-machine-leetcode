from typing import List
class Solution:
    def twosum( self, nums:List[int], target:int)->List[int]:
        d={}
        for i in range(0, len(nums)):
            value=nums[i]
            difference= target-value
            if value not in d:
                d[difference]=i
            else:
                cur_idx=i
                prev_idx=d[value]
                return [cur_idx, prev_idx]   

if __name__ =="__main__":
    s=Solution()
    nums=[1, 2, 3, 4]
    target= 6
    res=s.twosum(nums,target)
    print(res)




                 

            


        