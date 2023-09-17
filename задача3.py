print("Enter elements:")
s = input()
l = s.split()

for i in range(len(l)):
    l[i] = int(l[i])

mx = l[0]
for i in range(len(l)):
    if l[i] % 2 != 0 and l[i] > mx:
        mx = l[i]
print("Max element:", mx)

mn = 98632567789975
for i in range(len(l)):
   if l[i] < 0:
     l[i] = -l[i]
   if l[i] < mn:
       mn = l[i]
print("Min element:", mn)




