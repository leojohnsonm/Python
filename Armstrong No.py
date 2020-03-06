a = int(input("enter the no: "))
arm = 0
d = a 
while d > 0:
    b = d % 10
    arm = arm + b ** 3
    d = d // 10
if a == arm:
    print(f"the entered no {a} is armstrong no")
else:
    print(f"the entered no {a} is not a armstrong no")
    
