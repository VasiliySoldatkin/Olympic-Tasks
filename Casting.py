k = int(input())
n, a, b, c = map(int,input().split())
if k == 2:
     s = min(a,b,c)
     print(s)
else:
     print(max(a+b+c-2*n,0))
