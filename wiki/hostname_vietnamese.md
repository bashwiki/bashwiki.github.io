# [Linux] Bash hostname cách sử dụng: [hiển thị hoặc thiết lập tên máy chủ]

## Tổng quan
Lệnh `hostname` được sử dụng để hiển thị hoặc thiết lập tên máy chủ của hệ thống. Tên máy chủ là một phần quan trọng trong việc xác định và quản lý các thiết bị trong mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `hostname` như sau:
```
hostname [options] [arguments]
```

## Tùy chọn phổ biến
- `-a`, `--alias`: Hiển thị tên bí danh của máy chủ.
- `-d`, `--domain`: Hiển thị tên miền của máy chủ.
- `-f`, `--fqdn`: Hiển thị tên miền đầy đủ (FQDN) của máy chủ.
- `-i`, `--ip-address`: Hiển thị địa chỉ IP của máy chủ.
- `-s`, `--short`: Hiển thị tên ngắn của máy chủ.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `hostname`:

1. Hiển thị tên máy chủ hiện tại:
   ```bash
   hostname
   ```

2. Hiển thị tên miền đầy đủ của máy chủ:
   ```bash
   hostname -f
   ```

3. Thiết lập tên máy chủ mới:
   ```bash
   sudo hostname new-hostname
   ```

4. Hiển thị địa chỉ IP của máy chủ:
   ```bash
   hostname -i
   ```

5. Hiển thị tên ngắn của máy chủ:
   ```bash
   hostname -s
   ```

## Mẹo
- Để thay đổi tên máy chủ một cách vĩnh viễn, bạn cần chỉnh sửa tệp cấu hình `/etc/hostname` và khởi động lại dịch vụ mạng.
- Sử dụng lệnh `hostnamectl` trên các hệ thống sử dụng systemd để quản lý tên máy chủ một cách dễ dàng hơn.
- Kiểm tra tên máy chủ thường xuyên để đảm bảo rằng nó đúng với cấu hình mạng của bạn, đặc biệt trong môi trường đa máy chủ.