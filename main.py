def prog(chis):
    for i  in range(1000,10000):
        vrem = i
        strok = []
        des = 1
        good = []
        for j in range(1,5):
            print(i)
            strok.append(vrem % (10 * des) // des)
            des *= 10
        for j in range(3):
            good.append(int(strok[j]) + int(strok[j+1]))
        good.pop(good.index(min(good)))
        otv = int(str(min(good))+str(max(good)))
        if otv == chis:
            print(i)
            return i
print(prog(int(input())))
