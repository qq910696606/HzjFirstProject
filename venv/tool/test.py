print('b')


# fenshu = input("请输入分数：")
# fenshu  = int(fenshu)
#
# x = 5
# y = 3
# small =  x if x < y else y
# print(small)


# a= list(range(10))
# for i in a:
#     print(i)

for i in range(1,10,2):
    print(i)

list = [1,2,3,4,5,6]

list.remove(2)
print(list)

del list[2]
print(list)

print(list.pop())
print(list)

print(list.pop(1))
print(list)


list = [1,333,3,44,533,26]
list.reverse()#颠倒
print(list)

list.sort()#指定方式排队，默认小到大
print(list)

list.sort(reverse=True)#指定方式排队，默认小到大
print(list)