num = int(input())  
sum = 0  
a=len(str(num))
temp = num  
  
while temp > 0:  
   digit = temp % 10  
   sum += digit ** a 
   temp //= 10  
  
if num == sum:  
   print("yes")  
else:  
   print("no")  