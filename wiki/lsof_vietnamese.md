# [Linux] Bash lsof Cách sử dụng: Liệt kê các tệp đang mở

## Overview
Lệnh `lsof` (List Open Files) được sử dụng để liệt kê tất cả các tệp đang mở trên hệ thống. Nó cung cấp thông tin về các tiến trình đang sử dụng tệp, giúp người dùng theo dõi và quản lý tài nguyên hệ thống hiệu quả hơn.

## Usage
Cú pháp cơ bản của lệnh lsof như sau:
```
lsof [options] [arguments]
```

## Common Options
- `-i`: Hiển thị các tệp mạng đang mở.
- `-u`: Liệt kê các tệp mở bởi một người dùng cụ thể.
- `-p`: Hiển thị các tệp mở bởi một tiến trình cụ thể.
- `+D`: Liệt kê tất cả các tệp mở trong một thư mục cụ thể.
- `-t`: Chỉ hiển thị ID của tiến trình (PID) mà không có thông tin chi tiết.

## Common Examples
- Liệt kê tất cả các tệp đang mở:
  ```bash
  lsof
  ```

- Liệt kê các tệp mở bởi một người dùng cụ thể:
  ```bash
  lsof -u username
  ```

- Hiển thị các tệp mạng đang mở:
  ```bash
  lsof -i
  ```

- Liệt kê các tệp mở bởi một tiến trình cụ thể:
  ```bash
  lsof -p 1234
  ```

- Liệt kê tất cả các tệp mở trong một thư mục:
  ```bash
  lsof +D /path/to/directory
  ```

## Tips
- Sử dụng lệnh `lsof` với quyền root để có thể xem tất cả các tệp mở của hệ thống.
- Kết hợp lệnh `grep` với `lsof` để lọc kết quả theo nhu cầu cụ thể, ví dụ: `lsof | grep filename`.
- Để theo dõi các tệp mở theo thời gian thực, bạn có thể sử dụng lệnh `watch`, ví dụ: `watch lsof`.