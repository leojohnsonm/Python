import re
a = "044-2251529044-17412580444-369258"
x = re.findall("[0]+\d{3}-\d{6}|[0]+\d{2}-\d{7}",a)
print(x)
exit()


import re
b = "7708955853979019749999443379779442273729"
y = re.findall("[6-9]\d{9}",b)
print(y)
exit()


import re
b = "044-1472589044-3692581"
y = re.findall("[044]+-\d{7}",b)
print(y)
exit()
