# [Linux] Bash du: [tính toán kích thước thư mục]

## Overview
Lệnh `du` (disk usage) được sử dụng để ước lượng kích thước của các thư mục và tệp tin trong hệ thống tệp. Nó giúp người dùng xác định dung lượng mà các tệp và thư mục chiếm trên đĩa.

## Usage
Cú pháp cơ bản của lệnh `du` như sau:
```bash
du [options] [arguments]
```

## Common Options
- `-h`: Hiển thị kích thước theo định dạng dễ đọc (KB, MB, GB).
- `-s`: Tóm tắt kích thước của thư mục mà không liệt kê các tệp con.
- `-a`: Hiển thị kích thước của tất cả các tệp và thư mục.
- `-c`: Tính tổng kích thước của tất cả các tệp và thư mục được liệt kê.
- `--max-depth=N`: Giới hạn độ sâu của thư mục hiển thị (N là số nguyên).

## Common Examples
- Để xem kích thước của thư mục hiện tại:
```bash
du -h
```

- Để xem kích thước của một thư mục cụ thể:
```bash
du -h /path/to/directory
```

- Để tóm tắt kích thước của một thư mục mà không liệt kê các tệp con:
```bash
du -sh /path/to/directory
```

- Để hiển thị kích thước của tất cả các tệp và thư mục trong thư mục hiện tại:
```bash
du -ah
```

- Để tính tổng kích thước của tất cả các thư mục trong thư mục hiện tại:
```bash
du -ch
```

- Để giới hạn độ sâu hiển thị của thư mục:
```bash
du -h --max-depth=1
```

## Tips
- Sử dụng tùy chọn `-h` để dễ dàng đọc kích thước mà không cần phải tính toán.
- Kết hợp `du` với `sort` để sắp xếp các thư mục theo kích thước:
```bash
du -h | sort -h
```
- Thường xuyên kiểm tra kích thước của các thư mục để quản lý dung lượng đĩa hiệu quả hơn.