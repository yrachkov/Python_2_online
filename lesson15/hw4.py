s = 99999
h = s // 3600
d = s // 86400 
f = (s-86400) // 3600
if d >= 1:
    print(d ,'день')
    if f >= 1:
        print(f,'годин')
if d < 1:
    print('0 день')
    if h >= 1:
        print(h,'годин')   
    else:
        print('0 годин')