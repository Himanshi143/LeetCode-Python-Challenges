#Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        a=[str(i) for i in nums]
        for i in range(len(a)):
            for j in range(i+1,len(a)):
                if(int(a[j]+a[i])>int(a[i]+a[j])):
                    temp=a[i]
                    a[i]=a[j]
                    a[j]=temp
                else:
                    continue
        print(a)  
        f=int("".join(a))
        return str(f)     