a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
print("", end = "")
for j in range(c,d+1):
    print("\t", j, end ="")
print()
for i in range(a,b+1):
    print(i, end = "")
    for j in range(c,d+1):
        print("\t", j*i, end= "")
    print()