n = int(input())
a = []
count = [[1 for _ in range(n+1)] for _ in range(4)]
print(count)
for i in range(n):
     a.append(int(input()))
b = 0
for g in range(1, 4):
     count[g][n] = 0
     for f in range(n-1, -1, -1):
          count[g][f] = a[f] * count[g-1][f+1] + count[g][f+1]
print(count[3][0])
