# [리눅스] Bash useradd 사용법

## Tổng quan
Lệnh `useradd` trong Bash được sử dụng để tạo một tài khoản người dùng mới trên hệ thống Linux. Lệnh này cho phép quản trị viên hệ thống thêm người dùng mới, thiết lập thông tin người dùng và cấu hình các tùy chọn liên quan đến tài khoản.

## Cách sử dụng
Cú pháp cơ bản của lệnh `useradd` như sau:

```bash
useradd [tùy chọn] tên_người_dùng
```

### Các tùy chọn phổ biến:
- `-m`: Tạo thư mục home cho người dùng mới.
- `-s`: Chỉ định shell mặc định cho người dùng (ví dụ: `/bin/bash`).
- `-G`: Thêm người dùng vào một hoặc nhiều nhóm (cách nhau bằng dấu phẩy).
- `-c`: Thêm mô tả cho tài khoản người dùng.
- `-d`: Chỉ định thư mục home cụ thể cho người dùng.

## Ví dụ
### Ví dụ 1: Tạo người dùng mới với thư mục home
```bash
useradd -m -s /bin/bash newuser
```
Lệnh trên sẽ tạo một tài khoản người dùng mới có tên là `newuser`, đồng thời tạo thư mục home cho người dùng này và thiết lập shell mặc định là `/bin/bash`.

### Ví dụ 2: Tạo người dùng mới và thêm vào nhóm
```bash
useradd -m -s /bin/bash -G sudo newuser
```
Lệnh này không chỉ tạo tài khoản `newuser` mà còn thêm người dùng vào nhóm `sudo`, cho phép người dùng này thực hiện các lệnh với quyền quản trị.

## Mẹo
- Luôn kiểm tra xem tên người dùng đã tồn tại hay chưa trước khi tạo mới để tránh xung đột.
- Sử dụng tùy chọn `-c` để thêm thông tin mô tả cho người dùng, giúp dễ dàng quản lý hơn.
- Sau khi tạo người dùng, hãy nhớ thiết lập mật khẩu cho tài khoản bằng lệnh `passwd` để bảo mật tài khoản.