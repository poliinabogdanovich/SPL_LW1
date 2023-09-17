i = 0
num = 2
while i < 1001:
    k = 0
    for j in range(2, num):
        if num % j == 0:
            k += 1
            break
    if k == 0:
        print(num)
        i += 1
    num += 1