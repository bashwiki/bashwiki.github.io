# [Linux] Bash uname cách sử dụng: Hiển thị thông tin hệ thống

## Tổng quan
Lệnh `uname` trong Bash được sử dụng để hiển thị thông tin về hệ thống đang chạy, bao gồm tên kernel, tên máy, phiên bản kernel, và nhiều thông tin khác. Đây là một công cụ hữu ích để kiểm tra cấu hình hệ thống và xác định môi trường hoạt động.

## Cách sử dụng
Cú pháp cơ bản của lệnh `uname` như sau:

```
uname [tùy chọn] [tham số]
```

## Tùy chọn phổ biến
Dưới đây là một số tùy chọn thường gặp của lệnh `uname` cùng với giải thích ngắn gọn:

- `-a`: Hiển thị tất cả thông tin hệ thống.
- `-s`: Hiển thị tên kernel.
- `-n`: Hiển thị tên máy.
- `-r`: Hiển thị phiên bản kernel.
- `-v`: Hiển thị thông tin phiên bản kernel.
- `-m`: Hiển thị kiến trúc máy (ví dụ: x86_64).
- `-o`: Hiển thị tên hệ điều hành.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `uname`:

1. Hiển thị tất cả thông tin hệ thống:
   ```bash
   uname -a
   ```

2. Hiển thị tên kernel:
   ```bash
   uname -s
   ```

3. Hiển thị phiên bản kernel:
   ```bash
   uname -r
   ```

4. Hiển thị kiến trúc máy:
   ```bash
   uname -m
   ```

5. Hiển thị tên hệ điều hành:
   ```bash
   uname -o
   ```

## Mẹo
- Sử dụng tùy chọn `-a` để có cái nhìn tổng quát nhất về hệ thống của bạn.
- Kết hợp lệnh `uname` với các lệnh khác như `grep` để lọc thông tin cụ thể mà bạn cần.
- Thường xuyên kiểm tra thông tin hệ thống giúp bạn nắm bắt được tình trạng và cấu hình của máy chủ hoặc máy tính cá nhân.