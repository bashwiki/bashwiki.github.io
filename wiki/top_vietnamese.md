# [리눅스] Bash top 사용법

## Tổng quan
Lệnh `top` trong Bash là một công cụ giám sát hệ thống thời gian thực, cho phép người dùng theo dõi các quá trình đang chạy trên hệ thống Linux. Nó cung cấp thông tin chi tiết về việc sử dụng CPU, bộ nhớ, và các thông số khác của các tiến trình, giúp người dùng quản lý tài nguyên hệ thống một cách hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `top` là:

```bash
top [options]
```

Một số tùy chọn phổ biến của lệnh `top` bao gồm:

- `-d <seconds>`: Đặt thời gian làm mới (refresh) giữa các lần cập nhật thông tin, tính bằng giây.
- `-p <pid>`: Chỉ hiển thị thông tin cho tiến trình có ID (PID) cụ thể.
- `-u <username>`: Chỉ hiển thị các tiến trình của người dùng cụ thể.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `top`:

1. Chạy lệnh `top` đơn giản để xem tất cả các tiến trình đang chạy:

   ```bash
   top
   ```

2. Chạy lệnh `top` với thời gian làm mới là 5 giây:

   ```bash
   top -d 5
   ```

3. Chỉ hiển thị thông tin cho một tiến trình cụ thể với PID 1234:

   ```bash
   top -p 1234
   ```

## Mẹo
- Sử dụng phím `h` trong giao diện `top` để xem hướng dẫn sử dụng chi tiết và các phím tắt có sẵn.
- Bạn có thể nhấn `Shift + M` để sắp xếp các tiến trình theo mức sử dụng bộ nhớ, hoặc `Shift + P` để sắp xếp theo mức sử dụng CPU.
- Để thoát khỏi giao diện `top`, nhấn phím `q`.
- Nếu bạn muốn lưu lại thông tin từ `top`, bạn có thể sử dụng lệnh `top -b -n 1 > output.txt` để xuất kết quả ra file `output.txt`.

Hy vọng rằng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng lệnh `top` trong Bash!