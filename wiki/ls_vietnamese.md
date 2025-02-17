# [Linux] Bash ls Cách sử dụng: Liệt kê các tệp và thư mục

## Overview
Lệnh `ls` trong Bash được sử dụng để liệt kê các tệp và thư mục trong một thư mục cụ thể. Đây là một trong những lệnh cơ bản và thường được sử dụng nhất trong môi trường dòng lệnh.

## Usage
Cú pháp cơ bản của lệnh `ls` như sau:
```bash
ls [options] [arguments]
```

## Common Options
- `-l`: Hiển thị thông tin chi tiết về các tệp và thư mục.
- `-a`: Hiển thị tất cả các tệp, bao gồm cả các tệp ẩn (bắt đầu bằng dấu chấm).
- `-h`: Hiển thị kích thước tệp ở định dạng dễ đọc (như KB, MB).
- `-R`: Liệt kê các thư mục và tệp trong tất cả các thư mục con.
- `-t`: Sắp xếp các tệp theo thời gian sửa đổi gần nhất.

## Common Examples
- Liệt kê tất cả các tệp và thư mục trong thư mục hiện tại:
  ```bash
  ls
  ```

- Liệt kê tất cả các tệp, bao gồm cả tệp ẩn:
  ```bash
  ls -a
  ```

- Hiển thị thông tin chi tiết về các tệp:
  ```bash
  ls -l
  ```

- Liệt kê các tệp trong thư mục con:
  ```bash
  ls -R
  ```

- Liệt kê các tệp và sắp xếp theo thời gian sửa đổi:
  ```bash
  ls -lt
  ```

## Tips
- Sử dụng `ls -lh` để có thông tin chi tiết với kích thước dễ đọc.
- Kết hợp nhiều tùy chọn, ví dụ: `ls -la` để xem tất cả các tệp với thông tin chi tiết.
- Thêm đường dẫn vào lệnh để liệt kê tệp trong thư mục khác, ví dụ: `ls /path/to/directory`.