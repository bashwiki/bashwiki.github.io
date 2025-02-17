# [Linux] Bash iptables Cách sử dụng: Quản lý tường lửa

## Tổng quan
`iptables` là một công cụ dòng lệnh trong Linux được sử dụng để cấu hình, quản lý và kiểm soát tường lửa của hệ thống. Nó cho phép người dùng định nghĩa các quy tắc để cho phép hoặc từ chối lưu lượng mạng dựa trên nhiều tiêu chí khác nhau.

## Cách sử dụng
Cú pháp cơ bản của lệnh `iptables` như sau:

```
iptables [options] [arguments]
```

## Các tùy chọn phổ biến
- `-A`: Thêm một quy tắc vào cuối chuỗi.
- `-D`: Xóa một quy tắc khỏi chuỗi.
- `-L`: Liệt kê các quy tắc hiện có trong chuỗi.
- `-F`: Xóa tất cả các quy tắc trong chuỗi.
- `-P`: Đặt chính sách mặc định cho chuỗi.
- `-I`: Chèn một quy tắc vào đầu chuỗi.

## Ví dụ thường gặp
1. **Liệt kê các quy tắc hiện có:**
   ```bash
   iptables -L
   ```

2. **Thêm quy tắc cho phép lưu lượng HTTP:**
   ```bash
   iptables -A INPUT -p tcp --dport 80 -j ACCEPT
   ```

3. **Xóa quy tắc cho phép lưu lượng SSH:**
   ```bash
   iptables -D INPUT -p tcp --dport 22 -j ACCEPT
   ```

4. **Đặt chính sách mặc định từ chối tất cả lưu lượng:**
   ```bash
   iptables -P INPUT DROP
   ```

5. **Xóa tất cả các quy tắc:**
   ```bash
   iptables -F
   ```

## Mẹo
- **Sao lưu cấu hình:** Trước khi thay đổi các quy tắc, hãy sao lưu cấu hình hiện tại bằng lệnh `iptables-save > iptables-backup.txt`.
- **Kiểm tra quy tắc:** Sử dụng `iptables -L -n -v` để xem chi tiết về các quy tắc và lưu lượng đã được xử lý.
- **Cẩn thận với chính sách mặc định:** Đảm bảo rằng bạn không vô tình chặn lưu lượng quan trọng khi thay đổi chính sách mặc định.
- **Sử dụng script:** Nếu bạn có nhiều quy tắc, hãy xem xét việc viết một script để tự động hóa quá trình cấu hình.