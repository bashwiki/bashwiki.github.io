# [Linux] Bash shutdown cách sử dụng: Tắt máy tính hoặc khởi động lại hệ thống

## Tổng quan
Lệnh `shutdown` trong Bash được sử dụng để tắt máy tính hoặc khởi động lại hệ thống một cách an toàn. Nó cho phép người dùng lên lịch tắt máy hoặc khởi động lại, đồng thời thông báo cho người dùng khác về việc này.

## Cách sử dụng
Cú pháp cơ bản của lệnh là:

```bash
shutdown [options] [arguments]
```

## Các tùy chọn phổ biến
- `-h` hoặc `--halt`: Tắt máy tính.
- `-r` hoặc `--reboot`: Khởi động lại máy tính.
- `-P` hoặc `--poweroff`: Tắt máy và ngắt nguồn.
- `now`: Thực hiện lệnh ngay lập tức.
- `+m`: Tắt máy sau `m` phút (ví dụ: `+5` để tắt sau 5 phút).
- `hh:mm`: Thời gian cụ thể để tắt máy (theo định dạng 24 giờ).

## Ví dụ thường gặp
1. **Tắt máy ngay lập tức:**
   ```bash
   shutdown now
   ```

2. **Khởi động lại máy tính:**
   ```bash
   shutdown -r now
   ```

3. **Tắt máy sau 10 phút:**
   ```bash
   shutdown +10
   ```

4. **Tắt máy vào lúc 22:30:**
   ```bash
   shutdown 22:30
   ```

5. **Tắt máy và ngắt nguồn:**
   ```bash
   shutdown -P now
   ```

## Mẹo
- Luôn thông báo cho người dùng khác trước khi tắt máy để tránh mất dữ liệu.
- Sử dụng tùy chọn `-h` hoặc `-r` để đảm bảo rằng hệ thống sẽ tắt hoặc khởi động lại một cách an toàn.
- Kiểm tra các tiến trình đang chạy trước khi tắt máy để đảm bảo không có công việc quan trọng bị gián đoạn.