# tzuhao's soludtion for zerojudge a021 



ls=list(map(str,input().split()))
# print(ls)
a=int(ls[0])
b=int(ls[2])

if ls[1]=='+':
    print(a+b)
if ls[1]=='-':
    print(a-b)
if ls[1]=='*':
    print(a*b)
if ls[1]=='/':
    print(a//b)

