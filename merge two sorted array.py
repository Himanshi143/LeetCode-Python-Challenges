#Given two sorted arrays, ‘a’ and ‘b’, of size ‘n’ and ‘m’, respectively, return the union of the arrays.

def sortedArray(a: [int], b: [int]) -> [int]:
    l=0
    r=0
    arr=[]
    while(l<len(a) and r<len(b)):
        if(a[l]<=b[r]):
            if(len(arr)==0 or a[l]!=arr[-1]):
                arr.append(a[l])
            l+=1
        else:
            if(len(arr)==0 or b[r]!=arr[-1]):
                arr.append(b[r])
            r+=1
    while(l<len(a)):
        if(a[l]!=arr[-1]):
            arr.append(a[l])
        l+=1
    while(r<len(b)):
        if(b[r]!=arr[-1]):
            arr.append(b[r])
        r+=1
    return arr
