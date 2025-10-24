# # to create a file
# file=open('anees.txt','w')
# file.close()


# file=open('C:/Users/anees/OneDrive/Documents/anees.td','w')
# file.close()


# read intear content from a file as string 
# file=open('anees.txt','r')
# c=file.read()
# print(c)
# file.close()


# read one line at time
# file=open('anees.txt','r')
# c=file.readline()
# d=file.readline()
# print(c.strip())
# print(d)
# file.close()

# read one line atb for loop
# file=open('anees.txt','r')
# for line in file:
#     print(line.strip())
# file.close()


# read lines
# file=open('anees.txt','r')
# a=file.readlines()
# print(a)
# file.close()

# file=open('anees.txt','w')
# file.write('hello world')
# file.close()

# file=open('anees.txt','w')
# file.writelines(['hallo world\n','good morning'])
# file.close()

# file=open('anees.txt','a')
# file.write('\nhallow')
# file.close()

# with open ('anees.txt','r') as c:
#     w=c.read()
#     print(w)

with open ('anees.txt','r') as file:
    content = file.read()
    position = file.tell()
    print(content)
    print(position)

# file=open('anees.txt','r')
# file.seek(5)
# print(file.read())
# file.close()
