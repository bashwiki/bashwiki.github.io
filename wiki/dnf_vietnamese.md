# [Linux] Bash dnf Cách sử dụng: Quản lý gói phần mềm

## Tổng quan
Lệnh `dnf` (Dandified YUM) là một công cụ quản lý gói phần mềm trên các hệ điều hành dựa trên RPM như Fedora, CentOS và RHEL. Nó cho phép người dùng cài đặt, cập nhật, và gỡ bỏ các gói phần mềm một cách dễ dàng và hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dnf` như sau:
```
dnf [options] [arguments]
```

## Các tùy chọn phổ biến
- `install`: Cài đặt gói phần mềm.
- `remove`: Gỡ bỏ gói phần mềm.
- `update`: Cập nhật gói phần mềm đã cài đặt.
- `search`: Tìm kiếm gói phần mềm trong kho.
- `info`: Hiển thị thông tin chi tiết về gói phần mềm.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `dnf`:

### Cài đặt một gói phần mềm
```bash
dnf install vim
```

### Gỡ bỏ một gói phần mềm
```bash
dnf remove vim
```

### Cập nhật tất cả các gói phần mềm
```bash
dnf update
```

### Tìm kiếm một gói phần mềm
```bash
dnf search httpd
```

### Hiển thị thông tin về một gói phần mềm
```bash
dnf info httpd
```

## Mẹo
- Luôn kiểm tra cập nhật thường xuyên để đảm bảo hệ thống của bạn an toàn và ổn định.
- Sử dụng tùy chọn `--assumeyes` để tự động xác nhận các hành động mà không cần nhập tay.
- Kiểm tra các gói phụ thuộc trước khi cài đặt hoặc gỡ bỏ để tránh xung đột phần mềm.