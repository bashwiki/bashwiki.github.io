# [Linux] Bash crontab cách sử dụng: Quản lý tác vụ định kỳ

## Tổng quan
Lệnh `crontab` được sử dụng để quản lý các tác vụ định kỳ trên hệ thống Unix/Linux. Nó cho phép người dùng lên lịch thực hiện các lệnh hoặc script vào những thời điểm cụ thể, giúp tự động hóa các công việc thường xuyên.

## Cách sử dụng
Cú pháp cơ bản của lệnh `crontab` như sau:

```bash
crontab [options] [arguments]
```

## Các tùy chọn phổ biến
- `-e`: Mở trình soạn thảo để chỉnh sửa crontab hiện tại.
- `-l`: Hiển thị nội dung của crontab hiện tại.
- `-r`: Xóa crontab hiện tại.
- `-i`: Xác nhận trước khi xóa crontab.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng `crontab`:

1. **Mở crontab để chỉnh sửa**:
   ```bash
   crontab -e
   ```

2. **Hiển thị crontab hiện tại**:
   ```bash
   crontab -l
   ```

3. **Xóa crontab hiện tại**:
   ```bash
   crontab -r
   ```

4. **Lên lịch chạy một script mỗi ngày lúc 2 giờ sáng**:
   ```bash
   0 2 * * * /path/to/script.sh
   ```

5. **Lên lịch chạy một lệnh mỗi thứ Hai lúc 8 giờ sáng**:
   ```bash
   0 8 * * 1 /usr/bin/somecommand
   ```

## Mẹo
- **Kiểm tra log**: Để theo dõi các tác vụ đã thực hiện, bạn có thể kiểm tra log hệ thống, thường nằm ở `/var/log/syslog` hoặc `/var/log/cron`.
- **Sử dụng đường dẫn đầy đủ**: Khi lên lịch, hãy sử dụng đường dẫn đầy đủ cho các lệnh và script để tránh lỗi không tìm thấy.
- **Thêm thông báo**: Bạn có thể thêm thông báo qua email bằng cách chỉ định biến `MAILTO` trong crontab để nhận thông báo khi có lỗi xảy ra.