def r(m,n):
    if m > n:
        return(n+r(n+1,m))
    if m < n:
        return(m+r(m+1,n))
    if m == n:
        return 0
    print(m,n)

m = int(input(':'))
n = int(input(':'))
print(r(m,n))