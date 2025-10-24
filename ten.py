# # 1
# a="anees"
# print(len(a))


# # 2
# a="hello world"
# print(a.upper())


# # 3
# b=[5,6,7,8]
# sumb=sum (b)
# print ("sum of all elements:", sumb)

# # 4
# a=[10,20,30,40]
# b=max(a)
# print(b)

# #5
# a= (1,2,3,2,4,2)
# print(a[2])


# # 6
# set1 = {1,2,3,4,}
# set2 = {6,7,8,9,}
# union_set = set1.union(set2)
# intersection_set=set1.intersection(set2)
# print("set1: ")


# # 7
# dict1={"name": "anees", "age" : "20"}
# dict2={"city": "palakkad", "age" : "22"}
# dict1. update(dict2)
# print(dict1)



# tuple1 = (1, 2, 3, 4)
# tuple2 = (3, 4, 5, 6)
# common = tuple(set(tuple1) & set(tuple2))
# print("Tuple 1:", tuple1)
# print("Tuple 2:", tuple2)
# print("Common elements:",common)




a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = max(a, b, c)
print("The largest number is:",largest)