a,b=input().split()
for Number in range (int(a)+1,int(b)):
    cnt = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            cnt += 1
            break

    if (cnt == 0 and Number != 1):
        print(" %d" %Number, end = '  ')