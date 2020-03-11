import re
import os                 #file handling n data fetching
f = open("mail.txt","r")  #("file_name","mode")
pat = f.read()            #data's in file assigned to "pat"
x = re.findall("[a-z]+\w+@gmail.com|[a-z]+\w+@yahoo.com|[a-z]+\w+@hotmail.com|[a-z]+\w+@outlook.com",pat)
y = re.findall("[6-9]\d{9}",pat)
print(x)
print(y)

