def re():
    k = input(':') 
    c = ['a','y','e','u','o','i']
    b = 0
    for i in k:
        if i in c:
            b += 1
    print(b)
print(re())