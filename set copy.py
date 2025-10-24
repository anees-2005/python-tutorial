# a = {1,2,3}
# print(type(a))

# b=set()
# print(b)


# c=set{[1,2,3]}
# print(c)


#for loop
# c={1,2,3}
# for set in c:
#     print(set)


#precense cheking
# a={1,2,3}
# print(2 in a)

# a={1,2,3}
# print(5 in a)


#add and update
# a={1,2,3}
# a.add(5)
# print(a)

# a={1,2,3}
# a.update([4,5,6])
# print(a)

#remove and discard
# a={1,2,3}
# a.remove(2)
# print(a)

# a={1,2,3}
# a.discard(3)  #remove and discard same but ilatha elamant ozhivakan nokiyall removill error adikum discar dill adikilla
# print(a)


#pop
# a={1,2,3}
# b=a.pop()
# print(a)
# print(b)


# #clear
# a={1,2,3}
# a.clear()
# print(a)



#set union
# a={1,2,3,4}
# b={5,6,7}
# c=a.union(b)
# print(c)

#intersection
# a={1,2,3}
# b={2,3,4}
# c=a & b
# print(c)

#set diffrence
# a={1,2,3}
# b={2,3,4}
# c=a - b
# print(c)


#symmetric
# a={1,2,3}
# b={2,3,4}
# c=a ^ b
# print(c)

#subset and superset
# a={1,2}
# b={1,2,3,4}
# print(a.issubset(b))

# a={1,2}
# b={1,2,3,4}
# print(a.issuperset(b))


#forzenset
# a=frozenset([1,2,3])
# print(a)
