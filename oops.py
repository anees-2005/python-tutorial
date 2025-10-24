# class Car:
#     def __init__(self,make,model,year,price):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.price=price
#     def display(self):
#         return f"this car brand {self.make} and model is {self.model} year {self.year} offer price {self.price}"
    
# vari=Car("maruti","fronx",2025,"700k")
# print(vari.display())

# vari1=Car("maruti","baleno",2025,"700k")
# print(vari1.display())

# # print(vari.price)

# vari.price='500k'
# print(vari.display())



# class Iphone:
#     def __init__(self,model,year,price):
#         self.m=model
#         self.y=year
#         self.p=price
#     def display(self):
#         return f"new iphone {self.m} lounged in {self.y} this offer price {self.p}"

# apple17=Iphone("17pro max",2025,"150k")
# print(apple17.display())

# class Andriod:
#     def __init__(self,brand,model,price):
#         self.b=brand
#         self.m=model
#         self.p=price
#     def __str__(self):
#         return f"{self.b} the model is {self.m} this offer price {self.p}"
    
# andr=Andriod("realme","15pro","15k")
# print(andr)


# class Employee:
#     company= "Softroniics"
#     def __init__(self,name,position):
#         self.n=name
#         self.p=position
# no1 = Employee("anees","Employee")
# no2 = Employee("unais","staff")
# no3 = Employee("sreenand","manager")

# print(no1.n)
# print(no1.company)


# inner class
# class Employee:
#     class Company:
#         def __init__(self,name,cname,salary):
#             self.n=name
#             self.c=cname
#             self.s=salary
#     def __init__(self,gender,esalary,name,cname,salary):
#         self.g=gender
#         self.sa=esalary
#         self.company = Employee.Company(name,cname,salary)
#     def display(self):
#         print(f"Employee Name: {self.company.n}")
#         print(f"Company Name: {self.company.c}")
#         print(f"Monthly Salary: {self.company.s}")
#         print(f"Male OR Female: {self.g}")

# em= Employee("male","20k","sandeep","softroniics","50k")
# em.display()
        
# em.company.c="infopark"
# em.display()

# compossition 
# class Company:
#     def __init__(self,location,cname):
#         self.l=location
#         self.cn=cname

# class Employee:
#         def __init__(self,name,salary,location,cname):
#             self.n=name
#             self.s=salary
#             self.company=Company(location,cname)
#         def display(self):
#              print(f"my company from {self.company.l}")
#              print(f"company name {self.company.cn}")
#              print(f"name {self.n}")
#              print(f"{self.s}")
             
# em=Employee("anees",5000,"Vazhathodi","Softroniics")
# em.display() 

# del em
# print(em.company.name)

# loosly couple
# class Company:
#     def __init__(self,Lname,age):
#         self.Ln=Lname
#         self.a=age
# class Employee:
#     def __init__(self,name,location,combo):
#         self.na=name
#         self.l=location
#         self.com=combo
#     def display(self):
#         print(f"Name: {self.na} Location: {self.l} Last Name: {self.com.Ln} age {self.com.a}")
    
# A1 = Company("Mariyam",30)
# B2 = Employee("Jhon","London",A1)
# B2.display()

# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.__salary=salary
#     def display(self):
#         print(f"Name: {self.name} Salary: {self.__salary}")

#     def update_salary(self, Salary):
#         self.__salary = Salary

# A1=Employee("Jhone","40k")
# A1.display()

# A1.update_salary("70k")
# A1.display()

# single inheritance
# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         print(f"{self.name} Make a Sound")
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} Hoo hoo")
# A=Dog("Buddy")
# A.speak()


# multiple inheritance
# class Engine:
#     def V12(self):
#         print("Engine Started")
# class Wheel:
#     def inch(self):
#         print("wheel is the rotated")
# class car(Engine,Wheel):
#     def Mustang(self):
#         print("Car is 250kmh Moving")

# ford=car()

# ford.V12()
# ford.inch()
# ford.Mustang()

# class Mustang:
#     def V6(self):
#         print("First Genaration")
# class Shelby(Mustang):
#     def V8(self):
#         print("Second Genaration")
# class Dark_Horse(Shelby):
#     def V12(self):
#         print("Third Genaration")

# ford=Dark_Horse()

# ford.V6()
# ford.V8()
# ford.V12()

# class Sigma:
#     def Base(self):
#         print("1.2L Petrol")
# class Delta(Sigma):
#     def Base(self):
#         print("1.0L Turbo Boosterjet Petrol")
# class Alpha(Sigma):
#     def Base(self):
#         print("CNG")
  

# Fronx=Alpha()
# delta=Delta()

# Fronx.Base()
# delta.Base()



# class A:
#     def Base(self):
#         print("1.2L Petrol")
# class B(A):
#     def Baa(self):
#         print("1.0L Turbo Boosterjet Petrol")
# class C(A):
#     def Ba(self):
#         print("CNG")
# class D(B,C):
#     def Bas(self):
#         print("Hybrid")

# A1=D()
# A1.Base()
# A1.Baa()
# A1.Bas()
# A1.Ba()

  
# class Animal:
#     def hores(self):
#         print("animal is moving")
# class car(Animal):
#     pass
#     # def hores(self):
#     #     print("car is stable")
# class bike(Animal):
#     pass
#     # def hores(self):
#     #     print("offroad type")
# A1=[car(),bike()]
# for i in A1:
#     i.hores()


# class dog:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print("haaa")
# class Duck:
#     def __init__(self,name):
#        self.name=name
    
#     def speak(self):
#         print("raaa")
# class Human:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print("hello")

# def make(obj):
#     print(f"{obj.name} says:")
#     obj.speak()

# for A in[dog("opu"),Duck("mou"),Human("mun")]:
#     make(A)


# Abstraction
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area():
        pass
class Rectangle(Shape):
    de