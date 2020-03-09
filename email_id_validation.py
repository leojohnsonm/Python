#this code fetches the email only 
import re
a = "123johns123@gmail.com123"
x = re.findall("[a-z]+\d+@gmail.com",a)
print(x)
exit()


#this code fetches both mail and  mobile no 
import re
a = "johns123@gmail.comleo123@yahoo.com770895585396599527749944337977leo123@hotmail.com"
x = re.findall("[a-z]+\d+@gmail.com|[a-z]+\d+@yahoo.com|[a-z]+\d+@outlook.com|[a-z]+\d+@hotmail.com|[6-9]\d{9}",a)
print(x)
exit()







