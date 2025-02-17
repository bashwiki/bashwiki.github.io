# [Linux] Bash command tìm kiếm: Tìm kiếm tệp tin và thư mục

## Overview
Lệnh `find` trong Bash được sử dụng để tìm kiếm tệp tin và thư mục trong hệ thống tệp. Nó cho phép người dùng xác định các tiêu chí tìm kiếm khác nhau như tên tệp, kích thước, thời gian sửa đổi và nhiều thuộc tính khác.

## Usage
Cú pháp cơ bản của lệnh `find` như sau:
```
find [đường_dẫn] [tùy_chọn] [biểu_thức]
```

## Common Options
- `-name`: Tìm tệp tin theo tên.
- `-type`: Xác định loại tệp tin (ví dụ: `f` cho tệp tin, `d` cho thư mục).
- `-size`: Tìm tệp tin theo kích thước.
- `-mtime`: Tìm tệp tin theo thời gian sửa đổi (ngày).
- `-exec`: Thực thi một lệnh trên các tệp tin tìm thấy.

## Common Examples
- Tìm tất cả các tệp tin có đuôi `.txt` trong thư mục hiện tại:
  ```bash
  find . -name "*.txt"
  ```

- Tìm tất cả các thư mục trong `/home/user`:
  ```bash
  find /home/user -type d
  ```

- Tìm các tệp tin lớn hơn 1MB:
  ```bash
  find . -size +1M
  ```

- Tìm các tệp tin đã được sửa đổi trong 7 ngày qua:
  ```bash
  find . -mtime -7
  ```

- Thực thi lệnh `rm` để xóa tất cả các tệp tin `.log` tìm thấy:
  ```bash
  find . -name "*.log" -exec rm {} \;
  ```

## Tips
- Sử dụng `-iname` thay vì `-name` để tìm kiếm không phân biệt chữ hoa chữ thường.
- Kết hợp nhiều tùy chọn để tinh chỉnh kết quả tìm kiếm.
- Luôn kiểm tra kết quả tìm kiếm trước khi thực hiện các lệnh xóa để tránh mất dữ liệu không mong muốn.