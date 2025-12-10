def tim_so_fibonacci(n):
    if n == 0:
        return 0          # F(0)
    if n == 1:
        return 1          # F(1)
    return tim_so_fibonacci(n - 1) + tim_so_fibonacci(n - 2)
print(tim_so_fibonacci(7))