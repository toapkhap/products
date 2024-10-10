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