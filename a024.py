
# def is_prime(n):
#     for i in range(2,n):
#         if n%i == 0:
#             return False
#     return True


quiz=list(map(int,input().split()))
a=max(quiz)
b=min(quiz)


GCD = a//b
modulus=a%b
while(modulus!=0):
    a=b
    b=modulus
    modulus=a%b
print (b)
    


# if is_prime(a) and is_prime(b):
#     print(1)
# else:
#     for i in range(c,0,-1):
#         if a%i==0 and b%i==0:
#             GCD=i 
#             break
#     print(GCD) 


