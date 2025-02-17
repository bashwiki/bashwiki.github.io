# [Linux] Bash route sử dụng: Quản lý bảng định tuyến mạng

## Tổng quan
Lệnh `route` được sử dụng để hiển thị và quản lý bảng định tuyến mạng trên hệ thống Linux. Nó cho phép người dùng xem và thay đổi các tuyến đường mà hệ thống sử dụng để gửi dữ liệu đến các địa chỉ IP khác nhau.

## Cách sử dụng
Cú pháp cơ bản của lệnh `route` như sau:
```
route [options] [arguments]
```

## Các tùy chọn phổ biến
- `-n`: Hiển thị địa chỉ IP thay vì tên miền.
- `add`: Thêm một tuyến đường mới vào bảng định tuyến.
- `del`: Xóa một tuyến đường khỏi bảng định tuyến.
- `-e`: Hiển thị bảng định tuyến chi tiết.

## Ví dụ thường gặp
1. Hiển thị bảng định tuyến hiện tại:
   ```bash
   route -n
   ```

2. Thêm một tuyến đường mới:
   ```bash
   route add -net 192.168.1.0 netmask 255.255.255.0 gw 192.168.1.1
   ```

3. Xóa một tuyến đường:
   ```bash
   route del -net 192.168.1.0
   ```

4. Hiển thị bảng định tuyến chi tiết:
   ```bash
   route -e
   ```

## Mẹo
- Sử dụng tùy chọn `-n` để tăng tốc độ hiển thị bảng định tuyến bằng cách bỏ qua việc phân giải tên miền.
- Kiểm tra thường xuyên bảng định tuyến của bạn để đảm bảo rằng các tuyến đường vẫn chính xác và hiệu quả.
- Khi thêm hoặc xóa tuyến đường, hãy chắc chắn rằng bạn có quyền truy cập cần thiết (có thể cần quyền root).