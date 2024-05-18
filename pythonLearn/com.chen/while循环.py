count = 0
while count < 9:
    print("the count is:", count)
    count = count + 1
print("good bye")

# continue和break用法
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print(i)
i = 1
while 1:
    print(i)
    i += 1
    if i > 10:
        break

count = 0
while count < 5:
    print(count,"is less than 5")
    count = count + 1
else:
    print(count,"is not less than 5")