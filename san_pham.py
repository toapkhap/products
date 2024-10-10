from luu_tru import *
from validate import *
def products():
    while True:
        print("--Các chức năng---")
        print("1.Hiện thị sản phẩm")
        print("2.Thêm sản phẩm mới")
        print("3.Cập nhật thông tin sản phẩm")
        print("4.Tìm kiếm sản phẩm")
        print("5. Xoá sản phẩm")
        print("6.Sản phẩm các giá tiền lớn nhất")
        print("7.Sản phẩm có giá tền nhỏ nhất")
        print("8.Đếm số sản phẩm có trong danh sách")
        print("9.Xoá tất cả sản phẩm trong danh sách")
        print("10.Hiện thị danh sách sản phẩm theo từng danh mục")
        print("11.Thoát chương trình")
        chon=int(input("Mời bạn chọn chức năng: "))
        if chon==1:
            hien_thi_san_pham()
        elif chon==2:
            them_san_pham()
        elif chon==3:
            cap_nhat_san_pham()
        elif chon==4:
            tim_kiem_san_pham()
        elif chon==5:
            xoa_san_pham()
        elif chon==6:
            san_pham_gia_lon_nhat()
        elif chon==7:
            san_pham_nho_nhat()
        elif chon==8:
            dem_san_pham()
        elif chon==9:
            xoa_sach_san_pham()
        elif chon==10:
            s_p_danh_muc()
        elif chon==11:
            thoat_chuong_trinh()
        else:
            print("Chức năng đó không tồn tại,mời bạn nhập lại: ")
            
def hien_thi_san_pham():
    if not san_pham:
        print("Danh sách sản phẩm đang trống")
    else:
        for i in san_pham:
            print(f"'Mã sản phẩm:{i['Mã sản phẩm']},'Tên sản phẩm:{i['Tên sản phẩm']},'Giá':{i['Giá']},'Danh mục':{i['Danh mục']},'Mô tả':{i['Mô tả']}")

def them_san_pham():
    lua_chon=validate_yes_no("Bạn có chắc chắn muốn thêm sản phẩm không(Yes/No): ")
    if lua_chon=='Yes':
        them_san_pham={}
        them_san_pham['Mã sản phẩm']=validate_products_id(san_pham)
        them_san_pham['Tên sản phẩm']=validate_product_name()
        them_san_pham['Giá']=validate_product_price()
        them_san_pham['Danh mục']=validate_category()
        them_san_pham['Mô tả']=validate_mo_ta()
        ghi_du_lieu_vao_file()
        san_pham.append(them_san_pham)
        print("Chúc  mừng bạn đã thêm sản phẩm thành công!")
        lua_chon=validate_yes_no("Bạn có muốn xem sản phẩm vừa thêm không: ")
        if lua_chon=='Yes':
            for key,values in them_san_pham.items():
                print(f"{key}:{values}")
        elif lua_chon=='No':
            print("Mời bạn chọn các chức năng khác")
    elif lua_chon=='No':
        print("Bạn đã huỷ thêm sản phẩm mới,mời bạn chọn các chức năng khác")
    else:
        print("Lựa chọn không hợp lệ,mời bạn chọn lại: ")
def cap_nhat_san_pham():
    lua_chon=validate_yes_no("Bạn có chắc chắn muốn cập nhật thông tin sản phẩm không: ")
    nhap_ma=input("Mời nhập mã sản phẩm muốn sửa: ")
    for them_san_pham in san_pham:
        if lua_chon=='Yes':
            if nhap_ma in them_san_pham['Mã sản phẩm']:
                them_san_pham['Tên sản phẩm']=validate_product_name()
                them_san_pham['Giá']=validate_product_price()
                them_san_pham['Danh mục']=validate_category()
                them_san_pham['Mô tả']=validate_mo_ta()
                ghi_du_lieu_vao_file()
                print("Thêm sản phẩm thành công")
            elif nhap_ma not in them_san_pham['Mã sản phẩm']:
                print("Mã sản phẩm không tồn tại")
        elif lua_chon=='No':
            print("Bạn đã huỷ cập nhật thông tin sản phẩm")
        else:
            print("Lựa chọn sai cú pháp,mời bạn chọn lại chức năng: ")
def tim_kiem_san_pham():
    ma_san_pham=input("Mời bạn nhập mã sản phẩm: ")
    for them_san_pham in san_pham:
        if ma_san_pham in them_san_pham['Mã sản phẩm']:
            print(them_san_pham)
            break
    else:
        print("Mã sản phẩm không tồn tại")
def xoa_san_pham():
    ma_san_pham=input("Mời bạn nhập mã sản phẩm cần xoá: ")
    for them_san_pham in san_pham:
        if ma_san_pham in them_san_pham['Mã sản phẩm']:
            lua_chon=validate_yes_no("Bạn có chắc chắn muốn xoá sản phẩm này không: ")
            if lua_chon=='Yes':
                san_pham.remove(them_san_pham)
                ghi_du_lieu_vao_file()
                print("Xoá thành công")
                break
        elif ma_san_pham not in them_san_pham['Mã sản phẩm']:
            print("Mã sản phẩm không tồn tại")
    else:
        print("Bạn đã huỷ xoá sản phẩm")
def san_pham_gia_lon_nhat():
    gia_lon_nhat=max(san_pham,key=lambda x:x['Giá'])
    print("Sản phẩm có giá tiền cao nhất là: ",gia_lon_nhat)
def san_pham_nho_nhat():
    gia_nho_nhat=min(san_pham,key=lambda x:x['Giá'])
    print("Sản phẩm có giá tiền nhỏ nhất ",gia_nho_nhat)
def dem_san_pham():
    so_san_pham=len(san_pham)
    print("Số sản phẩm trong danh sách: ",so_san_pham)
def xoa_sach_san_pham():
    lua_chon=validate_yes_no("Bạn có chắc chắn xoá hết danh sách sản phẩm không: ")
    if lua_chon=='Yes':
        san_pham.clear()
        ghi_du_lieu_vao_file()
        print("Xoá thành công!")
    elif lua_chon=='No':
        print("Bạn đã huỷ xoá danh sách sản phẩm")
    else:
        print("Bạn đã chọn sai,mời bạn chọn lại: ")
def s_p_danh_muc():
    danh_muc=input("Mời bạn nhập tên danh mục sản phẩm mà bạn muốn tìm kiếm: ")
    cac_danh_muc=[s_p for s_p in san_pham if s_p['Danh mục']==danh_muc]
    if cac_danh_muc:
        for s_p in cac_danh_muc:
            print(f"Mã sản phẩm:{s_p['Mã sản phẩm']},'Tên sản phẩm:{s_p['Tên sản phẩm']},'Giá':{s_p['Giá']},'Danh mục':{s_p['Danh mục']},'Mô tả':{s_p['Mô tả']}")
    else:
        print("Danh mục này không tồn tại")
def thoat_chuong_trinh():
    lua_chon=validate_yes_no("Bạn có chắc chắn muốn thoát chương trình không(Yes/No): ")
    if lua_chon=='No':
        print("Mời bạn tiếp tục chương trình")
    elif lua_chon=='Yes':
        print("Thoát chương trình thành công")
        exit()
products()