# [Linux] Bash pidof: Xác định PID của tiến trình

## Overview
Lệnh `pidof` được sử dụng để tìm kiếm và xác định Process ID (PID) của một hoặc nhiều tiến trình đang chạy trên hệ thống. Nó trả về các PID tương ứng với tên tiến trình mà bạn chỉ định.

## Usage
Cú pháp cơ bản của lệnh `pidof` như sau:
```
pidof [options] [arguments]
```

## Common Options
- `-o, --exclude`: Loại trừ một hoặc nhiều PID khỏi kết quả.
- `-s, --single`: Chỉ trả về PID đầu tiên tìm thấy.
- `-h, --help`: Hiển thị hướng dẫn sử dụng lệnh.
- `-V, --version`: Hiển thị thông tin phiên bản của lệnh.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `pidof`:

1. **Tìm PID của một tiến trình cụ thể**:
   ```bash
   pidof firefox
   ```

2. **Tìm PID của nhiều tiến trình**:
   ```bash
   pidof sshd apache2
   ```

3. **Loại trừ một PID khỏi kết quả**:
   ```bash
   pidof -o 1234 firefox
   ```

4. **Chỉ lấy PID đầu tiên của tiến trình**:
   ```bash
   pidof -s firefox
   ```

## Tips
- Sử dụng `pidof` trong các script để tự động hóa việc theo dõi và quản lý tiến trình.
- Kết hợp `pidof` với các lệnh khác như `kill` để dễ dàng dừng một tiến trình cụ thể.
- Kiểm tra xem tiến trình có đang chạy hay không bằng cách sử dụng `pidof` trước khi thực hiện các thao tác khác.