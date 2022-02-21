s = int(input())
n = int(input())
m = 0
while (n != s):
    m = m + n
    n = int(input())
    if (n==s):
        break
print (m+n)