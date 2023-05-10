from collections import Counter

n,m = map(int,input().split())

rows = []
cols = [{} for i in range(m)]
grid = []

for i in range(n):
    s = input()
    rows.append(Counter(s))
    grid.append(list(s))

    for j in range(m):
        if s[j] not in cols[j]:
            cols[j][s[j]] = 1

        else:
            cols[j][s[j]] += 1

res = ""
for row in range(n):
    for col in range(m):
        ele = grid[row][col]
        if rows[row][ele] == 1 and cols[col][ele] == 1:
            res += ele

print(res)
