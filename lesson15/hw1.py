def r(d,f):
    return d + f 

def k(d,f):
    return d - f

def l(d,f):
    return d * f 

def o(d,f):
    if f != 0:
        return d / f 
    return 'Error'    

def b(s,d,f):
    if s == "+":
        print(r(d,f))
    if s == "-":
        print(k(d,f))       
    if s == "*":
        print(l(d,f))
    if s == "/":
        print(o(d,f))        
s = input('знак')  
d = int(input('число'))      
f = int(input('число2')) 
print(b(s,d,f))

