# [Linux] Bash trap cách sử dụng: Quản lý tín hiệu trong Bash

## Overview
Lệnh `trap` trong Bash được sử dụng để xử lý tín hiệu và sự kiện trong các script. Nó cho phép bạn chỉ định các hành động cụ thể khi một tín hiệu nhất định được nhận, giúp quản lý các tình huống như dừng hoặc thoát khỏi script một cách an toàn.

## Usage
Cú pháp cơ bản của lệnh `trap` như sau:
```bash
trap [options] [arguments]
```

## Common Options
- `SIGINT`: Tín hiệu ngắt (Ctrl+C).
- `SIGTERM`: Tín hiệu yêu cầu dừng chương trình.
- `EXIT`: Hành động sẽ được thực hiện khi script kết thúc.
- `ERR`: Hành động sẽ được thực hiện khi có lỗi xảy ra.

## Common Examples
1. **Bắt tín hiệu ngắt (Ctrl+C)**:
   ```bash
   trap 'echo "Script bị ngắt"; exit' SIGINT
   ```
   Trong ví dụ này, khi người dùng nhấn Ctrl+C, thông báo sẽ được in ra và script sẽ thoát.

2. **Thực hiện hành động khi script kết thúc**:
   ```bash
   trap 'echo "Script đã kết thúc"' EXIT
   ```
   Hành động này sẽ in ra thông báo khi script hoàn tất.

3. **Xử lý lỗi**:
   ```bash
   trap 'echo "Có lỗi xảy ra"; exit 1' ERR
   ```
   Nếu có lỗi xảy ra trong script, thông báo sẽ được in ra và script sẽ thoát với mã lỗi 1.

4. **Bắt nhiều tín hiệu**:
   ```bash
   trap 'echo "Đang thoát"; exit' SIGINT SIGTERM
   ```
   Trong trường hợp này, cả hai tín hiệu ngắt và yêu cầu dừng sẽ kích hoạt cùng một hành động.

## Tips
- Sử dụng `trap` để đảm bảo rằng tài nguyên được giải phóng đúng cách khi script kết thúc.
- Đặt lệnh `trap` ở đầu script để đảm bảo rằng các tín hiệu được xử lý ngay từ đầu.
- Kiểm tra các tín hiệu mà script của bạn có thể nhận để xử lý chúng một cách hiệu quả.