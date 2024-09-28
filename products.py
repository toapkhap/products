def san_pham():
    san_pham=[{
        'Mã sản phẩm': 'Sp001',
        'Tên sản phẩm': 'Quần kaki',
        'Giá': 7200,
        'Danh mục': 'Thời trang',
        'Mô tả': 'Chất lượng cotton'
    },
    {
        'Mã sản phẩm': 'Sp002',
        'Tên sản phẩm': 'Áo sơ mi',
        'Giá': 2000,
        'Danh mục': 'Thời trang',
        'Mô tả': 'Trắng trơn'
    }]
    while True:
        print("---Các chức năng---")
        print("1.Hiện thị sản phẩm!")
        print("2.Thêm sản phẩm mới!")
        print("3.Cập nhật thông tin sản phẩm!")
        print("4.Tìm kiếm sản phẩm!")
        print("5.Xoá sản phẩm!")
        print("6.Sản phẩm có giá tiền lớn nhất!")
        print("7.Sản phẩm có giá tiền nhỏ nhất!")
        print("8.Đếm số sản phẩm có trong danh sách!")
        print("9.Xoá tất cả thông tin sản phẩm trong danh sách!")
        print("10.Hiện thị danh sách sản phẩm theo danh mục!")
        print("11.Thoát chương trình!")
        chon=int(input("Mời bạn chọn chức năng: "))
        if chon==1:
            if not san_pham:
                print("Danh sách sản phẩm đang trống")
            else:
                for i in san_pham:
                    print(f"Mã sản phẩm:{i['Mã sản phẩm']},Tên sản phẩm:{i['Tên sản phẩm']},Giá:{i['Giá']},Danh mục:{i['Danh mục']},Mô tả:{i['Mô tả']}")
        elif chon==2:
            lua_chon=input("Bạn có chắc chắn muốn thêm sản phẩm mới không(Yes/No): ")
            if lua_chon=='Yes': 
                them_san_pham={}                
                them_san_pham['Mã sản phẩm']=input("Mời bạn nhập mã sản phẩm mới: ")
                them_san_pham['Tên sản phẩm']=input("Mời bạn nhập tên sản phẩm mới: ")
                them_san_pham['Giá']=int(input("Mời bạn nhập giá sản phẩm mới: "))
                them_san_pham['Danh mục']=input("Mời ban nhập danh mục cho sản phẩm mới: ")
                them_san_pham['Mô tả']=input("Mời bạn mô tả cho sản phẩm mới: ")
                san_pham.append(them_san_pham)
                print("Chúc mừng bạn đã thêm thành công!")
                lua_chon=input("Bạn có muốn xem thông tin sản phẩm vừa thêm không(xem/không): ")
                if lua_chon=='xem':
                    for key,vlues in them_san_pham.items():
                        print(f"{key}:{vlues}")
                elif lua_chon=='không':
                    print("Mời bạn chọn các chức năng khác")
            elif lua_chon=='No':
                print("Huỷ thêm sản phẩm mới, mời bạn chọn chức năng khác!")
            else:
                print("Lựa chọn không hợp lệ,mời bạn chọn lại")
        elif chon==3:
            lua_chon=input("Bạn có chắc chắn muốn cập nhật thông tin sản phẩm mới không(Yes/No): ")
            nhap_ma=input("Mời bạn nhập mã sản phẩm muốn sửa: ")
            for them_san_pham in san_pham:
                if lua_chon=='Yes':
                    if nhap_ma in them_san_pham['Mã sản phẩm']:
                        them_san_pham['Tên sản phẩm']=input("Mời bạn nhập tên mới sản phẩm: ")
                        them_san_pham['Giá']=int(input("Mời bạn nhập giá mới của sản phẩm: "))
                        them_san_pham['Danh mục']=input("Mời bạn nhập danh mục mới của sản phẩm: ")
                        them_san_pham['Mô tả']=input("Mời bạn nhập mô tả mới của sản phẩm: ")
                        print("Cập nhật thành công!")
                    elif nhap_ma not in them_san_pham['Mã sản phẩm']:
                        print("Sản phẩm này không tồn tại")
                elif lua_chon=='No':
                    print("Huỷ cập nhật sản phẩm,mời bạn chọn chức năng khác!")
                else:
                    print("Lựa chọn sai cú pháp!")
        elif chon==4:
            ma_san_pham=input("Mời bạn nhập mã sản phẩm tìm kiếm: ")
            for them_san_pham in san_pham:
                if ma_san_pham in them_san_pham['Mã sản phẩm']:
                    print(them_san_pham)
                    break
            else:
                print("Mã sản phẩm không tồn tại")
        elif chon==5:
            ma_san_pham=input("Mời bạn nhập mã sản phẩm bạn muốn xoá: ")
            for them_san_pham in san_pham:
                if ma_san_pham in them_san_pham['Mã sản phẩm']:
                    lua_chon=input("Bạn có chắc chắn muốn xoá sản phẩm không: ")
                    if lua_chon=='Yes':
                        san_pham.remove(them_san_pham)
                        print("Xoá thành công")
                        break
                elif ma_san_pham not in them_san_pham['Mã sản phẩm']:
                        print("Mã sản phẩm không tồn tại")
            else:
                print("Huỷ xoá sản phẩm")
        elif chon==6:
            gia_lon_nhat=max(san_pham,key=lambda x: x['Giá'])
            print("Sản phẩm có giá cao nhất là: ",gia_lon_nhat)
        elif chon==7:
            gia_nho_nhat=min(san_pham,key=lambda x: x['Giá'])
            print("Sản phẩm có giá thấp nhất là: ",gia_nho_nhat)
        elif chon==8:
            so_san_pham=len(san_pham)
            print("Số sản phẩm đang có trong danh sách là: ",so_san_pham)
        elif chon==9:
            lua_chon=input("Bạn có chắc chắn muốn hết tất cả sản phẩm không(Yes/No):")
            if lua_chon=='Yes':
                san_pham.clear()
                print("Xoá thành công")
            elif lua_chon=='No':
                print("Huỷ xoá tất cả thành công!")
            else:
                print("Mời bạn chọn chức năng khác!")
        elif chon==10:
            danh_muc=input("Mời bạn nhập danh mục sản phẩm muốn tìm kiếm: ")
            cac_danh_muc=[s_p for s_p in san_pham if s_p['Danh mục']==danh_muc]
            if cac_danh_muc:
                for s_p in cac_danh_muc:
                    print(f"Mã sản phẩm:{s_p['Mã sản phẩm']},Tên sản phẩm:{s_p['Tên sản phẩm']},Giá:{s_p['Giá']},Danh mục:{s_p['Danh mục']},Mô tả:{s_p['Mô tả']}")
            else:
                print("Danh mục không có trong danh sách")
        elif chon==11:
            lua_chon=input("Bạn có chắc chắn muốn thoát chương trình(Yes/No): ")
            if lua_chon=='No':
                print("Mời bạn chọn chức năng tiếp!")
            elif lua_chon=='Yes':
                print("Thoát chương trình thành công")
                break
    