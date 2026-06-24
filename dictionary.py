# ----------dictionary------------
# Defination of dictionary.
# creation of dictionary
# index and slicing 
# traversing of tuple
# in-built methods. count(),index()
# dictionary comprehension
# Assignment and class activity

#------------------defination and properties of dictionary----------------
#1. Dictionary is a data structure in python used to store multiple data of different types with key:value.
#2. ordered,mutable
#3. indexed by key, not position
#4. key must be unique(immutable).
#5 value can be of any type.
#6 used in fast lookup.


#creation of dictionary
# stu_profile={"aman":"noida","ravi":"delhi","sita":"mumbai"}
# print(type(stu_profile))
# print(stu_profile)

# stu_marks=dict([("aman",300),("shivam",80)])
# print(stu_marks)

# stu_profile={"aman":"noida","ravi":"delhi","sita":"mumbai"}
# stu_profile["aman"]="dubai"
# print(stu_profile)
# stu_profile["sita"]="delhi"
# print(stu_profile)

#inbuilt methods of dictionary
# stu_marks={"aman":300,"shivam":80,"ravi":90}
# v=stu_marks.values()
# k=stu_marks.keys()
# i=stu_marks.items()
# res=stu_marks.get('rohan',"not found")
# print(res)
# print(v)
# print(k)
# print(i)

# update()
# stu_marks={"aman":300,"shivam":80,"ravi":90}
# new_marks={"rohan":100,"shivam":90}
# stu_marks.update(new_marks)
# print(stu_marks)

# profile={
#     'aman':{
#         'address':['noida','delhi','dubai'],
#         'hobbies':['cricket','football','chess'],
#         'password':{"insta":443534,"fb":343434},
#     },
#     'dev':{
#         'address':['noida','delhi','dubai','varanasi'],
#         'hobbies':['cricket','football','chess'],
#         'password':{"insta":"000000","fb":343434},
#     },
# }
# res=profile['dev']["password"]["insta"]
# res=profile['aman']["password"]["insta"]

# print(res)


# #travesrsing of dictionary
# stu_marks={"aman":300,"shivam":80,"ravi":90}
# sum=0
# v=stu_marks.values()
# for i in v:
#     sum=sum+i
# print(sum)






               