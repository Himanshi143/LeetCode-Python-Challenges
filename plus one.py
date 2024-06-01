#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        z=[]
        for i in digits[0:]:
            z.extend(str(i))
        a="".join(z)
        print(type(a))
        b=str(int(a)+1)
        p=[]
        for j in b[0:]:
            p.append(int(j))
        return p
obj=Solution()
sol=obj.plusOne(digits=[9])
print("List is: ",sol)