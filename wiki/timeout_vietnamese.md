# [Linux] Bash timeout cách sử dụng: Giới hạn thời gian thực thi lệnh

## Tổng quan
Lệnh `timeout` trong Bash cho phép bạn giới hạn thời gian thực thi của một lệnh. Nếu lệnh không hoàn thành trong khoảng thời gian đã chỉ định, `timeout` sẽ tự động dừng lệnh đó.

## Cách sử dụng
Cú pháp cơ bản của lệnh `timeout` như sau:

```bash
timeout [options] [thời gian] [lệnh] [arguments]
```

## Các tùy chọn phổ biến
- `-k, --kill-after=DURATION`: Thời gian sau khi lệnh bị dừng, lệnh sẽ bị giết.
- `-s, --signal=SIGNAL`: Tín hiệu sẽ được gửi đến lệnh khi thời gian hết.
- `--preserve-status`: Giữ lại mã trạng thái của lệnh gốc.

## Ví dụ thường gặp
1. **Giới hạn thời gian thực thi lệnh `sleep` trong 5 giây:**
   ```bash
   timeout 5s sleep 10
   ```
   Lệnh `sleep 10` sẽ bị dừng sau 5 giây.

2. **Giới hạn thời gian và gửi tín hiệu `SIGKILL` sau 10 giây:**
   ```bash
   timeout -s KILL 10s sleep 30
   ```
   Lệnh `sleep 30` sẽ bị giết sau 10 giây.

3. **Sử dụng tùy chọn `--preserve-status`:**
   ```bash
   timeout --preserve-status 5s ls /nonexistent
   ```
   Nếu lệnh `ls` không tìm thấy thư mục, mã trạng thái sẽ được giữ lại.

## Mẹo
- Sử dụng `timeout` để tránh các lệnh treo hoặc chạy quá lâu, đặc biệt trong các kịch bản tự động.
- Kết hợp `timeout` với các lệnh khác trong một chuỗi để kiểm soát thời gian thực thi của nhiều lệnh.
- Thử nghiệm với các tín hiệu khác nhau để tìm ra tín hiệu phù hợp nhất cho lệnh của bạn.