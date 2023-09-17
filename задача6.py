c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)

if sum(c_1) > sum(c_2):
    print("Сумма больше в кортеже 1")
else:
    print("Сумма больше в кортеже 2")

mn = c_1[0]
ind_mn = 0
for i in range(len(c_1)):
    if c_1[i] < mn:
        mn = c_1[i]
        ind_mn = i

mx = c_1[0]
ind_mx = 0
for i in range(len(c_1)):
    if c_1[i] > mx:
        mx = c_1[i]
        ind_mx = i

print("Минимум в кортеже 1 по индексу =", ind_mn)
print("Максимум в кортеже 1 по индексу =", ind_mx)

mn = c_2[0]
ind_mn = 0
for i in range(len(c_2)):
    if c_2[i] < mn:
        mn = c_2[i]
        ind_mn = i

mx = c_2[0]
ind_mx = 0
for i in range(len(c_2)):
    if c_2[i] > mx:
        mx = c_2[i]
        ind_mx = i

print("Минимум в кортеже 2 по индексу =", ind_mn)
print("Максимум в кортеже 2 по индексу =", ind_mx)