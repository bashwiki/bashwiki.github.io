# [리눅스] Bash rmdir 사용법

## Tổng quan
Lệnh `rmdir` trong Bash được sử dụng để xóa các thư mục rỗng. Mục đích chính của lệnh này là giúp người dùng quản lý hệ thống tệp bằng cách loại bỏ những thư mục không còn cần thiết, giúp giữ cho cấu trúc thư mục gọn gàng và dễ quản lý hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `rmdir` như sau:

```bash
rmdir [tùy chọn] <thư_mục>
```

### Tùy chọn phổ biến:
- `-p`: Xóa thư mục và các thư mục cha của nó nếu chúng cũng rỗng.
- `--ignore-fail-on-non-empty`: Không báo lỗi nếu thư mục không rỗng.

## Ví dụ
### Ví dụ 1: Xóa một thư mục rỗng
Giả sử bạn có một thư mục rỗng tên là `thumuc_rong`, bạn có thể xóa nó bằng lệnh sau:

```bash
rmdir thumuc_rong
```

### Ví dụ 2: Xóa thư mục và các thư mục cha rỗng
Nếu bạn có một cấu trúc thư mục như sau:

```
/home/user/thumuc_cha/thumuc_con/
```

Và cả `thumuc_con` và `thumuc_cha` đều rỗng, bạn có thể xóa chúng bằng lệnh:

```bash
rmdir -p /home/user/thumuc_cha/thumuc_con
```

## Mẹo
- Trước khi sử dụng lệnh `rmdir`, hãy đảm bảo rằng thư mục bạn muốn xóa thực sự rỗng. Bạn có thể sử dụng lệnh `ls` để kiểm tra nội dung của thư mục.
- Nếu bạn muốn xóa thư mục không rỗng, hãy sử dụng lệnh `rm -r` thay vì `rmdir`, nhưng hãy cẩn thận vì lệnh này sẽ xóa tất cả nội dung bên trong thư mục.
- Sử dụng tùy chọn `-p` một cách cẩn thận để tránh xóa nhầm các thư mục cha không còn cần thiết.