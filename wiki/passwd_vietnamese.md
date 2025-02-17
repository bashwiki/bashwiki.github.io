# [Linux] Bash passwd Cách sử dụng: Thay đổi mật khẩu người dùng

## Tổng quan
Lệnh `passwd` trong Bash được sử dụng để thay đổi mật khẩu của người dùng trong hệ thống Linux. Nó cho phép người dùng cập nhật mật khẩu của chính mình hoặc của người khác (nếu có quyền truy cập).

## Cách sử dụng
Cú pháp cơ bản của lệnh `passwd` như sau:
```
passwd [tùy chọn] [tên người dùng]
```

## Tùy chọn phổ biến
- `-d`: Xóa mật khẩu của người dùng, cho phép đăng nhập mà không cần mật khẩu.
- `-l`: Khóa tài khoản người dùng, ngăn không cho đăng nhập.
- `-u`: Mở khóa tài khoản người dùng đã bị khóa.
- `-e`: Buộc người dùng phải thay đổi mật khẩu trong lần đăng nhập tiếp theo.

## Ví dụ phổ biến
- Thay đổi mật khẩu của người dùng hiện tại:
  ```bash
  passwd
  ```

- Thay đổi mật khẩu cho một người dùng cụ thể (cần quyền root):
  ```bash
  sudo passwd ten_nguoi_dung
  ```

- Khóa tài khoản người dùng:
  ```bash
  sudo passwd -l ten_nguoi_dung
  ```

- Mở khóa tài khoản người dùng:
  ```bash
  sudo passwd -u ten_nguoi_dung
  ```

- Buộc người dùng phải thay đổi mật khẩu trong lần đăng nhập tiếp theo:
  ```bash
  sudo passwd -e ten_nguoi_dung
  ```

## Mẹo
- Luôn sử dụng mật khẩu mạnh để bảo vệ tài khoản của bạn.
- Thay đổi mật khẩu định kỳ để tăng cường bảo mật.
- Sử dụng quyền root một cách cẩn thận khi thay đổi mật khẩu của người dùng khác.