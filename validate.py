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