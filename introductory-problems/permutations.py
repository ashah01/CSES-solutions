n = int(input())
permutation = []
chosen = [False for _ in range(n+1)]

def search():
    if (len(permutation) == n):
        f = False
        for i in range(n-1):
            if abs(permutation[i] - permutation[i+1]) == 1:
                f = True
                break
        
        if not f:
            print(*permutation)
            quit()
    
    else:
        for i in range(1, n+1):
            if chosen[i]: continue
            chosen[i] = True
            permutation.append(i)
            search()
            chosen[i] = False
            permutation.pop()

search()

print("NO SOLUTION")