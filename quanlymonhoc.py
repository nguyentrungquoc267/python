'''
Xây dựng chương trình quản lý môn học gồm các thông tin: mã môn học , tên môn học ,
số tín chỉ . chương trình được thực hiện các công việc sau :
- nhập 1 danh sách  môn học 
- hiển thị thông tin các môn học 
- thêm được 1 môn học 
- xóa được 1 môn học theo mã 
- tìm kiếm thông tin môn học theo cả 3 trường : mã môn học , tên môn học và số tín chỉ 
- ghi thông tin của các môn học vào tệp MonHoc.txt
- đọc thông tin môn học từ tệp MonHoc.txt
'''

class MonHoc:
    # hàm khởi trạo ( contructor)
    def __init__(self,maMH,tenMH,soTC):
        self.maMH=maMH
        self.tenMH=tenMH
        self.soTC=soTC
    # phương thức hiển thị trong lớp
    def hienthiMH(self):
        print("mã môn học :",self.maMH)
        print("tên môn học :",self.tenMH)
        print("số tín chỉ :",self.soTC)
# khai báo 1 list rỗng 
dsMH = []
# hàm nhập danh sách môn học 
def nhapDSMH():
    n=int(input("nhập số lượng môn học : "))
    for i in range(n):
        maMH=input("nhập vaò mã môn học :")
        tenMH=input(("nhập vào tên môn học "))
        soTC=input("nhập vào số tín chỉ môn học : ")
        mh=MonHoc(maMH, tenMH, soTC)
        dsMH.append(mh)
# hàm hiển thị danh sách môn học 
def hienthiDSMH():
    print("danh sách môn học là: ")
    for i in range(len(dsMH)):
        print("thôngtin môn học ",i+1)
        dsMH[i].hienthiMH()
# hàm thêm môn học 
def themMH():
    while True:
        print("nhập vào thông tin môn học cần thêm :")
        maMH=input("nhập vaò mã môn học :")
        tenMH=input(("nhập vào tên môn học "))
        soTC=input("nhập vào số tín chỉ môn học : ")
        mh = MonHoc(maMH,tenMH,soTC)
        dsMH.append(mh)

        tiep_tuc = input("Bạn có muốn nhập thêm môn học khác không? (có/không): ")
        if tiep_tuc.lower() != 'có':
            break
# hàm xóa thông tin theo mã môn học 
def xoaMHtheoMa():
    maXoa=input("nhập vào mã môn học muốn xóa : ")
    for mh in dsMH:
        if(mh.maMH == maXoa):
            dsMH.remove(mh)
# hàm tìm kiếm thông tin 
def timkiem():
    thongtin=input("nhập thông tin môn học cần tìm ( mã , tên , số tc ): ")
    for i in range(len(dsMH)):
        if(dsMH[i].maMH== thongtin or dsMH[i].tenMH==thongtin or dsMH[i].soTC==thongtin):
            print("kết quả tìm kiếm : ")
            dsMH[i].hienthiMH()
#ghi dsmh vào  tệp  
def ghiDSMHvaotep():
    with open("MonHoc.txt","w") as file:
        n=len(dsMH)
        file.write(str(n)+"\n")
        for i in range(n):
            file.write(dsMH[i].maMH+ "\n") 
            file.write(dsMH[i].tenMH+ "\n")
            file.write(dsMH[i].soTC+ "\n")
# hàm đọc ds môn học từ tệp 
def docDSMHtutep():
    with open("MonHoc.txt","r") as file:
        n = int(file.readline())
        print("số lượng môn học là :",n)
        for i in range(n):
            print("mã môn học :",file.readline(),end = "")
            print("tên môn học :",file.readline(),end = "")
            print("số tín chỉ :",file.readline(),end = "")

# hàm main 
def main():
    while True:
        print("1. Nhập danh sách môn học ")
        print("2. Đọc danh sách môn học từ tệp ")
        print("3. Hiển thị danh sách môn học ")
        print("4. Thêm 1 môn học mới ")
        print("5. Xóa 1 môn học theo mã")
        print("6. Tìm kiếm 1 môn học ")
        print("7. Ghi danh sách môn học vào tệp ")
        print("8. Lưu và thoát ")

        luachon= int(input("Mời bạn cconj chức năng (1-7): "))

        if(luachon==1):
            nhapDSMH()
        elif (luachon==2):
            print("Danh sách môn học được đọc từ tệp là :")
            docDSMHtutep()
        elif(luachon==3):
            hienthiDSMH()
        elif(luachon==4):
            themMH()
            print("ds môn học sau khi thêm ")
            hienthiDSMH()
        elif(luachon==5):
            xoaMHtheoMa()
            print("ds môn học sau khi đã xóa : ")
            hienthiDSMH()
        elif(luachon==6):
            timkiem()
        elif(luachon==7):
            ghiDSMHvaotep()
        elif(luachon==8):
            break

#gọi main :
main()