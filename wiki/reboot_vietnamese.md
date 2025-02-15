# [리눅스] Bash reboot 사용법

## Tổng quan
Lệnh `reboot` trong Bash được sử dụng để khởi động lại hệ thống Linux. Đây là một lệnh quan trọng cho các kỹ sư và nhà phát triển, cho phép họ khôi phục lại trạng thái của hệ thống một cách nhanh chóng và hiệu quả. Khi lệnh này được thực thi, tất cả các tiến trình đang chạy sẽ bị dừng lại và hệ thống sẽ khởi động lại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `reboot` như sau:

```bash
reboot [OPTIONS]
```

### Các tùy chọn phổ biến:
- `-f` hoặc `--force`: Bỏ qua các tiến trình dừng lại và khởi động lại ngay lập tức.
- `-p` hoặc `--poweroff`: Tắt máy thay vì khởi động lại (tùy chọn này có thể không khả dụng trên một số hệ thống).
- `-h` hoặc `--halt`: Dừng hệ thống mà không khởi động lại.

## Ví dụ
### Ví dụ 1: Khởi động lại hệ thống
Để khởi động lại hệ thống một cách bình thường, bạn có thể sử dụng lệnh sau:

```bash
sudo reboot
```

### Ví dụ 2: Khởi động lại ngay lập tức
Nếu bạn muốn khởi động lại ngay lập tức mà không chờ các tiến trình dừng lại, bạn có thể sử dụng tùy chọn `-f`:

```bash
sudo reboot -f
```

## Mẹo
- **Lưu dữ liệu trước khi khởi động lại**: Trước khi thực hiện lệnh `reboot`, hãy chắc chắn rằng bạn đã lưu tất cả dữ liệu quan trọng để tránh mất mát thông tin.
- **Sử dụng `shutdown` trước khi khởi động lại**: Trong một số trường hợp, bạn có thể muốn sử dụng lệnh `shutdown` để thông báo cho người dùng khác về việc khởi động lại trước khi thực hiện lệnh `reboot`.
- **Kiểm tra các tiến trình đang chạy**: Trước khi khởi động lại, hãy kiểm tra các tiến trình đang chạy để đảm bảo không có công việc quan trọng nào đang bị gián đoạn.

Lệnh `reboot` là một công cụ mạnh mẽ trong quản lý hệ thống, giúp bạn duy trì và khôi phục hệ thống một cách hiệu quả.