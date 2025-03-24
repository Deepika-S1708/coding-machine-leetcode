from typing import List
class Binarysearch:
    def binary_search(self, nums:List[int], target:int)->int:
            left=0
            right=len(nums)-1
            while left<=right:
                mid=(left+right)//2
                if nums[mid]==target:
                     return mid             
                elif target>nums[mid]:        
                     left=mid+1
                elif target<nums[mid]:
                     right=mid-1
            return -1
                                         
if __name__=="__main__":
    
    s= Binarysearch()
    nums= [2,3,4,0,7,8]
    nums.sort()
    target= 8
    res= s.binary_search(nums, target)   
    print(res) 
    
                 


                
                
                
            

       

