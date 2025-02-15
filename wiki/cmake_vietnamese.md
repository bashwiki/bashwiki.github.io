# [리눅스] Bash cmake 사용법

## Tổng quan
`cmake` là một công cụ quản lý xây dựng phần mềm, giúp tự động hóa quá trình biên dịch và xây dựng các dự án phần mềm. Nó sử dụng các tệp cấu hình để tạo ra các tệp Makefile hoặc tệp dự án cho các IDE khác nhau, giúp lập trình viên dễ dàng biên dịch và quản lý mã nguồn của họ trên nhiều nền tảng khác nhau.

## Cách sử dụng
Cú pháp cơ bản của lệnh `cmake` như sau:

```bash
cmake [tùy chọn] [đường dẫn đến thư mục nguồn]
```

### Các tùy chọn phổ biến:
- `-S <thư mục nguồn>`: Xác định thư mục chứa mã nguồn.
- `-B <thư mục xây dựng>`: Xác định thư mục nơi các tệp xây dựng sẽ được tạo ra.
- `-G <trình tạo>`: Chỉ định trình tạo mà bạn muốn sử dụng (ví dụ: "Unix Makefiles", "Ninja").
- `-D <biến>=<giá trị>`: Đặt giá trị cho các biến cấu hình.

## Ví dụ
### Ví dụ 1: Xây dựng một dự án đơn giản
Giả sử bạn có một thư mục mã nguồn tại `~/my_project`, bạn có thể sử dụng lệnh sau để tạo thư mục xây dựng và biên dịch dự án:

```bash
mkdir ~/my_project/build
cd ~/my_project/build
cmake -S .. -B . -G "Unix Makefiles"
make
```

### Ví dụ 2: Đặt biến cấu hình
Nếu bạn muốn đặt một biến cấu hình trong quá trình xây dựng, bạn có thể làm như sau:

```bash
cmake -S ~/my_project -B ~/my_project/build -D CMAKE_BUILD_TYPE=Release
```

## Mẹo
- Luôn tạo một thư mục xây dựng riêng biệt để giữ cho mã nguồn của bạn sạch sẽ và dễ quản lý.
- Sử dụng tùy chọn `-D` để tùy chỉnh các tham số biên dịch mà không cần chỉnh sửa tệp CMakeLists.txt.
- Kiểm tra các thông báo lỗi trong quá trình chạy `cmake` để đảm bảo rằng tất cả các thư viện và phụ thuộc cần thiết đều được cài đặt đúng cách.