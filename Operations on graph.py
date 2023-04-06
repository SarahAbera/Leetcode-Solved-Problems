from collections import defaultdict
n = int(input())
k = int(input())
graph = defaultdict(list)
for _ in range(k):
    operation = list(map(int,input().split()))
    if operation[0] == 1:
        graph[operation[1]].append(operation[2])
        graph[operation[2]].append(operation[1])

    if operation[0] == 2:
        print(*graph[operation[1]])
