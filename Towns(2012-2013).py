n = int(input())
a = []
s = 0
for i in range(n):
     a.append(input())
for i in range(n):
     for j in range(n):
          if a[i][j]=='C':
               s += 1
b = []
fir = 0
hold = s//2
m = '1'
su = ''
k = 0
for i in range(n):
     for j in range(n):
          if a[i][j] == 'C':
               if fir < hold:
                    su += m
                    fir += 1
               else:
                    m = '2'
                    fir = 0
                    su += m
          else:
               su+=m
     b.append(su)
     su = ''
inp = ''
for i in range(n):
     for j in range(n):
          inp += b[i][j]
     print(inp)
     inp = ''
