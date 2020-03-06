a = int(input("enter the no: "))
d = a
rev = 0
while a > 0:
    b = a % 10
    rev = rev*10 + b
    a = a // 10
print(f"the entered no {d} is reversed to {rev}")
exit()



a = int(input("enter the no: "))
c = int(input("enter the no: "))
for a in range(a, c+1):
    rev = 0
    print(a)
    while a > 0:                               
        b = a % 10       
        rev = rev*10 + b
        a = a // 10
    print("the reverse of the digit is",rev)
exit()


