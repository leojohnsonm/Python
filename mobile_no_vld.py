import re
a = input("enter the 10 digit mobile no: ")
x = re.findall("[0]*[91]\d{11}|[6-9]\d{10}", a)
print(f"the entered no {x} is right")
