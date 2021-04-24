def r(L):
    if len(L) == 1:
        return L[0]
    else:
        return max(L[0],r(L[1:]))
print(r([1,2,3,4]))