# a=7
# for i in range(1, a+1):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()




# a=5
# print("*"*a)

# a=5
# for i in range(a):
#     print('*')


# a=5
# for i in range(a):
#     print('*',end='')


# a=5
# for j in range(a):
#     for i in range(a):
#         print('*',end='')



# a=5
# for j in range(a):
#     for i in range(a):
#         print('*')


# a=5
# for j in range(a):
#     for i in range(a):
#         print('*',end='')
#     print()


#MY TEST
# j=3
# i=4
# for j in range(j):                   <<<<<<<<<<<<<<<<<<
#     for i in range(i):
#         print('*',end=' ')
#     print()



# increasing triangle pattern
# a=5
# for i in range(a):          #rows  (zero index)
#     for j in range(i+1):        #colums (zero index)
#         print('*',end=' ')
#     print()



# Decreasing triangle pattern
# a=5
# for i in range(a):          #rows  (zero index)
#     for j in range(i,a):        #colums (zero index)
#         print('*',end=' ')
#     print()




# Right side triangle
# a=5
# for i in range(a):
#     for j in range(i,a):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()








# a=5
# for i in range(a):
#     for j in range(i+1):
#         print(' ',end=' ')
#     for j in range(i,a):
#         print('*',end=' ')
#     print()




# hill pattern
# a=5
# for i in range(a):
#     for j in range(i,a):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i+1):
#         print('*',end=' ')
#     print()



 # Reverse Hill Pattern
# a=5
# for i in range(a):
    # for j in range(i+1):
    #     print(' ',end=' ')
    # for j in range(i,a-1):
    #     print('*',end=' ')
    # for j in range(i,a):
    #     print('*',end=' ')
    # print()




# Diamond pattern
a=5
for i in range(a-1  ):
    for j in range(i,a):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()
for i in range(a):
    for j in range(i+1):
        print(" ",end=' ')
    for j in range(i,a-1):
        print('*',end=' ')
    for j in range(i,a):
        print('*',end=' ')
    print()