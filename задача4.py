s = 'Enjoy every moment'

d = {}
for i in range (len(s)):
    if s[i] in d:
        d[s[i]] += 1
    else:
        d[s[i]] = 1
print(d)