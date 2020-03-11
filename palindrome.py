a = str(input("enter the string: "))
rev = ''
for i in a:
    rev = i + rev
if a == rev:
    print(f"the given string {a} is palindrome")
else:
    print(f"the given string {a} is not a palindrome")



