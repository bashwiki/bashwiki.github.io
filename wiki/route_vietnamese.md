# [리눅스] Bash route 사용법

## Tổng quan
Lệnh `route` trong Bash được sử dụng để hiển thị và quản lý bảng định tuyến IP của hệ thống. Bảng định tuyến chứa thông tin về cách gửi gói tin đến các địa chỉ IP khác nhau, cho phép hệ thống xác định con đường tốt nhất để truyền dữ liệu. Lệnh này rất hữu ích cho các kỹ sư mạng và lập trình viên khi cần kiểm tra hoặc thay đổi cấu hình mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `route` như sau:

```
route [OPTION] [ARGUMENTS]
```

Một số tùy chọn phổ biến của lệnh `route` bao gồm:

- `-n`: Hiển thị địa chỉ IP thay vì tên miền, giúp tăng tốc độ hiển thị.
- `add`: Thêm một tuyến đường mới vào bảng định tuyến.
- `del`: Xóa một tuyến đường khỏi bảng định tuyến.
- `-e`: Hiển thị thông tin chi tiết về bảng định tuyến.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `route`.

1. **Hiển thị bảng định tuyến hiện tại**:
   ```bash
   route -n
   ```
   Lệnh này sẽ hiển thị bảng định tuyến mà không cần phân giải tên miền, giúp bạn thấy được các địa chỉ IP và các tuyến đường hiện có.

2. **Thêm một tuyến đường mới**:
   ```bash
   route add -net 192.168.1.0/24 gw 192.168.1.1
   ```
   Lệnh này sẽ thêm một tuyến đường mới cho mạng con `192.168.1.0` với cổng đi qua là `192.168.1.1`.

## Mẹo
- Khi làm việc với lệnh `route`, hãy luôn kiểm tra bảng định tuyến sau khi thực hiện các thay đổi để đảm bảo rằng các tuyến đường đã được thêm hoặc xóa thành công.
- Sử dụng tùy chọn `-n` để tăng tốc độ hiển thị bảng định tuyến, đặc biệt là trên các hệ thống có nhiều tuyến đường.
- Nếu bạn không chắc chắn về cú pháp hoặc các tùy chọn, hãy sử dụng lệnh `man route` để xem tài liệu hướng dẫn chi tiết về lệnh này.