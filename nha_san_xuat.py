nha_cung_cap = []


def xac_nhan_hanh_dong():
    while True:
        tra_loi = input("{Thông báo} (Y/N): ").strip().upper()
        if tra_loi in ['Y' , 'N']:
            return tra_loi == 'Y'
        print("Mời bạn chọn Y (có) hoặc N (không)")


def hien_thi_nha_cung_cap():
    
    print("Danh sach nhà cung cấp: ")
    for ncc in nha_cung_cap:
        print(ncc)

def tim_kiem_nha_cung_cap():
    tu_khoa = input("Nhập từ khóa tìm kiếm: ")
    ket_qua = [ ncc for ncc in nha_cung_cap if tu_khoa in ncc["Tên"]]
    print("Kết quả tìm kiếm: ")
    for kq  in ket_qua:
        print(kq) 

def them_nha_cung_cap():
    nha_cung_cap_mơi = {

        "Ma": input("Nhập mã nhà cung cấp: "),
        "Tên": input("Nhập tên nhà cung cấp: "),
        "Địa chỉ": input("Nhập địa chỉ nhà cung cấp: "),
        "SĐT": input("Nhập số điện thoại nhà cung cấp: "),
        "Điều khoản": input("Nhập điều khoản: ")

    }
    nha_cung_cap.append(nha_cung_cap_mơi)
    print("Nhà cung cấp đã được thêm mới.")

def cap_nhat_nha_cung_cap():
    ma = input("Nhập mã nhà cung cấp cần cập nhật: ")
    for ncc in nha_cung_cap:
        if ncc["Mã"] == ma:
            ncc ["Tên"] = input("Nhập mã mới: ")
            ncc ["Địa chỉ: "] = input("Nhập đại chỉ mới: ")
            ncc ["Sđt"] = input("Nhập số điện thoại mới: ")
            ncc ["Điều khoản"] = input("Nhập điều khoản mới: ")
            print("Nhà cung cấp cập nhật")
            return
    print("Không tìm thấy nahf cung cấp cần cập nhật với mã này")


def xoa_nha_cung_cap():
    ma = input("Nhập mã nhà cung cấp cần xóa: ")
    global nha_cung_cap
    nha_cung_cap = [ ncc for ncc in nha_cung_cap if ncc ["Mã"] != ma]
    print("Nhà cung cấp đã được xóa")

def chuc_nang_6():
    print("Chức năng 6: Thống kê số lượng nhà cung cấp")

def chuc_nang_7():
    print("Chức năng 7: Nhà cung cấp cấp theo khu vực")

def chuc_nang_8():
    print("Chức năng 8: Xếp hạng các nhà cung cấp")

def chuc_nang_9():
    print("Chức năng 9: ")

def chuc_nang_10():
    print("Chức năng 10: ")


def nha_san_xuat():
    while True:
        print("\MENU: ")
        print("1. Hiển thị nhà cung cấp")
        print("2. Tìm kiếm nhà cung cấp")
        print("3. Thêm nhà cung cấp")
        print("4. Cập nhật nhà cung cấp")
        print("5. Xóa nhà cung cấp")
        print("6. Thống kê số lượng nhà cung cấp")
        print("7. Nhà cung cấp theo khu vực")
        print("8. Xếp hạng các nhà cung cấp")
        print("9. Chức năng 9")
        print("10. Chức năng 10")

        chon = input("Mời bạn chọn chức năng: ")
        if chon == "1":
            hien_thi_nha_cung_cap()
        elif chon == "2":
            tim_kiem_nha_cung_cap()
        elif chon == "3":
            them_nha_cung_cap()
        elif chon == "4":
            cap_nhat_nha_cung_cap()
        elif chon == "5":
            xoa_nha_cung_cap()
        elif chon == "6":
            chuc_nang_6()
        elif chon == "7":
            chuc_nang_7()
        elif chon == "8":
            chuc_nang_8()
        elif chon == "9":
            chuc_nang_9()
        elif chon == "10":
            chuc_nang_10()
        elif chon == "0":
            break
        else:
            print("Không có chức năng này, vui lòng chọn lại chức năng từ ( 1 - 10 ).")
