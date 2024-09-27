danh_sach_don_hang = []


def them_ma_don_hang():
    ma = input("Nhập mã đơn hàng: ")
    ngay = input("Nhập vào ngày: ")
    ncc = input("Nhập vào nhà cung cấp: ")
    ds_san_pham = input("Nhập vào sản phẩm: ")
    nv_tiep_nhan = input("Nhập vào nhân viên tiếp nhân: ")

    them_don_hang = {
        "Mã": ma,
        "Ngày": ngay,
        "Ncc": ncc,
        "Ds_san_pham": ds_san_pham,
        "Nhân viên": nv_tiep_nhan
    }
    danh_sach_don_hang.append(them_don_hang)
    while True:
        sure = input("Bạn có chắc chắn muốn thêm đối tượng này? (Y/N): ").lower()

        if sure == "y":
            print("Thêm thành công")
            return them_don_hang
        elif sure == "n":
            print("Đã hủy")
            return None
        else:
            print("Vui lòng chỉ chọn Y or N:")



def hien_don_hang():
    if not danh_sach_don_hang:
        print("Chưa có đơn hàng nào")
    else:
        print("\nDanh sách đơn hàng.")
        for don_hang in danh_sach_don_hang:
            print(f"Mã: {don_hang["Mã"]}, Ngày: {don_hang["Ngày"]}, Ncc: {don_hang["Ncc"]}, Ds_san_pham: {don_hang["Ds_san_pham"]}, Nhân Viên: {don_hang["Nhân viên"]}")
        print()




def tim_kiem_don_hang():
    seach = input("Nhập mã muốn tìm: ")
    ket_qua = [don_hang for don_hang in danh_sach_don_hang
                if seach in don_hang["Mã"]
    ]
    
    if ket_qua:
        print("Kết quả tìm được: ")
        for don_hang in ket_qua:
            print(don_hang)
    else:
        print("Ko có mã này")
    print()


def cap_nhat():
    cap_nhat_ma = input('Nhập mã đơn hàng cần cập nhật: ')
    for don_hang in danh_sach_don_hang:
        if don_hang["Mã"] == cap_nhat_ma:
            print(f"Thông tin hiện tại: {don_hang}")
            don_hang['Ngày'] = input('Nhập ngày hàng mới: ')
            don_hang['Ngay_chuyen'] = input('Nhập ngày chuyển mới : ')
            don_hang['Ds_san_pham'] = input('Nhập sản phẩm mới: ')
            don_hang['Trang_thai'] = input('Nhập trạng thái mới: ')
                
            while True:
                sure = input("Bạn chắc chắn muốn cấp nhật chứ (Y/N): ").lower()
                if sure == "y":
                    print("Cập nhật thành công")
                    return
                elif sure == "n":
                    print("Hủy cẩp nhật")
                    return None 
                else:
                    print("Chỉ được chon Y or N")
    else:      
        print('Không tìm thấy đơn hàng')



def xoa_don_hang():
    ma = input("Nhập mã đơn hàng cần xóa: ")
    for don in danh_sach_don_hang:
        if don["Mã"] == ma:
            danh_sach_don_hang.remove(don)

            while True:
                print(f"Thông tin đơn hàng hiện tại: {don}")
                sure = input("Chắc chắn xóa chưa? (Y/N): ").lowre()
                if sure == "y":
                    print("Xóa thành công")
                    return
                elif sure == "n":
                    print("Hủy xóa")
                    return
                else:
                    print("Chỉ chọn Y or N")
        else:
            print('Không tìm thấy đơn hàng')
            print()

def xem_chi_tiet():
    print("chức năng đang được phát triển")
    print()

def sap_xep_don_hang():
    print("chức năng đang được phát triển")
    print()

def thong_ke_don_hang():
    print("chức năng đang được phát triển")
    print()

def lich_su_don_hang():
    print("chức năng đang được phát triển")
    print()

def hien_thi_SP():
    print("chức năng đang được phát triển")
    print()

def don_hang():
    while True:
        print("Đơn Hàng")
        print("1. Thêm đơn hàng")
        print("2. Hiện thị đơn hàng")
        print("3. Tim kiếm đơn hàng")
        print("4. Cập nhật đơn hàng")
        print("5. Xóa")
        print("CHỨC NĂNG SÁNG TẠO")
        print("6. Xem chi tiết đơn hàng")
        print("7. Săp xếp đơn hàng")
        print("8. Thống kê đơn hàng")
        print("9. Lịch sử đặt hàng")
        print("10. Hiện thị sản phẩm")
        print("11. Thoát")
        chon = input("Mơi bạn chon: ")

        if chon == "1":
            them_ma_don_hang()
        elif chon == "2":
            hien_don_hang()
        elif chon == "3":
            tim_kiem_don_hang()
        elif chon == "4":
            cap_nhat()
        elif chon == "5":
            xoa_don_hang()
        elif chon == "6":
            xem_chi_tiet()
        elif chon == "7":
            sap_xep_don_hang()
        elif chon == "8":
            thong_ke_don_hang()
        elif chon == "9":
            lich_su_don_hang()
        elif chon == "10":
            hien_thi_SP()
        elif chon == "11":
            break
        else:
            print("Mời bạn chọn lại")