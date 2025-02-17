# [Linux] Bash ln cách sử dụng: Tạo liên kết tệp

## Overview
Lệnh `ln` trong Bash được sử dụng để tạo liên kết giữa các tệp. Có hai loại liên kết: liên kết cứng (hard link) và liên kết mềm (symbolic link). Liên kết cứng tạo ra một tên khác cho cùng một tệp, trong khi liên kết mềm tạo ra một đường dẫn đến tệp gốc.

## Usage
Cú pháp cơ bản của lệnh `ln` như sau:
```
ln [options] [arguments]
```

## Common Options
- `-s`: Tạo liên kết mềm thay vì liên kết cứng.
- `-f`: Buộc ghi đè lên tệp đích nếu nó đã tồn tại.
- `-n`: Không ghi đè lên tệp đích nếu nó là một liên kết.
- `-v`: Hiển thị thông tin chi tiết về các liên kết được tạo.

## Common Examples
- Tạo một liên kết cứng:
  ```bash
  ln file.txt link_to_file.txt
  ```

- Tạo một liên kết mềm:
  ```bash
  ln -s file.txt symlink_to_file.txt
  ```

- Tạo liên kết mềm với ghi đè:
  ```bash
  ln -sf file.txt symlink_to_file.txt
  ```

- Tạo liên kết cho nhiều tệp:
  ```bash
  ln -s file1.txt file2.txt file3.txt symlink_to_files/
  ```

## Tips
- Sử dụng liên kết mềm khi bạn cần tạo đường dẫn đến tệp trong các thư mục khác nhau.
- Hãy cẩn thận với liên kết cứng, vì chúng không thể được tạo cho các tệp nằm trên các hệ thống tệp khác nhau.
- Kiểm tra liên kết bằng lệnh `ls -l` để xem thông tin chi tiết về các liên kết đã tạo.