# [Linux] Bash tail cách sử dụng: Xem nội dung cuối của tệp tin

## Overview
Lệnh `tail` trong Bash được sử dụng để hiển thị nội dung cuối cùng của một tệp tin. Đây là công cụ hữu ích để theo dõi các tệp log hoặc xem nhanh nội dung mà không cần mở toàn bộ tệp.

## Usage
Cú pháp cơ bản của lệnh `tail` như sau:
```
tail [options] [arguments]
```

## Common Options
- `-n [number]`: Hiển thị số dòng cuối cùng được chỉ định từ tệp.
- `-f`: Theo dõi tệp tin trong thời gian thực, hiển thị các dòng mới được thêm vào.
- `-c [number]`: Hiển thị số byte cuối cùng được chỉ định từ tệp.
- `-q`: Không hiển thị tiêu đề tệp khi có nhiều tệp được chỉ định.

## Common Examples
- Hiển thị 10 dòng cuối cùng của tệp `log.txt`:
  ```bash
  tail log.txt
  ```

- Hiển thị 20 dòng cuối cùng của tệp `data.txt`:
  ```bash
  tail -n 20 data.txt
  ```

- Theo dõi tệp `server.log` trong thời gian thực:
  ```bash
  tail -f server.log
  ```

- Hiển thị 50 byte cuối cùng của tệp `file.txt`:
  ```bash
  tail -c 50 file.txt
  ```

## Tips
- Sử dụng `tail -f` để theo dõi các tệp log trong thời gian thực, rất hữu ích cho việc phát hiện lỗi.
- Kết hợp `tail` với các lệnh khác như `grep` để lọc các dòng cụ thể từ tệp.
- Bạn có thể sử dụng `tail` với nhiều tệp cùng lúc để so sánh nội dung cuối của chúng.