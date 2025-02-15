# [리눅스] Bash arp 사용법

## Tổng quan
Lệnh `arp` trong Bash được sử dụng để quản lý bảng ARP (Address Resolution Protocol) trên hệ thống. Bảng ARP lưu trữ các địa chỉ IP và địa chỉ MAC tương ứng, cho phép các thiết bị trong mạng nội bộ giao tiếp với nhau. Lệnh này chủ yếu được sử dụng để xem, thêm, hoặc xóa các mục trong bảng ARP, giúp quản lý kết nối mạng hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `arp` như sau:

```bash
arp [options] [hostname]
```

### Các tùy chọn phổ biến:
- `-a`: Hiển thị tất cả các mục trong bảng ARP.
- `-d hostname`: Xóa mục ARP cho hostname cụ thể.
- `-s hostname hw_addr`: Thêm một mục ARP mới với hostname và địa chỉ MAC cụ thể.

## Ví dụ
### Ví dụ 1: Hiển thị bảng ARP
Để xem tất cả các mục trong bảng ARP, bạn có thể sử dụng lệnh sau:

```bash
arp -a
```

Lệnh này sẽ hiển thị danh sách các địa chỉ IP và địa chỉ MAC tương ứng mà hệ thống đã lưu trữ.

### Ví dụ 2: Thêm một mục ARP
Nếu bạn muốn thêm một mục ARP mới, bạn có thể sử dụng lệnh sau:

```bash
arp -s 192.168.1.10 00:1A:2B:3C:4D:5E
```

Lệnh này sẽ thêm một mục vào bảng ARP, liên kết địa chỉ IP `192.168.1.10` với địa chỉ MAC `00:1A:2B:3C:4D:5E`.

## Mẹo
- Hãy chắc chắn rằng bạn có quyền truy cập đủ để thực hiện các thay đổi trong bảng ARP, vì một số lệnh yêu cầu quyền quản trị.
- Kiểm tra định kỳ bảng ARP của bạn để đảm bảo rằng không có mục nào lỗi thời hoặc không chính xác, điều này có thể gây ra sự cố kết nối mạng.
- Sử dụng lệnh `arp -d` để xóa các mục không cần thiết, giúp giữ cho bảng ARP của bạn gọn gàng và hiệu quả hơn.