# [Linux] Bash basename Cách sử dụng: Trả về tên tệp từ đường dẫn

## Overview
Lệnh `basename` trong Bash được sử dụng để lấy tên tệp từ một đường dẫn đầy đủ. Nó loại bỏ phần đường dẫn và chỉ giữ lại tên tệp, giúp bạn dễ dàng làm việc với tên tệp mà không cần phải nhớ toàn bộ đường dẫn.

## Usage
Cú pháp cơ bản của lệnh `basename` như sau:
```
basename [options] [arguments]
```

## Common Options
- `-a`: Xử lý nhiều tệp và trả về tên của từng tệp.
- `-s`: Loại bỏ phần mở rộng tệp được chỉ định.
- `--help`: Hiển thị thông tin trợ giúp về lệnh.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `basename`:

1. Lấy tên tệp từ đường dẫn:
   ```bash
   basename /home/user/document.txt
   ```
   Kết quả: `document.txt`

2. Lấy tên tệp từ đường dẫn và loại bỏ phần mở rộng:
   ```bash
   basename /home/user/document.txt .txt
   ```
   Kết quả: `document`

3. Xử lý nhiều tệp cùng lúc:
   ```bash
   basename -a /home/user/file1.txt /home/user/file2.txt
   ```
   Kết quả:
   ```
   file1.txt
   file2.txt
   ```

## Tips
- Sử dụng tùy chọn `-s` để loại bỏ phần mở rộng tệp nếu bạn chỉ cần tên tệp mà không cần phần mở rộng.
- Khi làm việc với nhiều tệp, hãy sử dụng tùy chọn `-a` để tiết kiệm thời gian và công sức.
- Kết hợp `basename` với các lệnh khác như `find` để xử lý tệp một cách hiệu quả hơn.