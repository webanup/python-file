class A:
    def displayA(self):
        print("welcome anup")
        
class B:
    def displayB(self):
        print("welcome back anup")
        
class C(A,B):
    def displayC(self):
        print("again welcome back anup")        
        
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
        
            