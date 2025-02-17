# [Linux] Bash cron cách sử dụng: Tự động hóa tác vụ theo lịch

## Overview
Lệnh `cron` trong Bash được sử dụng để lên lịch thực hiện các tác vụ tự động trên hệ thống Linux. Nó cho phép người dùng định nghĩa các lệnh hoặc script sẽ được chạy vào những thời điểm cụ thể, giúp tiết kiệm thời gian và công sức cho các công việc lặp đi lặp lại.

## Usage
Cú pháp cơ bản của lệnh `cron` như sau:
```bash
crontab [options] [file]
```

## Common Options
- `-e`: Chỉnh sửa crontab của người dùng hiện tại.
- `-l`: Liệt kê các tác vụ đã được lên lịch trong crontab.
- `-r`: Xóa crontab của người dùng hiện tại.
- `-i`: Xác nhận trước khi xóa crontab.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng `cron`:

1. **Chạy script mỗi ngày lúc 2 giờ sáng:**
   ```bash
   0 2 * * * /path/to/script.sh
   ```

2. **Chạy lệnh `backup` mỗi thứ Hai lúc 3 giờ chiều:**
   ```bash
   0 15 * * 1 /usr/bin/backup
   ```

3. **Chạy một lệnh mỗi 15 phút:**
   ```bash
   */15 * * * * /usr/bin/some_command
   ```

4. **Chạy script vào ngày 1 hàng tháng lúc 5 giờ chiều:**
   ```bash
   0 17 1 * * /path/to/monthly_script.sh
   ```

## Tips
- Sử dụng `crontab -l` để kiểm tra các tác vụ đã được lên lịch trước khi thêm mới.
- Đảm bảo rằng đường dẫn đến script hoặc lệnh là chính xác và có quyền thực thi.
- Ghi lại đầu ra của lệnh vào một file log để dễ dàng theo dõi và xử lý lỗi:
  ```bash
  0 2 * * * /path/to/script.sh >> /path/to/logfile.log 2>&1
  ```