s = ["1", "4", "0", "6", "9"]
a = ["7", "2", "1", "0", "5"]
s.sort()
print(s)
for i in range(len(a)):
    min_index = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_index]:
            min_index = j
    a[i], a[min_index] = a[min_index], a[i]
print(a)