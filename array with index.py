n=int(input())
array=list(map(int,input().split()))[:n]
for index,element in enumerate(array):
  print (element,index)
  