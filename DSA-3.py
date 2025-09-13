# DSA-3

list1 = list(range(1, 1000))
n = len(list1)
s = int(input("Enter the number to search: "))
found = False

for i in range(n):
    if list1[i] == s:
        print(f"The element is found at index {i}")
        found = True
        break  

if not found:
    print("Element not found in the list.")
