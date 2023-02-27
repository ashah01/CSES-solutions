n = int(input())
nlist = list(range(n, 0, -1))
t = n * (n + 1) // 2

if t % 2 != 0:
    print("NO")
else:
    s1 = []
    s2 = []
    if n % 2 != 0:
        s1.append(1)
        s1.append(2)
        s2.append(3)
        del nlist[-1]
        del nlist[-1]
        del nlist[-1]
    for i in range(len(nlist)//2):
        if i % 2 == 0:
            s1.append(nlist[i])
            s1.append(nlist[-(i+1)])
        else:
            s2.append(nlist[i])
            s2.append(nlist[-(i+1)])
    print("YES")
    print(len(s1))
    print(*s1)
    print(len(s2))
    print(*s2)

