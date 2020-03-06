a = 4
fac = 1
for i in range(1, a + 1):
        fac = fac * i
print("The factorial of", i, "is" , fac) 
exit()

a = int(input("enter the starting range: "))
b = int(input("enter the ending range: "))
fac = 1
for i in range(a,b+1):
    fac = fac * i
    print(f"the fac of the given no {i} is {fac}")
exit()



a = int(input("enter the no : "))
fac = 1
for i in range(1,a+1):
    fac = fac * i
    print(f"{i} {fac}")
    



