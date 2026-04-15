class A:
    
    def __init__(self,a):
        self.a=a
        
    def __lt__(self,other):
        if (self.a<other.a):
            return "ob1 is smaller than ob2"
        
        else:
            return "ob2 is smaller than ob1"
        
    def __eq__(self,other):
        if (self.a==other.a):
            return "ob1 and ob2 are equal"
        
        else:
            return "ob1 is'nt equal to ob2"
    
ob1=A(2)
ob2=A(1)

print('Passed values are: ',ob1.a , ob2.a)
print(ob1 < ob2)

ob1=A(3)
ob2=A(5)

print('Passed values are: ',ob1.a , ob2.a)
print(ob1 == ob2)        
            
        