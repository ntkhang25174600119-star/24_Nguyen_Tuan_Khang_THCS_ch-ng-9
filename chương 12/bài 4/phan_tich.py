from danh_sach import sap_xep_tang_dan
from tu_dien import lay_gia_tri
ds = [3, 5, 2, 6, 4]    
ds_sap_xep = sap_xep_tang_dan(ds)
print("Danh sách sau khi sắp xếp:", ds_sap_xep)

# Lấy giá trị từ từ điển
td = {"a": 10, "b": 20, "c": 30}
gia_tri = lay_gia_tri(td, "b")
print("Giá trị của khóa 'b':", gia_tri)