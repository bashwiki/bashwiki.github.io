# [Linux] Bash lsattr Cách sử dụng: Hiển thị thuộc tính tệp

## Overview
Lệnh `lsattr` được sử dụng để hiển thị các thuộc tính của tệp trong hệ thống tệp Linux. Nó cho phép người dùng xem các thuộc tính bảo mật và quản lý tệp, giúp kiểm soát quyền truy cập và hành vi của tệp.

## Usage
Cú pháp cơ bản của lệnh `lsattr` như sau:

```bash
lsattr [options] [arguments]
```

## Common Options
- `-a`: Hiển thị thuộc tính của tất cả các tệp, bao gồm cả tệp ẩn.
- `-d`: Chỉ hiển thị thuộc tính của thư mục, không hiển thị các tệp bên trong.
- `-R`: Thực hiện đệ quy, hiển thị thuộc tính của tất cả các tệp trong thư mục con.
- `-V`: Hiển thị thông tin chi tiết về thuộc tính tệp.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `lsattr`:

1. Hiển thị thuộc tính của tất cả các tệp trong thư mục hiện tại:
   ```bash
   lsattr
   ```

2. Hiển thị thuộc tính của tất cả các tệp, bao gồm cả tệp ẩn:
   ```bash
   lsattr -a
   ```

3. Hiển thị thuộc tính của một thư mục cụ thể:
   ```bash
   lsattr -d /path/to/directory
   ```

4. Hiển thị thuộc tính của tất cả các tệp trong thư mục con:
   ```bash
   lsattr -R /path/to/directory
   ```

5. Hiển thị thông tin chi tiết về thuộc tính tệp:
   ```bash
   lsattr -V filename
   ```

## Tips
- Sử dụng `lsattr` để kiểm tra thuộc tính tệp trước khi thực hiện các thay đổi, giúp tránh mất dữ liệu không mong muốn.
- Kết hợp `lsattr` với các lệnh khác như `chattr` để thay đổi thuộc tính tệp một cách hiệu quả.
- Thường xuyên kiểm tra các thuộc tính của tệp quan trọng để đảm bảo an toàn cho dữ liệu.