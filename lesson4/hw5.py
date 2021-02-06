k = input(':')
c = ['!','.','\'',' '] 
b = ''
for i in k:
    if i in c:
        b +='*'
    else:
        b += i
print(b)        