import random



n = input("Give a size for array: ")
total = 0
for i in range(0,2048):
    data = []
    for j in range((int(n))):
        data.append(0)



    for i in range(int(n)):
        p = random.randint(0,int(n)-1)
        k = random.randint(0,int(n)-1)
        if data[p] <= data[k]:
            if p <= int(n):
                data[p] = data[p] + 1
        else:
            if k <= int(n):
                data[k] = data[k] + 1


    total = total + max(data)



print(total/2048)


