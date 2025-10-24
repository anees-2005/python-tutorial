# def greet(name, age):
#     print(f"hello {name}, you are {age} year old")

# greet("anees",20)
# greet("jhone",30)


# print vs return
# def add(a,b):
#     print(a+b)
# a=add(2,5)
# print(a)

# def add(a,b):
#     return a+b
# a=add(5,2)
# print(a)

# types of arguments
# def add(name,message):
#     return f"my name is {name} hallo {message}"
# print("anees","good mornning")

# key word argument
# print(add(name="anees", message="good mornning"))


# defualt argument
# def add(message,name="anees"):
#     return f"my name is{name} hallo {message}"
# print(add("good mornning"))



# doc
# def add(a,b):
#     '''this is your output'''
#     return a+b
# # print(add(2,5))
# print(add.__doc__)

# # lambda
# add=lambda a,b: a+b
# print(add(5,5))



# reduce
from functools import reduce
num=[1,2,3,4,5,6,7,8,9,10]
c=reduce(lambda a,b:a+b,num,0)
print((c))


# filter
# num=[1,2,3,4,5,6,7,8,9,10]
# c=filter(lambda a:a%2==0,num)
# print(list(c))

# map
# num=[1,2,3,4,5,6,7,8,9,10]
# c=map(lambda a:a**2,num)
# print(list(c))


# highorder function
# def abc(n):
#     return lambda a:a+n
# b=abc(10)
# print(b(5))




# (high order function)---------------





# local and global
# x=10  #global scope (variable define at the top that is before any function)
# def local():
#     x=5 #local scope (variable define inside a funcction)
#     print(x)#local

# local()

# print(x)#global


# x=10
# def outer():
#     x=5 #anclosing(variable in the local scope of anclosing function(nested function))
#     def inner():
#         x=8
#         print(x)
#     inner()
# outer()
# print(x)




# arbitrary argumnet
# def abc(*num):
#     total=0
#     for i in num:
#         total+=i
#     return total
# a=abc(1,2,3,4,7,8,9)
# print(a)



# def abc(*name):
#     return name
# print(abc("anees","jhon","bob"))


# key word argument
# def abc(**name):
#     return name
# print(abc(n="anees",age=20,city="valanchery"))


# def abc(**name):
#     for k,v in name.items():
#         print(f"{k} {v}")
# abc(n="anees",age=20,city="valanchery")



# def abc(*a, **b):
#     print(a)
#     print(b)
# abc(1,2,3, name="anees",age=20,city="valanchery")


# def abc(c,*a, **b):
#     print(c)
#     print(a)
#     print(b)
# abc(1,2,3, name="anees",age=20,city="valanchery")


# recruction
# def factorial(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*factorial(a-1)
# print(factorial(5))


# a=5
# for i in range(a==0):
#     for j in range(a==1):
#         print(a)


# def facto(n):
#     f=1
#     for i in range(1,n+1):
#         f=f*i
#     return f
# print(facto(5))





# tail recruction
# def factorial(n, accumulator=1):
#     if n ==0 or n==1:
#         return accumulator
#     else:
#         return factorial(n-1, accumulator *n)
# print(factorial(5))


# fibonacci 
# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(5))



# sum of a list
# def sum_list(n):
#     if not n:
#         return 0
#     else:
#         return n [0]+ sum_list(n[1:])
# print(sum_list([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))



# itration
# def sum(n):
#     a=0
#     for i in range(1,n+1):
#         a+=i
#     return a
# print(sum(7))


# check of limit
# import sys
# a=sys.getrecursionlimit()
# print(a)

