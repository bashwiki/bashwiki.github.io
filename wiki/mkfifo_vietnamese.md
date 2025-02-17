# [Linux] Bash mkfifo Cách sử dụng: Tạo các FIFO (kênh) trong hệ thống

## Tổng quan
Lệnh `mkfifo` trong Bash được sử dụng để tạo các tệp FIFO (First In, First Out), còn được gọi là kênh. Các tệp này cho phép giao tiếp giữa các tiến trình trong hệ thống, cho phép một tiến trình ghi dữ liệu vào kênh và một tiến trình khác đọc dữ liệu từ kênh đó.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mkfifo` như sau:

```bash
mkfifo [tùy chọn] [tên_tệp]
```

## Các tùy chọn phổ biến
- `-m, --mode`: Đặt quyền truy cập cho tệp FIFO được tạo.
- `--help`: Hiển thị thông tin trợ giúp về lệnh.
- `--version`: Hiển thị phiên bản của lệnh.

## Ví dụ thông dụng
Dưới đây là một số ví dụ về cách sử dụng lệnh `mkfifo`:

1. Tạo một tệp FIFO đơn giản:
   ```bash
   mkfifo myfifo
   ```

2. Tạo một tệp FIFO với quyền truy cập cụ thể:
   ```bash
   mkfifo -m 644 myfifo
   ```

3. Tạo nhiều tệp FIFO cùng một lúc:
   ```bash
   mkfifo fifo1 fifo2 fifo3
   ```

4. Sử dụng FIFO để giao tiếp giữa hai tiến trình:
   ```bash
   # Trong một terminal, ghi vào FIFO
   echo "Hello, FIFO!" > myfifo

   # Trong một terminal khác, đọc từ FIFO
   cat myfifo
   ```

## Mẹo
- Đảm bảo rằng bạn đã mở tệp FIFO để đọc trước khi ghi vào nó, vì nếu không, lệnh ghi sẽ bị treo cho đến khi có một tiến trình đọc.
- Sử dụng quyền truy cập thích hợp cho tệp FIFO để đảm bảo rằng chỉ những tiến trình cần thiết mới có thể truy cập vào nó.
- Kiểm tra xem tệp FIFO đã tồn tại hay chưa trước khi tạo để tránh lỗi.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về lệnh `mkfifo` và cách sử dụng nó trong Bash!