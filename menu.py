import nha_san_xuat
import san_pham
import van_chuyen
import don_hang
import nhan_vien


def quan_li_chuoi_cung_ung():
    while True:
        print("----Menu-----")
        print("1.Nhà cung cấp")
        print("2.Sản phẩm")
        print("3.Vận chuyển")
        print("4.Đơn hàng")
        print("5.Nhân viên")
        print("6.Thoát chương trình")
        print("==============")
        chon_chuc_nang=input("Vui lòng chọn chức năng(1-6): ")
        
        if chon_chuc_nang=='1':
            print("Bạn đã chọn vào mục nhà cung cấp")
            nha_san_xuat.nha_san_xuat()
        elif chon_chuc_nang=='2':
            print("Bạn đã chọn vào mục sản phẩm")
            san_pham.products()
        elif chon_chuc_nang=='3':
            print("Bạn đã chọn vào mục vận chuyển")
            van_chuyen.van_chuyen()
        elif chon_chuc_nang=='4':
            don_hang.don_hang()
            print("Bạn đã chọn vào mục đơn hàng")
        elif chon_chuc_nang=='5':
            print("Bạn đã chọn vào mục nhân viên")
            nhan_vien.Cc_11()
        elif chon_chuc_nang=='6':
            print("Thoát chương trình")
            break
        else:
            print("Lựa chọn không hợp lệ,mời bạn chọn lại")
quan_li_chuoi_cung_ung()