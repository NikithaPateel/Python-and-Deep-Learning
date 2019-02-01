a = ["7", "2", "1", "0", "5"]
for i in range(len(a)):
    for j in range(0, len(a)-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)