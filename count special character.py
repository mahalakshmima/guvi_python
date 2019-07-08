a=input()
count=0
for i in range(len(a)):
  if a[i].isdigit() or a[i].isalpha():
    b=0
  else:
    count+=1
print(count)