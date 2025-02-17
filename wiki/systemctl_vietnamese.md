# [Linux] Bash systemctl cách sử dụng: Quản lý dịch vụ hệ thống

## Tổng quan
Lệnh `systemctl` là một công cụ mạnh mẽ trong hệ thống Linux dùng để quản lý dịch vụ và trạng thái của hệ thống. Nó cho phép người dùng khởi động, dừng, khởi động lại và kiểm tra trạng thái của các dịch vụ đang chạy trên hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `systemctl` như sau:
```
systemctl [options] [arguments]
```

## Các tùy chọn phổ biến
- `start`: Khởi động một dịch vụ.
- `stop`: Dừng một dịch vụ.
- `restart`: Khởi động lại một dịch vụ.
- `status`: Kiểm tra trạng thái của một dịch vụ.
- `enable`: Bật tự động khởi động dịch vụ khi hệ thống khởi động.
- `disable`: Tắt tự động khởi động dịch vụ khi hệ thống khởi động.

## Ví dụ phổ biến
- Khởi động một dịch vụ:
  ```bash
  systemctl start tên_dịch_vụ
  ```
  
- Dừng một dịch vụ:
  ```bash
  systemctl stop tên_dịch_vụ
  ```
  
- Khởi động lại một dịch vụ:
  ```bash
  systemctl restart tên_dịch_vụ
  ```
  
- Kiểm tra trạng thái của một dịch vụ:
  ```bash
  systemctl status tên_dịch_vụ
  ```
  
- Bật tự động khởi động dịch vụ:
  ```bash
  systemctl enable tên_dịch_vụ
  ```
  
- Tắt tự động khởi động dịch vụ:
  ```bash
  systemctl disable tên_dịch_vụ
  ```

## Mẹo
- Luôn kiểm tra trạng thái của dịch vụ sau khi thực hiện các thay đổi để đảm bảo rằng chúng hoạt động như mong đợi.
- Sử dụng `systemctl list-units --type=service` để xem danh sách tất cả các dịch vụ đang chạy trên hệ thống.
- Khi cần thêm thông tin chi tiết về một dịch vụ, bạn có thể sử dụng lệnh `journalctl -u tên_dịch_vụ` để xem nhật ký liên quan.