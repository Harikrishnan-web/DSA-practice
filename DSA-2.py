#DSA-2
#To check the input string is palindrome or not

def pali(i):
    return i == i[::-1]
i = input("Enter your string: ")
if (pali(i)==True):
    print(f"{i} is a palindrome")
else:
    print(f"{i[::-1]} is not a palindrome")

