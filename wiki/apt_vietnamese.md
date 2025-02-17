# [Ubuntu] Bash apt cách sử dụng: Quản lý gói phần mềm

## Tổng quan
Lệnh `apt` là một công cụ quản lý gói trên hệ điều hành Ubuntu và các bản phân phối dựa trên Debian. Nó cho phép người dùng cài đặt, nâng cấp và gỡ bỏ các gói phần mềm một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `apt` như sau:
```
apt [tùy chọn] [tham số]
```

## Tùy chọn phổ biến
- `update`: Cập nhật danh sách các gói có sẵn.
- `upgrade`: Nâng cấp tất cả các gói đã cài đặt lên phiên bản mới nhất.
- `install`: Cài đặt một gói phần mềm mới.
- `remove`: Gỡ bỏ một gói phần mềm đã cài đặt.
- `search`: Tìm kiếm một gói phần mềm trong kho lưu trữ.

## Ví dụ phổ biến
- Cập nhật danh sách gói:
  ```bash
  sudo apt update
  ```

- Nâng cấp tất cả các gói đã cài đặt:
  ```bash
  sudo apt upgrade
  ```

- Cài đặt một gói phần mềm, ví dụ `curl`:
  ```bash
  sudo apt install curl
  ```

- Gỡ bỏ một gói phần mềm, ví dụ `curl`:
  ```bash
  sudo apt remove curl
  ```

- Tìm kiếm một gói phần mềm, ví dụ `nginx`:
  ```bash
  apt search nginx
  ```

## Mẹo
- Luôn chạy `sudo apt update` trước khi cài đặt hoặc nâng cấp để đảm bảo bạn có danh sách gói mới nhất.
- Sử dụng `apt autoremove` để gỡ bỏ các gói không còn cần thiết, giúp tiết kiệm không gian lưu trữ.
- Kiểm tra các gói đã cài đặt bằng lệnh `apt list --installed` để quản lý tốt hơn.