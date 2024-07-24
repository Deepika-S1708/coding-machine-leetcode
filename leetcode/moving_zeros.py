nums= [1,2,3,0,4]
a=0
for i in range(len(nums)):
    if nums[i]!=0:

        temp=nums[i]
        nums[i]=nums[a]
        nums[a]=temp 
        a+=1
        # nums[i],nums[a]=nums[a],nums[i]
print(nums)


