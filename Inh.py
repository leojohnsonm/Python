class A:
    def ip(self):
        self.a = int(input("enter the no: "))
class B:
    def log(self):
        self.Sum = 0
        while self.a > 0:
            self.b = self.a % 10
            self.Sum = self.Sum + self.b
            self.a = self.a // 10
class C(A, B):
    def res(self):
        print(self.Sum)
obj = C()
obj.ip()
obj.log()
obj.res()
