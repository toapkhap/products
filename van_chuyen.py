danh_sach = [
    {'Ma': 'SP001', 'Don_hang': 'Sản phẩm 1', 'Ngay_chuyen': '2024-09-01', 'Dia_chi_giao': 'Poly 1', 'Trang_thai': 'Đang giao'},
    {'Ma': 'SP003', 'Don_hang': 'Sản phẩm 3', 'Ngay_chuyen': '2024-09-05', 'Dia_chi_giao': 'Poly 3', 'Trang_thai': 'Đã giao'},
    {'Ma': 'SP002', 'Don_hang': 'Sản phẩm 2', 'Ngay_chuyen': '2024-09-03', 'Dia_chi_giao': 'Poly 2', 'Trang_thai': 'Đang giao'},
    {'Ma': 'SP005', 'Don_hang': 'Sản phẩm 5', 'Ngay_chuyen': '2024-09-07', 'Dia_chi_giao': 'Poly 5', 'Trang_thai': 'Đang giao'},
    {'Ma': 'SP004', 'Don_hang': 'Sản phẩm 4', 'Ngay_chuyen': '2024-09-06', 'Dia_chi_giao': 'Poly 4', 'Trang_thai': 'Đã hủy'}
]

def hien_thi_danh_sach():
    if not danh_sach:
        print('Danh sách trống')
    else:
        print('Danh sách hiện tại là:')
        for don_hang in danh_sach:
            print(don_hang)

def tim_kiem():
    nhap_tim_kiem = input('Nhập mã tìm kiếm : ')
    ket_qua = [don_hang for don_hang in danh_sach if nhap_tim_kiem in don_hang['Ma']]
    if ket_qua:
        print('Kết quả tìm kiếm:')
        for don_hang in ket_qua:
            print(don_hang)
    else:
        print('Không tìm thấy mã')

def them_moi():
    nhap_ma = input('Nhập mã đơn hàng: ')
    nhap_don_hang = input('Nhập tên đơn hàng: ')
    nhap_ngay_chuyen = input('Nhập ngày chuyển: ')
    nhap_dia_chi_giao = input('Nhập địa chỉ giao: ')
    nhap_trang_thai = input('Nhập trạng thái: ')
    
    xac_nhan = input('Bạn có chắc chắn muốn thêm đối tượng này? (Y/N): ')
    if xac_nhan == 'Y':
        danh_sach.append({
            'Ma': nhap_ma, 
            'Don_hang': nhap_don_hang, 
            'Ngay_chuyen': nhap_ngay_chuyen, 
            'Dia_chi_giao': nhap_dia_chi_giao, 
            'Trang_thai': nhap_trang_thai
        })
        print('Đã thêm vào danh sách')
    else:
        print('Thao tác hủy')

def cap_nhat():
    ma = input('Nhập mã đơn hàng cần cập nhật: ')
    for don in danh_sach:
        if don['Ma'] == ma:
            nhap_cap_nhat = input('Nhập thông tin cần cập nhật : ')
            xac_nhan = input('Bạn có chắc chắn muốn cập nhật đơn hàng này? (Y/N): ')
            if xac_nhan == 'Y':
                don['Don_hang'] = input('Nhập đơn hàng mới: ')
                don['Ngay_chuyen'] = input('Nhập ngày chuyển mới : ')
                don['Dia_chi_giao'] = input('Nhập địa chỉ giao mới: ')
                don['Trang_thai'] = input('Nhập trạng thái mới: ')
                print('Cập nhật thành công')
            else:
                print('Thao tác hủy.')
            return
    print('Không tìm thấy đơn hàng')

def xoa():
    ma = input('Nhập mã đơn hàng cần xóa: ')
    for don in danh_sach:
        if don['Ma'] == ma:
            xac_nhan = input('Bạn có chắc chắn muốn xóa đơn hàng này? (Y/N): ')
            if xac_nhan == 'Y':
                danh_sach.remove(don)
                print('Xóa đơn hàng thành công')
            else:
                print('Thao tác hủy.')
            return
    print('Không tìm thấy đơn hàng')

def xem_chi_tiet():
    ma = input('Nhập mã đơn cần xem chi tiết: ')
    for don in danh_sach:
        if don['Ma'] == ma:
            print('Chi tiết đơn hàng:')
            print(don)
            return
    print('Không tìm thấy đơn hàng')

def in_danh_sach():
    print('Danh sách là:')
    hien_thi_danh_sach()

def sap_xep():
    print('Chức năng đang phát triển')

def trang_thai_don_hang():
    print('Chức năng đang phát triển')

def lich_su_don_hang():
    print('Chức năng đang phát triển')

def van_chuyen():
    while True:
        print('---Vận chuyển---')
        print('1. Hiển thị danh sách')
        print('2. Tìm kiếm/Lọc')
        print('3. Thêm mới')
        print('4. Cập nhật')
        print('5. Xóa')
        print('6. Sắp xếp')
        print('7. Xem chi tiết')
        print('8. In danh sách')
        print('9. Trạng thái đơn hàng')
        print('10. Lịch sử đơn hàng')
        print('0. Thoát')

        chon_chuc_nang = input('Chọn chức năng: ')
        if chon_chuc_nang == '1':
            hien_thi_danh_sach()
        elif chon_chuc_nang == '2':
            tim_kiem()
        elif chon_chuc_nang == '3':
            them_moi()
        elif chon_chuc_nang == '4':
            cap_nhat()
        elif chon_chuc_nang == '5':
            xoa()
        elif chon_chuc_nang == '6':
            sap_xep()
        elif chon_chuc_nang == '7':
            xem_chi_tiet()
        elif chon_chuc_nang == '8':
            in_danh_sach()
        elif chon_chuc_nang == '9':
            trang_thai_don_hang()
        elif chon_chuc_nang == '10':
            lich_su_don_hang()
        elif chon_chuc_nang == '0':
            xac_nhan = input('Bạn có chắc chắn muốn thoát? (Y/N): ')
            if xac_nhan == 'Y':
                print('Thoát chương trình.')
                break
        else:
            print("Chức năng không hợp lệ, vui lòng chọn lại.")

    