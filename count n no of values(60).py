count=0
num=int(input())
if num<=100000:
  for i in range(1,num+1):
    count+=i
  print(count)