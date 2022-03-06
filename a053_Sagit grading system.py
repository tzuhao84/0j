# tzuhao solution for zerojudge a053

while True:
    try:
        
        n=int(input())
        if (n>=40):
            ans=100
        else:
            if 0<=n<=10:
                ans=n*6
            if 11<=n<=20:
                ans=60+(n-10)*2
            if 21<=n<40:
                ans=60+20+(n-20)*1
        print(ans)
            
    except EOFError:
        break
