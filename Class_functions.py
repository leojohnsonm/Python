class A:
    def ip(self):
        self.a = int(input("enter the no: "))
        self.b = int(input("enter the no: "))
    def op(self):
        self.c = self.a + self.b
        print(self.c)
obj = A()       #first call the class
obj.ip()        #then call the function - parent 
obj.op()        #then call the child class 
