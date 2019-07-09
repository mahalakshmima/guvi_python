r=0
ab,bi=map(int,input().split())
ne=list(map(int,input().split()))[:ab]
for sh in ne:
  if sh==bi:
    r+=1
if(r!=0):
  print("yes")
else:
  print("no")