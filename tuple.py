# ----------tuple------------
# Defination of tuple.
# creation of tuple
# index and slicing of tuple
# traversing of tuple
# in-built methods. count(),index()
# tuple comprehension
# Assignment and class activity


# ------------------defination of tuple----------------
# tuple is a data structure in python used to store multiple data 
# of different types with comma(,) in round braces.
#immutable
# support indexing slicing and ordered.


#creation of tuple 
t1=(50,)
print(t1)
print(type(t1))


# #travesrsing of tuple
# def  tuple_fun(m):
#     new_value=[]
#     for i in m:
#         if i>55:
#             new_value.append(i)
#     return new_value
# marks_tuple=(50,60,70,80,90)
# res=tuple_fun(marks_tuple)
# print(res)

#write a fuction sum of indices of tuple.
marks_tuple=(50,60,70,80,90)
s=0
for i in  range (len(marks_tuple)):
    s+=i
print(s)




