# [리눅스] Bash ip 사용법

## Tổng Quan
Lệnh `ip` trong Bash là một công cụ mạnh mẽ dùng để quản lý các cấu hình mạng trên hệ thống Linux. Nó cho phép người dùng thực hiện các tác vụ như xem, thêm, sửa đổi và xóa các giao diện mạng, địa chỉ IP, và các quy tắc định tuyến. Lệnh này được coi là một phần của bộ công cụ `iproute2`, thay thế cho các lệnh cũ như `ifconfig` và `route`.

## Cách Sử Dụng
Cú pháp cơ bản của lệnh `ip` như sau:

```
ip [OPTIONS] OBJECT {COMMAND | help}
```

Trong đó:
- `OPTIONS`: Các tùy chọn bổ sung cho lệnh.
- `OBJECT`: Đối tượng mà bạn muốn thao tác, ví dụ như `link`, `addr`, `route`, v.v.
- `COMMAND`: Lệnh cụ thể mà bạn muốn thực hiện trên đối tượng đó.

### Một số tùy chọn phổ biến:
- `link`: Quản lý các giao diện mạng.
- `addr`: Quản lý địa chỉ IP.
- `route`: Quản lý bảng định tuyến.

## Ví Dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `ip`.

### Ví dụ 1: Xem thông tin giao diện mạng
Để xem thông tin chi tiết về các giao diện mạng trên hệ thống, bạn có thể sử dụng lệnh sau:

```bash
ip link show
```

Lệnh này sẽ hiển thị danh sách các giao diện mạng cùng với trạng thái của chúng (up/down).

### Ví dụ 2: Thêm địa chỉ IP vào giao diện
Để thêm một địa chỉ IP mới vào một giao diện mạng, bạn có thể sử dụng lệnh sau:

```bash
ip addr add 192.168.1.100/24 dev eth0
```

Lệnh này sẽ thêm địa chỉ IP `192.168.1.100` với mặt nạ mạng `/24` vào giao diện `eth0`.

## Mẹo
- Sử dụng lệnh `ip help` để xem danh sách đầy đủ các đối tượng và lệnh có sẵn.
- Để tránh nhầm lẫn, hãy luôn kiểm tra trạng thái của các giao diện mạng sau khi thực hiện các thay đổi bằng cách sử dụng `ip link show`.
- Khi làm việc với các địa chỉ IP và bảng định tuyến, hãy cẩn thận với các thay đổi có thể ảnh hưởng đến kết nối mạng của bạn.