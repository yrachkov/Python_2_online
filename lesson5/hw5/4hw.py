Gmail = 'iorjfgehjuvrh@gmail.com'
b = ''
for i,char in enumerate(Gmail):
    if i >Gmail.index('@')   <Gmail.index('.'):
        b +="*"
    else:
        b += char    
print(b)
