#DSA-1
#To find maximum number in the array
n=int(input("Enter the size of array: "))
a=[]
for i in range(n):
    n1=int(input(f"Enter the element {i+1}: "))
    a.append(n1)

#to find maximum
s=int(input("Enter the element to search: "))
for j in range(n):
    if a[j]==s:
        print(f"The element is found at {j}")
    elif a[j]!=s:
        continue
    else:
        print("The element is not found")
    
