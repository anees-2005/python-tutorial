# importing enteart module
# import module

# a=module.zxc("anees")
# print(a)


# import only specific function from the module
# from module import zxc
# a=zxc("anees")
# print(a)

# importing module with a short function name(alias)
# from module import asd as d
# a=d("anees")
# print(a)
# import module with a short name(alias)
# import module as mo
# a=mo.asd("anees")
# print(a)


# import sys
# print(sys.version_info)

# import json
# a='{"name":"anees","age":20}'
# b=json.loads(a)
# print(b)


# popular third party librarys (install using pip)
# import numpy as np
# ar=np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(ar[1,2])



# pandas (for a data manupulaction and working structure data)
# import pandas as pd
# data ={"name":["jhon","brito",'jons'],
#        "place":['valnchery','kuttipuram','koppam'],
#        "age":[20,30,40]}
# a=pd.DataFrame(data)
# print(a)


# import matplotlib.pyplot as plt
# x = [0,1,2,3]
# y= [10,20,30,40]
# plt.plot(x,y)
# plt.show()


# request
# import requests 
# b=requests.get('https://www.bmw.in/en/index.html')
# print(b.status_code)


# from bs4 import BeautifulSoup
# import requests
# c=requests.get("https://www.bmw.in/en/index.html")
# v=BeautifulSoup(c.content,'html.parser')
# print(v.title.text)


# open cv (imge,video,processing)``
import cv2 
img=cv2.imread('image_one.jpg')
cv2.imshow('Image',img)
cv2.waitKey(0)



# next class varumboll HTTP status code nokkivarannam(example:404 error code)

