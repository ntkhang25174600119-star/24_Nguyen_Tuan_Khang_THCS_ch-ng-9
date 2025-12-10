def so_nguyen_to(n):
    if n < 2: 
        return False 
    for i in range(2, n):
        return False 
    return True

def so_nguyen_to_trong_khoang(a, b):
        for n in range(a, b + 1):
            if so_nguyen_to(n):
                print(n, end=" ")      
        
so_nguyen_to_trong_khoang(1, 30)


def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def in_so_nguyen_to_trong_khoang(a, b):
    for n in range(a, b + 1):
        if la_so_nguyen_to(n):
            print(n, end=" ")

# chạy thử
in_so_nguyen_to_trong_khoang(1, 30)