# TODO: experiment with dynamic approach to reduce time complexity

"""
in: 5

out: 1, 3, 5, 2, 4


in: 4
out: 2, 4, 1, 3



1. If n = 1, return 1

2. if n ∈ {2, 3}, return no sol

3. Until n letters are obtained:
    - Start at 2, start incrementing two
    - If end of array is reached (or n-1), restart index at 1

"""

def solve(n):
    if n == 1: return [1]
    
    if n == 2 or n == 3: return["NO SOLUTION"]

    sequence = []
    i = 2

    while (len(sequence) < n):
        sequence.append(i)
        if (i + 2 <= n):
            i += 2
        else:
            i = 1
    
    return sequence


n = int(input())
print(*solve(n))
