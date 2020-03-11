import re  #starts with zero then the first digit must start with 6-9                     
a = "0979019749917708955853919944337977"
x = re.findall("^0+[6-9]\d{9}|[6-9]\d{9}",a)
print(x)


import re #starts with 91 then the first digit must start with 6-9
a = "919790197499 917708955853 917239234673 919442273729 919659952774"
x = re.findall("[91]([6-9]\d{9})",a)
print(x)
