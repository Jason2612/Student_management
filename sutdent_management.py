"""
Xem danh mục sinh viên
Thêm sinh viên mới vào danh mục
Cập nhật thông tin của sinh viên trong danh mục
Xóa thông tin sinh viên khỏi danh mục
Tìm kiếm thông tin sinh viên trong danh mục theo từ khóa
Sắp xếp thông tin sinh viên trong danh mục
"""

"""
Xây dựng lớp Student với các thuộc tính như mã sinh viên, họ tên, ngày tháng năm sinh, quê quán, chuyên ngành, 
lớp…Chức năng chính của lớp này là lưu giữ thông tin của 1 sinh viên

Xây dựng lớp danh mục sinh viên (Student_List) với thuộc tính là một List các đối tượng của lớp Student vừa xây dựng ở trên. 
Lớp này có các hàm thành viên tương ứng với các chức năng như đề bài yêu cầu. Mỗi hàm chức năng đều thao tác trên thuộc tính List sinh viên của lớp này. 
"""




class Student:
    def __init__(self, masv, hoten, ngaysinh, quequan, chuyennganh):
        self.masv = masv
        self.hoten = hoten
        self.ngaysinh = ngaysinh
        self.quequan = quequan
        self.chuyennganh = chuyennganh
        

    def input_info(self):
        self.masv = int(input("Nhap ma sinh vien: "))
        self.hoten = input("Nhap ho ten: ")
        self.ngaysinh = input("Nhap ngay sinh: ")
        self.quequan = input("Nhap que quan: ")
        self.chuyennganh = input("Nhap chuyen nganh: ")
        self.lst =  [self.masv, self.hoten, self.ngaysinh, self.quequan, self.chuyennganh]
        oplst.append(self.lst)
        print("\n")
    
    def output_info(self):
        for check in oplst:
            print("Ma sinh vien : ", check[0])
            print("Ho ten : ", check[1])
            print("Ngay sinh : ", check[2])
            print("Que quan : ", check[3])
            print("Chuyen nganh : ", check[4])
            print("\n")
    
    def search_info(self, student_id):
        for check in range(len(oplst)):
            if student_id == oplst[check][0]:
                print("Ma sinh vien: ", oplst[student_id-1][0])
                print("Ho ten: ", oplst[student_id-1][1])
                print("Ngay sinh: ", oplst[student_id-1][2])
                print("Que quan: ", oplst[student_id-1][3])
                print("Chuyen nganh: ", oplst[student_id-1][4])
                print("\n")
                break
        if student_id != oplst[check][0]:
            print("Không có sinh viên này")

    def update_info(self, student_id):
        for check in range(len(oplst)):
            if student_id == oplst[check][0]:
                oplst[student_id-1][1] = input("Nhap ho ten: ")
                oplst[student_id-1][2] = input("Nhap ngay sinh: ")
                oplst[student_id-1][3] = input("Nhap que quan: ")
                oplst[student_id-1][4] = input("Nhap chuyen nganh: ")
                print("\n")
                break
        
        if student_id != oplst[check][0]:
            Student.input_info(self)
    
    def delete_info(self, student_id):
        for check in range(len(oplst)):
            if student_id == oplst[check][0]:
                oplst.pop[student_id-1]
    
    def print_menu(self):
        print("Lua chon cac chuc nang sau")
        print(" 1.Them hoc sinh vao danh sach")
        print(" 2.In danh sach hoc sinh")
        print(" 3.Tìm thông tin học sinh")
        print(" 4.Thay đổi thông tin của sinh viên")
        print(" 5.Xóa thông tin sinh viên")
        print(" 0.Thoát khỏi chương trình")

oplst = []

a = Student('','','','','')
a.print_menu()
option = int(input("Nhập lựa chọn: "))
while option != 0:
        if option == 1:
            a.input_info()
            a.print_menu()
            option = int(input("Nhập lựa chọn: "))
            print("\n")
        elif option == 2:
            a.output_info()
            a.print_menu()
            option = int(input("Nhập lựa chọn: "))
            print("\n")
        elif option == 3:
            student_id = int(input("Nhập mã sinh viên: "))
            a.search_info(student_id)
            a.print_menu()
            option = int(input("Nhập lựa chọn: "))
            print("\n")
        elif option == 4:
            student_id = int(input("Nhập mã sinh viên: "))
            a.search_info(student_id)
            a.update_info(student_id)
            a.print_menu()
            option = int(input("Nhập lựa chọn: "))
            print("\n")
        elif option == 5:
            student_id = int(input("Nhập mã sinh viên: "))
            a.delete_info(student_id)
            a.print_menu()
            option = int(input("Nhập lựa chọn: "))

