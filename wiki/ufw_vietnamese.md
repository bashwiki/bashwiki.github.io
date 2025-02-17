# [Linux] Bash ufw Cách sử dụng: Quản lý tường lửa dễ dàng

## Tổng quan
Lệnh `ufw` (Uncomplicated Firewall) là một công cụ quản lý tường lửa đơn giản trên hệ điều hành Linux. Nó giúp người dùng thiết lập và quản lý các quy tắc tường lửa một cách dễ dàng, bảo vệ hệ thống khỏi các mối đe dọa từ mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ufw` như sau:
```
ufw [options] [arguments]
```

## Các tùy chọn phổ biến
- `enable`: Bật tường lửa.
- `disable`: Tắt tường lửa.
- `status`: Hiển thị trạng thái hiện tại của tường lửa.
- `allow [port]`: Cho phép lưu lượng truy cập qua cổng chỉ định.
- `deny [port]`: Từ chối lưu lượng truy cập qua cổng chỉ định.
- `delete [rule]`: Xóa một quy tắc tường lửa đã được thiết lập.

## Ví dụ thường gặp
- Bật tường lửa:
  ```bash
  ufw enable
  ```

- Tắt tường lửa:
  ```bash
  ufw disable
  ```

- Kiểm tra trạng thái tường lửa:
  ```bash
  ufw status
  ```

- Cho phép lưu lượng truy cập qua cổng 80 (HTTP):
  ```bash
  ufw allow 80
  ```

- Từ chối lưu lượng truy cập qua cổng 22 (SSH):
  ```bash
  ufw deny 22
  ```

- Xóa quy tắc cho phép cổng 80:
  ```bash
  ufw delete allow 80
  ```

## Mẹo
- Luôn kiểm tra trạng thái tường lửa sau khi thay đổi quy tắc để đảm bảo rằng các quy tắc đã được áp dụng đúng cách.
- Sử dụng `ufw status verbose` để có thêm thông tin chi tiết về các quy tắc đang hoạt động.
- Đảm bảo rằng bạn không chặn các cổng cần thiết cho việc truy cập từ xa, đặc biệt là cổng SSH, nếu bạn quản lý máy chủ từ xa.