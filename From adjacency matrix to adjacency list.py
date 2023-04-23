from collections import defaultdict
n = int(input())
adjacency_list = defaultdict(list)
for i in range(n):
    row = list(map(int,input().split()))
    for j in range(n):
        if row[j] == 1:
            adjacency_list[i+1].append(j+1)
            
for key,val in adjacency_list.items():
    if len(val) > 0:
        print(len(val), *val)
