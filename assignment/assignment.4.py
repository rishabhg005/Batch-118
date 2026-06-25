# Q.1. Write a Python program to find the sum of all elements in the list [10, 20, 30, 
# 40, 50].

# num= [10,20,30,40,50]
# sum=0
# for i in num:
#     sum=sum+i
# print(sum)

# Q.2. Write a Python program to display the odd and even elements from the list [10, 
# 23, 11, 12, 33, 44, 2, 5, 6].

# num=[10, 23, 11, 12, 33, 44, 2, 5, 6]
# even=[]
# odd=[]
# for i in num:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even no. is ",even)
# print("odd no is ", odd)

#Q 3. Write a Python program to count the odd and even numbers in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

# num1=[10, 23, 11, 12, 33, 44, 2, 5, 6]
# even=0
# odd=0
# for i in num1:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print("total even" , even)
# print("total odd ", odd)

# Q.4. Write a Python program to interchange the first and last elements in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].

# num2=[10, 23, 11, 12, 33, 44, 2, 5, 6]
# num2[0],num2[-1]= num2[-1],num2 [0]
# print(num2)

# Q 5. Write a Python program to duplicate all the items in the list li = [1, 2, 3], 
# such that the result is: 
# output = [1, 2, 3, 1, 2, 3, 1, 2, 3]. 
# li = [1, 2, 3]
# list1=[]

# for i in range(len(li)):
#     list1.extend(li)
# print(list1)

# 6. Find the smallest element in the list [10, 23, 11, 12, 33, 44, 2, 5, 6].
# list1= [10, 23, 11, 12, 33, 44, 2, 5, 6]
# sma_ele=list1[0]
# for i in list1:
#     if i<sma_ele:
#         sma_ele=i
# print(sma_ele)

# 7. Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64].

# list1=[89, 23, 24, 2, 55, 54, 64]
# gre_ele=list1[0]
# for i in list1:
#     if i>gre_ele:
#         gre_ele=i
# print(gre_ele)