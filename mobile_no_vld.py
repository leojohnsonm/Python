import re
a = input("enter the 10 digit mobile no: ")
x = re.findall("\d{10}", a)
print(f"the entered no {x} is right")

