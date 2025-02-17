# [Linux] Bash journalctl Cách sử dụng: Xem nhật ký hệ thống

## Tổng quan
Lệnh `journalctl` được sử dụng để truy cập và quản lý nhật ký hệ thống trên các hệ thống sử dụng systemd. Nó cho phép người dùng xem các thông tin ghi lại từ các dịch vụ và ứng dụng, giúp theo dõi hoạt động và khắc phục sự cố.

## Cách sử dụng
Cú pháp cơ bản của lệnh `journalctl` như sau:

```bash
journalctl [options] [arguments]
```

## Các tùy chọn phổ biến
- `-b`: Hiển thị nhật ký từ phiên khởi động hiện tại.
- `-f`: Theo dõi nhật ký theo thời gian thực (tương tự như lệnh `tail -f`).
- `--since`: Hiển thị nhật ký từ một thời điểm cụ thể.
- `--until`: Hiển thị nhật ký cho đến một thời điểm cụ thể.
- `-u [service]`: Hiển thị nhật ký cho một dịch vụ cụ thể.

## Ví dụ thường gặp
- Hiển thị tất cả nhật ký:
  ```bash
  journalctl
  ```

- Hiển thị nhật ký từ phiên khởi động hiện tại:
  ```bash
  journalctl -b
  ```

- Theo dõi nhật ký theo thời gian thực:
  ```bash
  journalctl -f
  ```

- Hiển thị nhật ký từ một thời điểm cụ thể:
  ```bash
  journalctl --since "2023-10-01 10:00:00"
  ```

- Hiển thị nhật ký cho một dịch vụ cụ thể:
  ```bash
  journalctl -u ssh.service
  ```

## Mẹo
- Sử dụng tùy chọn `-p` để lọc nhật ký theo mức độ nghiêm trọng (ví dụ: `-p err` chỉ hiển thị các lỗi).
- Kết hợp `--since` và `--until` để xem nhật ký trong một khoảng thời gian cụ thể.
- Xuất nhật ký ra file bằng cách sử dụng `journalctl > file.log` để lưu lại thông tin cho việc phân tích sau này.