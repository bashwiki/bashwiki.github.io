# [리눅스] Bash dirs 사용법

## Tổng quan
Lệnh `dirs` trong Bash được sử dụng để hiển thị danh sách các thư mục hiện tại trong ngăn xếp thư mục. Ngăn xếp thư mục cho phép người dùng lưu trữ và chuyển đổi giữa nhiều thư mục một cách dễ dàng. Mục đích chính của lệnh này là giúp người dùng theo dõi các thư mục mà họ đã truy cập trong phiên làm việc hiện tại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dirs` như sau:

```bash
dirs [options]
```

### Các tùy chọn phổ biến:
- `-l`: Hiển thị danh sách các thư mục trong định dạng dài.
- `-p`: Hiển thị danh sách các thư mục mà không có bất kỳ ký tự nào khác (như dấu ngoặc đơn).
- `+N`: Hiển thị thư mục ở vị trí N trong ngăn xếp.
- `-N`: Hiển thị thư mục ở vị trí -N từ cuối ngăn xếp.

## Ví dụ
### Ví dụ 1: Hiển thị danh sách thư mục hiện tại
```bash
$ dirs
/home/user/projects /home/user/documents /home/user/downloads
```
Kết quả trên cho thấy ba thư mục hiện tại trong ngăn xếp.

### Ví dụ 2: Sử dụng tùy chọn -l
```bash
$ dirs -l
/home/user/projects
/home/user/documents
/home/user/downloads
```
Kết quả này hiển thị danh sách thư mục theo định dạng dài, mỗi thư mục trên một dòng.

## Mẹo
- Sử dụng lệnh `pushd` và `popd` để thêm và xóa thư mục khỏi ngăn xếp, giúp quản lý thư mục hiệu quả hơn.
- Thường xuyên kiểm tra ngăn xếp thư mục bằng cách sử dụng `dirs` để giữ cho bạn luôn cập nhật về vị trí hiện tại của mình trong hệ thống tệp.
- Kết hợp `dirs` với các lệnh khác như `cd` để dễ dàng chuyển đổi giữa các thư mục mà bạn đã truy cập gần đây.