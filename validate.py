def validate_ma_san_pham(ma_san_pham1):
    try:
        if not ma_san_pham1 and len(ma_san_pham1)==5 and ma_san_pham1.startswith("Sp"):
            return "Mã sản phẩm phải bắt đầu bằng Sp, mã sản phẩm không được trống"
    except ValueError:
        return "Mã sản phẩm nhập không hợp lệ"
def validate_ten_san_pham(ten_san_pham):
    try:
        if not ten_san_pham.strip() and not isinstance(ten_san_pham,str) and len(ten_san_pham)>0:
            return "Tên sản phẩm không được để trống, tên sản phẩm phải là kiểu chuỗi"
    except ValueError:
        return "Tên sản phẩm nhập không hợp lệ"
def validate_gia(gia):
    try:
        if not gia and not isinstance(gia,(float,int)) and gia<=0:
            return "Giá sản phẩm phải là số nguyên dương lớn hơn không và không được để trống"
    except ValueError:
        return "Giá sản phẩm bạn nhập không đúng định dạng"
def validate_danh_muc(danh_muc):
    try:
        if not danh_muc and not isinstance(danh_muc,str) and len(danh_muc)>3:
            return "Danh mục sản phẩm không được để trống, kiểu định dạng là chuỗi"
    except ValueError:
        return "Danh mục sản phẩm bạn nhập không đúng định dạng"
def validate_mo_ta(mo_ta):
    try:
        if not mo_ta and not isinstance(mo_ta,str) and len(mo_ta)>10:
            return "Mô tả sản phẩm không được để trống, kiểu định dạng là kiểu chuỗi"
    except ValueError:
        return "Mô tả bạn nhập không đúng dạng"