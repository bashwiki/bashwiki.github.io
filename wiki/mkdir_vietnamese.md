# [Linux] Bash mkdir Cách sử dụng: Tạo thư mục mới

## Overview
Lệnh `mkdir` được sử dụng để tạo thư mục mới trong hệ thống tệp. Đây là một công cụ cơ bản nhưng rất hữu ích cho việc tổ chức và quản lý tệp tin trên máy tính.

## Usage
Cú pháp cơ bản của lệnh `mkdir` như sau:
```
mkdir [options] [arguments]
```

## Common Options
- `-p`: Tạo thư mục cha nếu nó chưa tồn tại.
- `-v`: Hiển thị thông báo khi thư mục được tạo thành công.
- `-m`: Thiết lập quyền truy cập cho thư mục mới.

## Common Examples
- Tạo một thư mục đơn giản:
  ```bash
  mkdir myfolder
  ```

- Tạo nhiều thư mục cùng lúc:
  ```bash
  mkdir folder1 folder2 folder3
  ```

- Tạo thư mục cùng với các thư mục cha:
  ```bash
  mkdir -p parent/child/grandchild
  ```

- Tạo thư mục và hiển thị thông báo:
  ```bash
  mkdir -v newfolder
  ```

- Tạo thư mục với quyền truy cập cụ thể:
  ```bash
  mkdir -m 755 mysecurefolder
  ```

## Tips
- Sử dụng tùy chọn `-p` để tránh lỗi khi thư mục cha không tồn tại.
- Kiểm tra quyền truy cập của thư mục mới để đảm bảo rằng bạn có thể truy cập và chỉnh sửa nó.
- Đặt tên thư mục rõ ràng và có tổ chức để dễ dàng tìm kiếm sau này.