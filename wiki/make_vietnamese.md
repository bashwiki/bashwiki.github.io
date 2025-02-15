# [리눅스] Bash make 사용법

## Tổng quan
Lệnh `make` là một công cụ tự động hóa được sử dụng chủ yếu để biên dịch và xây dựng các dự án phần mềm. Nó đọc một tệp có tên là `Makefile`, nơi định nghĩa các quy tắc và phụ thuộc giữa các tệp nguồn và tệp nhị phân. Mục đích chính của `make` là giúp quản lý quá trình biên dịch, giảm thiểu thời gian cần thiết để xây dựng lại các tệp không thay đổi và tự động hóa các tác vụ phức tạp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `make` như sau:

```bash
make [tùy chọn] [mục tiêu]
```

### Các tùy chọn phổ biến:
- `-f <tên_tệp>`: Chỉ định tệp Makefile khác với tệp mặc định (Makefile hoặc makefile).
- `-j <số>`: Chạy nhiều tác vụ song song, giúp tăng tốc độ biên dịch.
- `-B`: Buộc biên dịch lại tất cả các mục tiêu, bất kể chúng có thay đổi hay không.
- `-n`: Hiển thị các lệnh mà `make` sẽ thực hiện mà không thực sự thực hiện chúng.

## Ví dụ
### Ví dụ 1: Biên dịch một dự án đơn giản
Giả sử bạn có một tệp `Makefile` như sau:

```makefile
all: program

program: main.o utils.o
    gcc -o program main.o utils.o

main.o: main.c
    gcc -c main.c

utils.o: utils.c
    gcc -c utils.c
```

Bạn có thể chạy lệnh sau để biên dịch dự án:

```bash
make
```

### Ví dụ 2: Chạy biên dịch song song
Nếu bạn muốn tăng tốc độ biên dịch bằng cách sử dụng 4 luồng, bạn có thể sử dụng tùy chọn `-j`:

```bash
make -j4
```

## Mẹo
- **Sử dụng Makefile rõ ràng**: Đảm bảo rằng Makefile của bạn được tổ chức tốt và dễ hiểu. Sử dụng các biến để giảm thiểu sự lặp lại.
- **Kiểm tra phụ thuộc**: Đảm bảo rằng tất cả các phụ thuộc được định nghĩa chính xác trong Makefile để tránh lỗi biên dịch.
- **Sử dụng lệnh `make clean`**: Thêm một mục tiêu `clean` trong Makefile để xóa các tệp nhị phân và tệp tạm thời, giúp giữ cho thư mục làm việc của bạn gọn gàng.

Bằng cách sử dụng lệnh `make`, bạn có thể tự động hóa quá trình biên dịch và tiết kiệm thời gian trong việc phát triển phần mềm.