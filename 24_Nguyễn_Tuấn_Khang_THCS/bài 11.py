def tinh_tich():
    return lambda a, b, c: a * b * c 
tich = tinh_tich()
print(tich(2, 3, 4)) # vdu

def tinh_tich():
    return lambda a, b, c: a * b * c

tich = tinh_tich()
print(tich(2, 3, 4))  
