# [Linux] Bash tại at: [lên lịch thực thi lệnh]

## Overview
Lệnh `at` trong Bash cho phép người dùng lên lịch thực thi các lệnh hoặc tập lệnh vào một thời điểm cụ thể trong tương lai. Đây là một công cụ hữu ích cho việc tự động hóa các tác vụ mà bạn muốn thực hiện sau này.

## Usage
Cú pháp cơ bản của lệnh `at` như sau:
```bash
at [options] [time]
```

## Common Options
- `-f FILE`: Đọc lệnh từ tệp FILE thay vì từ stdin.
- `-m`: Gửi email thông báo khi lệnh đã được thực thi.
- `-q QUEUE`: Chỉ định hàng đợi để thực thi lệnh.
- `-v`: Hiển thị thời gian khi lệnh sẽ được thực thi.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `at`:

1. **Lên lịch thực thi một lệnh vào lúc 3 giờ chiều hôm nay:**
   ```bash
   echo "echo 'Hello, World!'" | at 15:00
   ```

2. **Lên lịch thực thi một tập lệnh vào ngày mai lúc 10 giờ sáng:**
   ```bash
   at 10:00 tomorrow -f /path/to/script.sh
   ```

3. **Lên lịch gửi một email vào lúc 5 giờ chiều:**
   ```bash
   echo "mail -s 'Reminder' user@example.com <<< 'This is a reminder!'" | at 17:00
   ```

4. **Lên lịch một lệnh để chạy sau 1 giờ:**
   ```bash
   echo "shutdown now" | at now + 1 hour
   ```

## Tips
- Đảm bảo rằng dịch vụ `atd` đang chạy trên hệ thống của bạn để lệnh `at` hoạt động.
- Kiểm tra danh sách các lệnh đã lên lịch bằng cách sử dụng lệnh `atq`.
- Hủy lệnh đã lên lịch bằng cách sử dụng lệnh `atrm [job number]`, trong đó `[job number]` là số của lệnh trong danh sách `atq`.