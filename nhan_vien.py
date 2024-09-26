
nhan_vien = {
    '001': {'ten': 'Nguyen Van A','chuc danh': 'nhan vien' , 'sdt': '0123456789', 'email': 'a@gmail.com'},
    '002': {'ten': 'Le Thi B','chuc danh': 'nhan vien', 'sdt': '0987654321','email': 'b@gmail.com'},
    '003': {'ten': 'Tran Van C','chuc danh': 'nhan vien', 'sdt': '0912345678','email': 'c@gmail.com'}
}

def xac_nhan():
    while True:
        y_n = input("Bạn có chắc chắn muốn thực hiện hành động này? (Y/N): ").upper()
        if y_n == 'Y':
            return True
        elif y_n == 'N':
            return False
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập Y hoặc N.")
            
def CT_5():
    while True:
        print("\n Quản lý thông tin nhân viên")
        print("++---------------++")
        print("|1. Mã nhân viên  |")
        print("|2. Tên nhân viên |") 
        print("|3. Chức danh     |")
        print("|4. Số điện thoại |")
        print("|5. Email         |")
        print("|6. Thêm          |")
        print("|7. Thoát         |")  
        print("++---------------++")
        
        try:
            chon_4 = int(input("\nChức năng bạn mong muốn: "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 11.")
            continue       
        if chon_4 == 1:
            print("Chức năng đang phát triển")
        elif chon_4 == 2:
            print("Chức năng đang phát triển")
        elif chon_4 == 3:
            print("Chức năng đang phát triển")
        elif chon_4 == 4:
            print("Chức năng đang phát triển")
        elif chon_4 == 5:
            print("Chức năng đang phát triển")
        elif chon_4 == 6:
            Cc_11()   
        elif chon_4 == 7:
            xac_nhan()
            print("Cảm ơn dùng")   
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")               

def Cc_11():
    while True:
        print("\nQuản lý thông tin nhân viên")
        print(" ++------------------------------++")
        print(" |Chức năng 1: Hiển thị danh sách nhân viên  |")
        print(" |Chức năng 2: Tìm kiếm/Lọc nhân viên        |")
        print(" |Chức năng 3: Thêm mới nhân viên            |")
        print(" |Chức năng 4: Cập nhật thông tin nhân viên  |")
        print(" |Chức năng 5: Xóa nhân viên                 |")
        print(" |Chức năng 6: Xem chi tiết nhân viên        |")
        print(" |Chức năng 7: Phân loại theo phòng ban      |")
        print(" |Chức năng 8: Xuất báo cáo nhân viên        |")
        print(" |Chức năng 9: Gửi thông báo cho nhân viên   |")
        print(" |Chức năng 10: Đánh giá nhân viên           |")
        print(" |Chức năng 11: Thoát                        |")
        print(" ++-----------------------------------------++")

        try:
            chon_5 = int(input("\nChức năng bạn mong muốn: "))
        except ValueError:
            print("Vui lòng nhập số từ 1 đến 11.")
            continue
        
        if chon_5 == 1:
            cc_1()
        elif chon_5 == 2:
            cc_2()
        elif chon_5 == 3:
            cc_3()
        elif chon_5 == 4:
            cc_4()
        elif chon_5 == 5:
            cc_5()
        elif chon_5 == 6:
            cc_6()
        elif chon_5 == 7:
            cc_7()
        elif chon_5 == 8:
            cc_8()
        elif chon_5 == 9:
            cc_9()
        elif chon_5 == 10:
            cc_10()
        elif chon_5 == 11:
            if xac_nhan():
                print("Thoát chương trình.")
                break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")

def cc_1():
    for id, info in nhan_vien.items():
     print("ID:", id)
     print("Tên:", info['ten'])
     print("-" * 20) 

def cc_2():
    mnv_tim_kiem = input("Nhập ID nhân viên cần tìm: ")
    if mnv_tim_kiem in nhan_vien:
        info = nhan_vien[mnv_tim_kiem]
        print('Thông tin nhân viên có ID: ',mnv_tim_kiem)
        print("Tên:", info['ten'])
        print("Chức danh:", info['chuc danh'])
        print("SĐT:", info['sdt'])
        print("Email:", info['email'])
        print("-" * 20)
    else:
        print('Không tìm thấy nhân viên với ID: ',mnv_tim_kiem)


def cc_3():
    if xac_nhan():
     id_moi         = input("Nhập ID nhân viên mới: ")
     ten_moi        = input("Nhập tên nhân viên mới: ")
     chuc_danh_moi  = input("Nhập chức danh: ")
     sdt_moi        = input("Nhập số điện thoại: ")
     email_moi      = input("Nhập email: ")


     nhan_vien[id_moi] = {
        'ten': ten_moi,
        'chuc danh': chuc_danh_moi,
        'sdt': sdt_moi,
        'email': email_moi
}

    print("Danh sách sau khi thêm nhân viên mới:", nhan_vien)
         
def cc_4():
    if xac_nhan():
        mnv_cap_nhat = input("Nhập ID của nhân viên muốn cập nhật: ")

        if mnv_cap_nhat in nhan_vien:
         ten_moi        = input("Nhập tên mới (hoặc nhấn Enter để giữ nguyên): ")
         chuc_danh_moi  = input("Nhập chức danh mới (hoặc nhấn Enter để giữ nguyên): ")
         sdt_moi        = input("Nhập số điện thoại mới (hoặc nhấn Enter để giữ nguyên): ")
         email_moi      = input("Nhập email mới (hoặc nhấn Enter để giữ nguyên): ")

        if ten_moi:
             nhan_vien[mnv_cap_nhat]['ten'] = ten_moi
        if chuc_danh_moi:
             nhan_vien[mnv_cap_nhat]['chuc danh'] = chuc_danh_moi
        if sdt_moi:
             nhan_vien[mnv_cap_nhat]['sdt'] = sdt_moi
        if email_moi:
             nhan_vien[mnv_cap_nhat]['email'] = email_moi

             print(f"Đã cập nhật thông tin nhân viên có ID {mnv_cap_nhat}")
        else:
            print(f"Không tìm thấy nhân viên có ID {mnv_cap_nhat}")
            print("Danh sách nhân viên sau khi cập nhật:", nhan_vien)
def cc_5():
    if xac_nhan():
        mnv_xoa = input("Nhập ID nhân viên muốn xóa: ")
    if mnv_xoa in nhan_vien:
     del nhan_vien[mnv_xoa]
     print(f"Đã xóa nhân viên có ID {mnv_xoa}")
    else:
     print(f"Không tìm thấy nhân viên có ID {mnv_xoa}")
     print("Danh sách nhân viên sau khi xóa:", nhan_vien)
def cc_6():
    for id, info in nhan_vien.items():
     print("ID:", id)
     print("Tên:", info['ten'])
     print("Chức danh:", info['chuc danh'])
     print("SĐT:", info['sdt'])
     print("Email:", info['email'])
     print("-" * 20) 

def cc_7():
    print("Chức năng đang phát triển")

def cc_8():
    print("Chức năng đang phát triển")

def cc_9():
    print("Chức năng đang phát triển")

def cc_10():
    print("Chức năng đang phát triển")
            
