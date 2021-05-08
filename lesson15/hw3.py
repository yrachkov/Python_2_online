def s(m):
    x = 1
    for i in range(1,m+1):
        x*=i
    return x
m = int(input(':'))
print(s(m))