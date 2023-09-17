s = 'gj3jhf79*%9&^^'

t = ""
for i in range(len(s)):
   if s[i].isdigit():
       t += s[i]
   else:
       if len(t)>0:
           print(t)
           t = ""