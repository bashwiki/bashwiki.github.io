# [Linux] Bash arp Cách sử dụng: Quản lý bảng ARP

## Tổng quan
Lệnh `arp` được sử dụng để quản lý bảng ARP (Address Resolution Protocol) trên hệ thống. Bảng ARP lưu trữ các địa chỉ IP và địa chỉ MAC tương ứng, giúp thiết bị trong mạng có thể giao tiếp với nhau.

## Cách sử dụng
Cú pháp cơ bản của lệnh arp như sau:
```
arp [options] [arguments]
```

## Các tùy chọn phổ biến
- `-a`: Hiển thị tất cả các mục trong bảng ARP.
- `-d`: Xóa một mục khỏi bảng ARP.
- `-s`: Thêm một mục mới vào bảng ARP.
- `-n`: Hiển thị địa chỉ IP mà không cần phân giải tên miền.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh arp:

1. **Hiển thị tất cả các mục trong bảng ARP:**
   ```bash
   arp -a
   ```

2. **Xóa một mục khỏi bảng ARP:**
   ```bash
   arp -d 192.168.1.10
   ```

3. **Thêm một mục mới vào bảng ARP:**
   ```bash
   arp -s 192.168.1.20 00:1A:2B:3C:4D:5E
   ```

4. **Hiển thị địa chỉ IP mà không phân giải tên miền:**
   ```bash
   arp -n
   ```

## Mẹo
- Hãy chắc chắn rằng bạn có quyền quản trị khi sử dụng các tùy chọn xóa hoặc thêm mục vào bảng ARP.
- Sử dụng lệnh `arp -a` thường xuyên để kiểm tra các mục trong bảng ARP, giúp phát hiện các vấn đề mạng kịp thời.
- Nếu bạn gặp phải vấn đề kết nối mạng, hãy thử xóa các mục cũ trong bảng ARP và để hệ thống tự động cập nhật lại.