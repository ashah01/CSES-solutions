n = int(input())
seq = sorted(list(map(int, input().split())))
for i in range(n-1):
    if seq[i] != i + 1:
        print(i + 1)
        exit()

if i == n-2:
    print(n)