a = int(input("enter the no to be summed: ")) #123
sum = 0
while a > 0:        
    b = a % 10
    sum = sum + b
    a = a // 10
print(f"the sum of the given no is {sum}")


a = int(input("enter the starting no: "))
c = int(input("enter the ending no: "))
for a in range(a, c+1):
    sum = 0
    while a > 0:
        print(a)
        b = a % 10
        sum = sum + b
        a = a // 10
    print("the sum of the digit is",sum)
exit()





