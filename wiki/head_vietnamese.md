# [Linux] Bash head cách sử dụng: Lấy dòng đầu tiên của tệp

## Overview
Lệnh `head` trong Bash được sử dụng để hiển thị một số dòng đầu tiên của một tệp. Mặc định, nó sẽ hiển thị 10 dòng đầu tiên, nhưng bạn có thể tùy chỉnh số lượng dòng muốn hiển thị.

## Usage
Cú pháp cơ bản của lệnh `head` như sau:
```
head [options] [arguments]
```

## Common Options
- `-n [number]`: Chỉ định số dòng muốn hiển thị. Ví dụ: `-n 5` sẽ hiển thị 5 dòng đầu tiên.
- `-c [number]`: Hiển thị số byte đầu tiên thay vì số dòng.
- `-q`: Không hiển thị tên tệp khi có nhiều tệp được chỉ định.
- `-v`: Luôn hiển thị tên tệp ngay cả khi chỉ có một tệp.

## Common Examples
- Hiển thị 10 dòng đầu tiên của tệp `file.txt`:
  ```bash
  head file.txt
  ```

- Hiển thị 5 dòng đầu tiên của tệp `file.txt`:
  ```bash
  head -n 5 file.txt
  ```

- Hiển thị 100 byte đầu tiên của tệp `file.txt`:
  ```bash
  head -c 100 file.txt
  ```

- Hiển thị 10 dòng đầu tiên của nhiều tệp và không hiển thị tên tệp:
  ```bash
  head -q file1.txt file2.txt
  ```

## Tips
- Sử dụng `head` kết hợp với các lệnh khác như `grep` hoặc `sort` để lọc và hiển thị dữ liệu một cách hiệu quả.
- Nếu bạn muốn xem các dòng cuối cùng của tệp, hãy sử dụng lệnh `tail` thay vì `head`.
- Lệnh `head` rất hữu ích khi bạn chỉ cần xem nhanh nội dung của tệp lớn mà không cần mở toàn bộ tệp.