# index error
# list1=['anees','dahad']
# print(list1[2])

# TypeError
# print(5+'anees')

# ValueError
# print(int('aa'))

# KeyError
# h={
#     "name":"anees",
#     "place":"valanchery",
# }
# print(h["age"])

# a=open('see.txt','r')
# c=a.read()
# print(c)
# a.close()


# try:
#     print(10/0)
# except ZeroDivisionError:
#     print('dash broo!')

# try:
#     a=int(input('enter a number:'))
#     c=10/a
# except ZeroDivisionError:
#     print('empty')
# else:
#     print(c)
# finally:
#     print('aaaaaa')

# d=10
# if d<=55:
#     raise ValueError('pozhi')

class AneesErorr(Exception):
    pass

def check (num):
    if num<0:
        raise AneesErorr('wooo')
try:
    check(-5)
except AneesErorr as a:
    print(a)

