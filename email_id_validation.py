#this code fetches the email only 
#logic - [a-z] - must start with a to z
#\w - used for may be the mail end with digit 
# + - used to add all the patterns 
import re
a = "123johns123@gmail.com123"
x = re.findall("[a-z]+\w+@gmail.com",a)
print(x)
exit()


#this code fetches both mail and  mobile no 
import re
a = "johns123@gmail.comleo123@yahoo.com770895585396599527749944337977leo123@hotmail.com"
x = re.findall("[a-z]+\w+@gmail.com|[a-z]+\w+@yahoo.com|[a-z]+\w+@outlook.com|[a-z]+\w+@hotmail.com|[6-9]\d{9}",a)
print(x)
exit()







