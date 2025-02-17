# [Linux] Bash ethtool Cách sử dụng: Kiểm tra và cấu hình thiết bị mạng

## Tổng quan
Lệnh `ethtool` được sử dụng để kiểm tra và cấu hình các thông số của thiết bị mạng Ethernet trên hệ thống Linux. Nó cho phép người dùng xem thông tin chi tiết về card mạng, bao gồm tốc độ kết nối, trạng thái, và các tùy chọn cấu hình khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ethtool` như sau:
```bash
ethtool [tùy chọn] [tham số]
```

## Các tùy chọn phổ biến
- `-s`: Cấu hình các tham số của card mạng.
- `-i`: Hiển thị thông tin về driver của card mạng.
- `-p`: Nháy đèn LED của card mạng để xác định vị trí.
- `-a`: Hiển thị trạng thái tự động điều chỉnh (auto-negotiation).
- `-t`: Thực hiện kiểm tra phần cứng trên card mạng.

## Ví dụ phổ biến
- Xem thông tin chi tiết về card mạng:
```bash
ethtool eth0
```

- Kiểm tra trạng thái tự động điều chỉnh:
```bash
ethtool -a eth0
```

- Hiển thị thông tin driver của card mạng:
```bash
ethtool -i eth0
```

- Nháy đèn LED của card mạng để xác định vị trí:
```bash
ethtool -p eth0
```

- Cấu hình tốc độ và chế độ full duplex cho card mạng:
```bash
ethtool -s eth0 speed 100 duplex full
```

## Mẹo
- Luôn kiểm tra thông tin card mạng trước khi thực hiện cấu hình để tránh lỗi.
- Sử dụng lệnh `man ethtool` để xem tài liệu hướng dẫn chi tiết về các tùy chọn và tham số.
- Đảm bảo rằng bạn có quyền truy cập root hoặc sudo để thực hiện các thay đổi cấu hình trên card mạng.