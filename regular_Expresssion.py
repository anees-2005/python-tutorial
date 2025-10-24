import re

# text = "hello world"
# print(re.search(r"world",text))


# text = "hello world"
# print(re.match(r"ello",text))


# text = "hel5lo3 wor4ld"
# print(re.findall(r'\d',text))


# text = "my number 455 another time 56"
# for neymar in re.finditer(r'\d',text):
#     print(neymar.group(),'at',neymar.start())

# text = "my number 455 another time 56"
# for neymar in re.finditer(r'\d+',text):
#     print(neymar.group(),'at',neymar.start())


# text = "my number 455 another time 56"
# print(re.sub(r'\d+','njr',text))

# text = "my number 455 another time 56"
# print(re.sub(r'\D+','njr',text))


# text = "my; number; 4,55, another ,time; 56"
# print(re.split(r'[;,]',text))


# text = "jhon:20, rajni:20, sumathi:30"
# print(re.findall(r'(\w+):(\d+)',text))


# pattern = re.compile(r'\d+')
# text = "my number 455 another time 56"
# print(pattern.findall(text))


# text = "MY NAME is anees"
# print(re.search(r'ANEES',text,re.IGNORECASE))


# text ='''anees
# sandeep
# unais'''
# print(re.findall(r'^s\w+',text,re.MULTILINE))


# text ='''anees
# sandeep
# unais'''
# print(re.findall(r"\w+s$",text,re.MULTILINE))

text = "hello\nworld"
print(re.search(r'hello.*world',text,re.DOTALL))