# a={
#     "name":"anees",
#     "place":"valanchery",
#     "age":20
# }
# print(a)


# a=dict(name="anees",place="kottappuram")
# print(a)


# a={
#     "name":"anees",
#     "place":"valanchery",
#     "age":20
# }
# print(a["name"])
# print(a.get("name")) #normal and get same but ilatha elamant access chezhan  nokiyall noramll error adikum get ill adikilla


#changing dict item
# a={
#      "name":"anees",
#      "place":"valanchery",
#      "age":20
# }
# a["age"]=25
# print(a)


#adding new item
# a={
#      "name":"anees",
#      "place":"valanchery",
#      "age":20
# }
# a["city"]="malappuram"
# print(a)


#removing item from dict
# a={
#      "name":"anees",
#      "place":"valanchery",
#      "age":20
# }
# b=a.pop("place")
# print(a)
# print(b)


#pop item
# a={
#      "name":"anees",
#      "place":"valanchery",
#      "age":20
# }
# b=a.popitem()
# print(a)
# print(b)

# del a["name"]
# print(a)

# a.clear()
# print(a)


# nested dict
# a ={
#     "person1":{"name":"jhon","place":"englend"},
#     "person2":{"name":"alin","place":"mexico"},
# }
# print(a["person1"]["place"])
# a["person1"]["place"]="france"
# print(a)

#keys
# a={ "name":"jhon",
#     "place": "valanchery",
#     "age":30
# }
# print(a.keys())
# print(a.values())
# print(a.items())


#update
# a={ "name":"jhon", "place": "valanchery", "age":30}
# a.update({"state":"malappuram" ,"age":40})
# print(a)


#fromkeys
# a=["name","age","place"]
# b=dict.fromkeys(a,"babu")
# print(b)


#setdefault
# a={ "name":"jhon", "place": "valanchery", "age":30}
# b=a.setdefault("state","malappuram")
# print(a)
# print(b)