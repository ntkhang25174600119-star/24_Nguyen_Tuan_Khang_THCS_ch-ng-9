def kiem_tra_so_armstrong(n):
    return n == sum(int(d)**3 for d in str(n))
print(kiem_tra_so_armstrong(153))
print(kiem_tra_so_armstrong(254))
