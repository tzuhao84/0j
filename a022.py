# tzuhao solution for a022




quiz=input()
# print(quiz)
ls=list(quiz)
reversels=list()
length=len(quiz)-1
# print('length=',length)
for i in range(len(quiz)):
    reversels.append(quiz[length-i])
# print(reversels)
reversels="".join(reversels)
# print(reversels)
if quiz==reversels:
    print('yes')
else:
    print('no')
