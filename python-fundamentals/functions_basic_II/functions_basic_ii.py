# 1. countdown
newList = []
def countdown(num):
    newList.append(num)
    while num > 0:
        num -= 1
        newList.append(num)
countdown(5)
print(newList)

# 2. print and return
def par(a,b):
    print(a)
    return b

par(1,2)

# 3. first plus length
def fpl(some_list):
    sum = some_list[0] + len(some_list)
    print(sum)

fpl([5,4,3,2,1])

# 4. values greater than second
def values(some_list):
    newList = []
    for i in range(len(some_list)):
        if i > some_list[1]:
            newList += i
        else:
            pass


# 5. this length that value