# [Linux] Bash ip cách sử dụng: [quản lý cấu hình mạng]

## Overview
Lệnh `ip` trong Bash được sử dụng để quản lý và cấu hình các giao diện mạng trên hệ thống Linux. Nó cho phép người dùng xem thông tin về các giao diện mạng, cấu hình địa chỉ IP, và thực hiện nhiều tác vụ liên quan đến mạng.

## Usage
Cú pháp cơ bản của lệnh `ip` như sau:
```bash
ip [options] [arguments]
```

## Common Options
- `link`: Quản lý các giao diện mạng.
- `addr`: Hiển thị và cấu hình địa chỉ IP.
- `route`: Quản lý bảng định tuyến.
- `neigh`: Quản lý hàng xóm mạng (ARP).

## Common Examples
- Hiển thị tất cả các giao diện mạng:
```bash
ip link show
```

- Hiển thị địa chỉ IP của các giao diện mạng:
```bash
ip addr show
```

- Thêm một địa chỉ IP mới cho giao diện mạng:
```bash
ip addr add 192.168.1.100/24 dev eth0
```

- Xóa một địa chỉ IP khỏi giao diện mạng:
```bash
ip addr del 192.168.1.100/24 dev eth0
```

- Hiển thị bảng định tuyến hiện tại:
```bash
ip route show
```

## Tips
- Sử dụng `ip -h` để xem hướng dẫn và danh sách các tùy chọn có sẵn.
- Để thay đổi cấu hình mạng, bạn cần quyền truy cập root hoặc sử dụng `sudo`.
- Thường xuyên kiểm tra trạng thái giao diện mạng để đảm bảo kết nối ổn định.