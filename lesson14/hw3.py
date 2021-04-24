def r(x):
    if x==[]:
        return 0
    else:
        return x[0]+r(x[1:])
 
print(r([1,2,3,4]))