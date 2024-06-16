# Contains Employee Details
class Employee:
    def __init__(self,empid=None,name=None,salary=None):
        self.empid = empid
        self.name = name
        self.salary = salary
    def setEmpid(self,empid):
        self.empid = empid
    def setName(self,Name):
        self.name = Name
    def setSalary(self,salary):
        self.salary= salary
    def getEmpid(self):
        return self.empid
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    
E1 = Employee()
E2 = Employee(1 ,"Rahul",40000)
E1.setEmpid(2)
E1.setName("Ujjwal")
E1.setSalary(50000)
print(E2.getEmpid(),E2.getName(),E2.getSalary())
print(E1.getEmpid(),E1.getName(),E1.getSalary())

