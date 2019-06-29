a=int(input())
if 1<=a<=1000:
  b=list(map(int,input().split()))
  b.sort()
  c = int((len(b) - 1)/2)
  print (b[c])
