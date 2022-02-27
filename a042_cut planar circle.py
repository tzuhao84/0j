# tzuhao's solution for a042_cut the planar circle
# The key is the arithmetic sequence

while True:
    try:
        n=int(input())
        if n==1:
            print('2')
        else:
            ans=2+(n-1)*n
            print(ans)
    except EOFError:
        break