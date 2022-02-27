# tzuhao's solution for Armstrong number

while True:
    try:
        ls=list(map(int,input().split()))
        n=ls[0]
        m=ls[1]
        # print(n,m)
        ans=[]
        for i in range(n,m+1):
            digit=len(list(str(i))) # the digit of the number
            digit=int(digit)
            sum=0
            for j in list(str(i)):
                sum=sum+int(j)**digit
            if i == sum:
                ans.append(i)
        if len(ans)!= 0: 
            print(*ans)
        else:
            print('none')
    except EOFError:
        break

        

