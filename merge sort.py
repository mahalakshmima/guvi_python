a=int(input())
if 1<=a<=100000:
  li=[int(i) for i in input().split()]
  li.sort()
  for i in li:
    print(i,end=" ")
