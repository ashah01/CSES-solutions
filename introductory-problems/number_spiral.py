n = int(input())
coords = [list(map(int, input().split())) for _ in range(n)]

for y, x in coords:
    sq = max(x, y)
    if y > x:
        if sq % 2 == 0:
            first_index = max(y, x)**2
            print(first_index - (x - 1))
        else:
            first_index = max(x, y)**2 - (2 * (max(x, y) - 1))
            print(first_index + (x - 1))
    else:
        if sq % 2 == 0:
            first_index = max(x, y)**2 - (2 * (max(x, y) - 1))
            print(first_index + (y - 1))
        else:
            first_index = max(y, x)**2
            print(first_index - (y-1))