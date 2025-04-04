from typing import List
class Solutions:
    def subsets(self, nums):
        res= [[]]
        for i in nums:
            temp=[]
            for subset in res:
                out= subset + [i]
            temp.append(out)                           
            res=res+temp
        return res  
     
if __name__=="__main__":


    s=Solutions()
    nums=[1,2,3]
    res=s.subsets(nums)
    print(res)






        
        

