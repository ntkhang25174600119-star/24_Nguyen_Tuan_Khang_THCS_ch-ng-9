def tim_so_le_lon_nhat(a,b,c):
    le = [x for x in(a,b,c) if x % 2 != 0]
    if not le:
        return -1 
    return max(le)
print(tim_so_le_lon_nhat(29,32,44))