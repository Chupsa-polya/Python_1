from turtle import colormode


a = str(input())
b = str(input())
c = str(input())
color = a[1]
flag = True
for i in b:
    if i != color:
        flag = False
        break
if c[1]!=color:
    flag = False

if flag == True:
    print ("верно")
else: 
    print ("не верно")