# # # ##1) 
# # # for i in range (1,11):
# # #     print(i)

# # # ##2)
# # # i=2
# # # while i<=20:
# # #     print(i)
# # #     i+=2
    
# # # ##3)
# # # num=int(input("Enter a number"))
# # # print(f"Multiplication table of a {num}:")
# # # for i in range (1,12):
# # #     print(f"{num}*{i}={num*i}")

# # # ##4)

# # # num = int(input("Enter a number: "))

# # # if num < 2:
# # #     print(num, "is not a prime number")
# # # else:

# # #     for i in range(2, num):
# # #         if num % i == 0:
# # #             print(num, "is not a prime number")
# # #             break
# # #     else:
# # #         print(num, "is a prime number")

# # # ##5)
# # # num=int(input("Enter a number"))
# # # fact=1
# # # for i in range(1,num+1):
# # #     fact=fact*i
# # # print("factorial is",fact)

    

# # # ##6)
# # # for i in range(1,11):
# # #     if i==5:
# # #         break
# # #     print(i)
    
    
# # #  ##7)
# # # for i in range(1,11):
# # #      if i==7:
# # #          continue
# # #      print(i)
 

# # # ##8)
# # # for i in range(1,21):
# # #     if i%3==0:
# # #         continue
# # #     print(i)  

# # # ##9)
# # # for i in range(1,101):
# # #     if i%4==0 and i%6==0:
# # #         print(f"stopped at {i} (first number divisible by both 4 and 6)")
# # #         break
# # #     print(i)

# # # ##10)
# # # for i in range(1,101):
# # #     if 10<=i<=20:
# # #         continue
# # #     print(i)



# # ##LOOPS

# # ## 1)  
# # # numbers=[1,2,3,4,5]
# # # total=sum(numbers)
# # # print("sum",total)                                      

# # ##2)
# # # numbers = [1,2,3,1,5,8,6,1,2,3,4,5,4,6]
# # # duplicate=list(set(numbers))
# # # print(duplicate)

# # ##3)




# # ##5)
# # # a=[1,2]
# # # b=[3,4]
# # # # c=a+b
# # # # c.sort()
# # # # print(c)

# # # ##6)

# # # a=[1,2,3]
# # # b=[2,3,4]
# # # c=[]
# # # for i in a:
# # #     if i in b:
# # #         c.append(i)
# # # print(c)

# # # ##7)

# # # a=(1,2,3,4)
# # # for i in a:
# # #     print(i)
    
# # # ##8)

# # # a=[1,2,3,4,5]
# # # b=tuple(a)
# # # print(b)

# # ##9)

# # a=(1,5,2,9,4,8)
# # print(a.index(9))

# # ##10)
# # a=(1,2,3)
# # if 3 in a:
# #     print("yes")
# # else:
# #     print("No")


# ##11)

# a=(1,3,5,7,2,5,2,6,2)
# print(a.count(2))

# ##12)
# a=(1,3,5,7,2,5,2,6,2)
# print(len(a))

# ##13)

# a=(1,5,9)
# b=(2,4,6)
# print(a+b)

# ##14)

# a=(1,2,3)
# b=list(a)
# b[1]=5
# print(b)


# ##15)

# a = {"name": "Adithya", "age": 23}
# print(a["name"])
# print(a["age"])

##16)

# d = {}
# d["x"] = 5
# d["x"] = 10
# del d["x"]
# print(d)

# ##17)

# d = {"a": 3, "b": 7}
# for i in d:
#     if d[i] == max(d.values()):
#         print(i)
        
# ##18)

# a = {"x": 1}
# b = {"y": 2}
# for i in b:
#     a[i] = b[i]
# print(a)

# ##19)

# a = {"x": 1}
# b = {"y": 2}
# for i in b:
#     a[i] = b[i]
# print(a)

# ##20)

d = {"a": 1}
if "a" in d:
    print("Found")
    
# ##21)

# a = ["x", "y"]
# b = [10, 20]
# d = {a[0]: b[0], a[1]: b[1]}
# print(d)