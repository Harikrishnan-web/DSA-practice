def min(a):
    mini=float("inf")
    for num in a:
        if num<mini:
            mini=num
    return mini
def max(a):
    maxi=float("-inf")
    for num in a:
        if num>maxi:
            maxi=num
    return maxi
n=int(input("Enter the length of array: "))
nrr=[]
for x in range(n+1):
    nrr.append(int(input("Enter the elements: ")))
    
print(f"The min and max of the array{nrr} is {min(nrr)} and {max(nrr)}")
