n = int(input())
adjacencyMatrix = []
for _ in range(n):
    row = list(map(int,input().split()))
    adjacencyMatrix.append(row)

pairs = [[0,0] for _ in range(n)]
for row in range(n):
    for col in range(n):
        if adjacencyMatrix[row][col] == 1:
            pairs[row][0] = 1
            break
for row in range(n):
    for col in range(n):
        if adjacencyMatrix[col][row] == 1:
            pairs[row][1] = 1
            break

source = []
sink = []
for i in range(n):
    row,col = pairs[i]
    if row == 0 and col == 0:
        source.append(i+1)
        sink.append(i+1)
    elif row == 0 and col == 1:
        sink.append(i+1)
    elif row == 1 and col == 0:
        source.append(i+1)
print(len(source), *source)
print(len(sink), *sink)
