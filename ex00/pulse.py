n = int(input())
x = int(input())
p = int(input())
if p >= n and p <= x:
    print("Пульс в норме", end =  "")
if p < n:
    print("Пульс низкий", end =  "")
if p > x:
    print("Пульс высокий", end =  "")

