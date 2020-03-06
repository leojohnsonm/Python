import re
a = "johns@gmail.com7708955853leo@yahoo.com96599527749944337977leo@yahoo.com"
x = re.findall("[a-z]*\d+@gmail.com|[a-z]+@yahoo.com|[a-z]+@outlook.com|[a-z]+@hotmail.com|[6-9]\d{9}",a)
print(x)

