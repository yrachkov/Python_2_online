from collections import Counter
s = ['ромашка','ромашка','ромашка','ромашка','toffix','toffix','toffix']
l = Counter(s)
for i,r in l.items():
    if r%2 ==0:
        print(i)