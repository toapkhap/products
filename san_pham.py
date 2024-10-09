def doc_du_lieu_tu_file():
    try:
        with open('san_pham.txt','r',encoding='utf-8') as sanpham:
            san_pham=[]
            for i in sanpham:
                ma_sp,ten_sp,gia,danh_muc,mo_ta=i.strip().split(",")
                san_pham.append({
                    'Mã sản phẩm':ma_sp,
                    'Tên sản phẩm':ten_sp,
                    'Giá':float(gia),
                    'Danh mục':danh_muc,
                    'Mô tả':mo_ta
                })
            return san_pham
    except FileNotFoundError:
        return []
def ghi_du_lieu_vao_file():
    with open('san_pham.txt','w',encoding='utf-8') as sanpham:
        for sp in san_pham:
            sanpham.write(f"{sp['Mã sản phẩm']},{sp['Tên sản phẩm']},{sp['Giá']},{sp['Danh mục']},{sp['Mô tả']}")
san_pham=doc_du_lieu_tu_file()
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
def validate_products_id(san_pham):
    ma_ton_tai=[sp['Mã sản phẩm'] for sp in san_pham]
    while True:
        ma_san_pham=input("Mời bạn nhập mã sản phẩm: ")
        if not ma_san_pham.strip():
            print("Mã sản phẩm bắt buộc không được để trống")
            continue
        if ma_san_pham in ma_ton_tai:
            print("Mã sản phẩm này đã tồn tại,vui lòng nhập mã khác")
            continue
        if ma_san_pham.startswith('Sp') and len(ma_san_pham)>=5:
            return ma_san_pham
        else:
            print("Mã sản phẩm phải bắt buộc phải bắt đầu 2 kí tự đầu là Sp và các kí tự phải lớn hơn 6")
def validate_product_name():
    while True:
        ten_san_pham=input("Mời bạn nhập tên sản phẩm: ")
        if not ten_san_pham.strip():
            print("Tên sản phẩm không được để trống")
            continue
        if isinstance(ten_san_pham,str) and len(ten_san_pham)>5:
            return ten_san_pham
        else:
            print("Tên sản phẩm phải là kiểu chuỗi ")

def validate_product_price():
    while True:
        gia_san_pham=input("Mời bạn nhập giá sản phẩm: ")
        if not gia_san_pham.strip():
            print("Giá sản phẩm không được để trống")
            continue
        try:
            gia_san_pham=float(gia_san_pham)
            if gia_san_pham >0:
                return gia_san_pham
            else:
                print("Giá sản phẩm phải là số dương")
        except ValueError:
            print("Giá sản phẩm không hợp lệ, giá bạn phải nhập giá trị bằng số")

def validate_category():
    while True:
        danh_muc=input("Mời bạn nhập danh mục sản phẩm: ")
        if not danh_muc.strip():
            print("Danh mục sản phẩm không được để trống")
            continue
        if len(danh_muc)>0 and isinstance(danh_muc,str):
            return danh_muc
        else:
            print("Danh mục sản phẩm không hợp lệ,mời bạn nhập lại")
def validate_mo_ta():
    while True:
        mo_ta=input("Mời bạn mô tả sản phẩm: ")
        if not mo_ta.strip():
            print("Mô tả không được để trống")
        if isinstance(mo_ta,str) and len(mo_ta)>0:
            return mo_ta
        else:
            print("Mã sản phẩm không hợp lệ,mời bạn nhập lại")

def validate_yes_no(prompt):
    while True:
        lua_chon=input(prompt).strip().capitalize()
        if lua_chon in ['Yes','No']:
            return lua_chon
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập 'Yes' hoặc 'No'")