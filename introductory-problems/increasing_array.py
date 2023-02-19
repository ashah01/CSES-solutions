n = int(input())
seq = list(map(int, input().split()))
mods = 0
for i in range(n-1):
    if (seq[i+1] < seq[i]):
        delta = abs(seq[i+1]-seq[i])
        seq[i+1] += delta
        mods += delta

print(mods)
