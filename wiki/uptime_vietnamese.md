# [Linux] Bash uptime Cách sử dụng: Xem thời gian hoạt động của hệ thống

## Overview
Lệnh `uptime` trong Bash được sử dụng để hiển thị thời gian hoạt động của hệ thống, số lượng người dùng đang đăng nhập và tải trung bình của hệ thống trong 1, 5 và 15 phút qua. Đây là một công cụ hữu ích để theo dõi tình trạng hoạt động của máy chủ hoặc máy tính.

## Usage
Cú pháp cơ bản của lệnh `uptime` như sau:

```bash
uptime [options]
```

## Common Options
- `-p`: Hiển thị thời gian hoạt động theo định dạng dễ đọc.
- `-s`: Hiển thị thời gian khởi động của hệ thống.

## Common Examples
Dưới đây là một số ví dụ thực tế khi sử dụng lệnh `uptime`:

1. **Hiển thị thông tin cơ bản về thời gian hoạt động:**

   ```bash
   uptime
   ```

2. **Hiển thị thời gian hoạt động theo định dạng dễ đọc:**

   ```bash
   uptime -p
   ```

3. **Hiển thị thời gian khởi động của hệ thống:**

   ```bash
   uptime -s
   ```

## Tips
- Sử dụng lệnh `uptime` thường xuyên để theo dõi tình trạng của hệ thống, đặc biệt là trên các máy chủ.
- Kết hợp lệnh `uptime` với các công cụ giám sát khác để có cái nhìn tổng quan hơn về hiệu suất hệ thống.
- Nếu bạn muốn theo dõi thời gian hoạt động liên tục, hãy xem xét việc sử dụng lệnh `watch` với `uptime` để tự động làm mới thông tin.