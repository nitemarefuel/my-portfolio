x = int(input("How many fibonacci interations? "))
fiblist = [1,1]
for i in range(x):
    fiblist.append(fiblist[i] + fiblist[i+1])

print(fiblist)

