# [Linux] Bash w: Xem thông tin người dùng đang đăng nhập

## Overview
Lệnh `w` trong Bash được sử dụng để hiển thị thông tin về người dùng đang đăng nhập vào hệ thống, bao gồm thời gian đăng nhập, thời gian hoạt động, và các lệnh mà họ đang thực hiện. Đây là một công cụ hữu ích để theo dõi hoạt động của người dùng trên máy chủ.

## Usage
Cú pháp cơ bản của lệnh `w` như sau:
```
w [options] [arguments]
```

## Common Options
- `-h`: Không hiển thị tiêu đề.
- `-s`: Hiển thị thông tin ngắn gọn hơn.
- `-u`: Hiển thị thông tin về thời gian hoạt động của người dùng.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `w`:

1. **Hiển thị thông tin người dùng đang đăng nhập:**
   ```bash
   w
   ```

2. **Hiển thị thông tin mà không có tiêu đề:**
   ```bash
   w -h
   ```

3. **Hiển thị thông tin ngắn gọn:**
   ```bash
   w -s
   ```

4. **Hiển thị thông tin với thời gian hoạt động của người dùng:**
   ```bash
   w -u
   ```

## Tips
- Sử dụng lệnh `w` thường xuyên để theo dõi hoạt động của người dùng trên máy chủ, đặc biệt trong môi trường đa người dùng.
- Kết hợp với các lệnh khác như `grep` để lọc thông tin cụ thể về một người dùng.
- Hãy chú ý đến thời gian hoạt động của người dùng để phát hiện các hoạt động bất thường hoặc không cần thiết.