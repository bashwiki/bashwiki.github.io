# [Linux] Bash users: Liệt kê người dùng hệ thống

## Overview
Lệnh `users` trong Bash được sử dụng để hiển thị danh sách tên người dùng đang đăng nhập vào hệ thống. Nó cung cấp thông tin nhanh chóng về những người dùng hiện đang hoạt động.

## Usage
Cú pháp cơ bản của lệnh `users` như sau:
```
users [options] [arguments]
```

## Common Options
- `-n`: Hiển thị số lượng người dùng đang đăng nhập.
- `-r`: Hiển thị tên người dùng theo định dạng rút gọn.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `users`:

1. Hiển thị danh sách người dùng đang đăng nhập:
   ```bash
   users
   ```

2. Hiển thị số lượng người dùng đang đăng nhập:
   ```bash
   users -n
   ```

3. Hiển thị tên người dùng theo định dạng rút gọn:
   ```bash
   users -r
   ```

## Tips
- Sử dụng lệnh `who` để có thêm thông tin chi tiết về người dùng, chẳng hạn như thời gian đăng nhập và địa chỉ IP.
- Kết hợp lệnh `users` với các lệnh khác như `wc -l` để đếm số lượng người dùng đang đăng nhập:
  ```bash
  users | wc -w
  ```
- Lệnh `users` rất hữu ích trong các script để theo dõi hoạt động của người dùng trên hệ thống.