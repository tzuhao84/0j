# tzuhao solution for a022

<<<<<<< HEAD
=======



>>>>>>> 65a949b92cf7020288f731fff903d12125b8161d
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
