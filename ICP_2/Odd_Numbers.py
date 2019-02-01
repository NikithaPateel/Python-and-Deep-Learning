odd_number = []
for i in range(100, 500):
    o = str(i)
    if(int(o[0]) % 2 != 0) and (int(o[1]) % 2 != 0) and (int(o[2]) % 2 != 0):
        odd_number.append(o)
print(odd_number)



