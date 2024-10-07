#Lets add or multiply using list and dictionories 
class Solution():
    def __init__(self, list):
        self.arg1=list['a']
        self.arg2=list['b']
    def sum(self):
        sum=self.arg1+self.arg2 
        return sum
    def multiply(self):
        mul=self.arg1*self.arg2
        return mul
    def display(self):
        print(self.sum())
        print(self.mul())

listin={'a':[1,2,3] , 'b':[4,5,6]}
a1=listin['a']
b1=listin['b']
sum_n=[]
mul_n=[]
s1=Solution({'a':a1[0], 'b':b1[0]})
sum_n.append(s1.sum())
mul_n.append(s1.multiply())
for i in range(1,len(a1)):
    s1.arg1=a1[i]
    s1.arg2=b1[i]
    sum_n.append(s1.sum())
    mul_n.append(s1.multiply())
print(f"sum={sum_n},multiplication={mul_n}")





        