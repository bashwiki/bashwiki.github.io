# [Linux] Bash hash cách sử dụng: Quản lý cache của các lệnh

## Overview
Lệnh `hash` trong Bash được sử dụng để quản lý cache của các lệnh đã được thực thi. Khi bạn chạy một lệnh, Bash lưu trữ vị trí của nó trong bộ nhớ cache để tăng tốc độ thực thi cho các lần gọi sau. Lệnh này cho phép bạn xem và xóa các mục trong cache này.

## Usage
Cú pháp cơ bản của lệnh `hash` như sau:
```bash
hash [options] [arguments]
```

## Common Options
- `-r`: Xóa toàn bộ cache của các lệnh đã lưu.
- `-p`: Chỉ định một đường dẫn cụ thể cho lệnh mà bạn muốn lưu vào cache.
- `-l`: Liệt kê tất cả các lệnh đã được lưu trong cache.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `hash`:

1. **Liệt kê các lệnh đã lưu trong cache**:
   ```bash
   hash
   ```

2. **Xóa toàn bộ cache**:
   ```bash
   hash -r
   ```

3. **Lưu một lệnh cụ thể vào cache với đường dẫn**:
   ```bash
   hash -p /usr/local/bin/mycommand mycommand
   ```

4. **Liệt kê các lệnh đã lưu cùng với đường dẫn**:
   ```bash
   hash -l
   ```

## Tips
- Sử dụng `hash` để kiểm tra xem lệnh nào đã được lưu trong cache, điều này giúp bạn xác định xem có cần phải cập nhật đường dẫn hay không.
- Nếu bạn thay đổi vị trí của một lệnh, hãy nhớ sử dụng `hash -r` để làm mới cache, tránh việc gọi lệnh từ vị trí cũ.
- Lệnh `hash` rất hữu ích khi làm việc với nhiều phiên bản của một lệnh, giúp bạn quản lý dễ dàng hơn.