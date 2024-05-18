list1 = ['physics','chenmistry',1997,2000]
list2 = [1,2,3,4,5,6,7]
list3 = ["a","b","c","d","a"]

print("list1[0]:",list1[0])
print("list2[1:5]:",list2[1:5])

list = []
list.append('Google')
list.append('Runoob')
print(list)

print(list1)
del list1[2]
print(list1)

print(list3.count("e"))

list.extend(list3)
print(list)

print(list.index('a'))
list.insert(0,'aa')
print(list)
temp = list.pop(0)
print(temp)
print(list)
list.remove('a')
print(list)

list.reverse()
print(list)
