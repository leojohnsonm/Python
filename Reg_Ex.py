import re
a = str(input("enter the 10 digit mob no: "))
x = re.findall("[0]*[91]*[6-9]\d{9}",a)
print(x)
