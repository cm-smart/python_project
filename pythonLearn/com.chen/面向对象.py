class Test:
    def prt(self):
        print(self)
        print(self.__class__)

t = Test()
t.prt()

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee:",Employee.empCount)

    def displayEmployee(self):
        print("name:",self.name,",salary:",self.salary)

emp1 = Employee("Zara",2000)
emp2 = Employee("Manni",5000)

emp1.displayEmployee()
emp2.displayEmployee()
print("total employee:",Employee.empCount)

emp1.age = 7
emp1.age = 8
del emp1.age

print("Employee.__doc__:",Employee.__doc__)
print("Employee.__name__:",Employee.__name__)
print("Employee.__module__:",Employee.__module__)
print("Employee.__bases__:",Employee.__bases__)
print("Employee.__dict__:",Employee.__dict__)

class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"销毁")
pt1 = Point()
pt2 = pt1
pt3 = pt1

print(id(pt1),id(pt2),id(pt3))
pt1.x = 10
print(pt3.x)

del pt1
del pt2
del pt3

class Parent:
    parentAttr = 100

    def __init__(self):
        print("调用父类构造函数")
    def parentMethod(self):
        print("调用父类方法")
    def setAttr(self,attr):
        Parent.parentAttr = attr
    def getAttr(self):
        print("父类属性：",Parent.parentAttr)

class Child(Parent):
    def __init__(self):
        print("调用子类构造方法")
    def childMethod(self):
        print("调用子类方法")

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()