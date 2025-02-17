# [Linux] Bash rpm cách sử dụng: Quản lý gói phần mềm

## Tổng quan
Lệnh `rpm` (Red Hat Package Manager) là một công cụ quản lý gói phần mềm được sử dụng chủ yếu trên các hệ điều hành dựa trên Red Hat. Nó cho phép người dùng cài đặt, gỡ bỏ, và quản lý các gói phần mềm dưới định dạng `.rpm`.

## Cách sử dụng
Cú pháp cơ bản của lệnh `rpm` như sau:

```bash
rpm [options] [arguments]
```

## Các tùy chọn thông dụng
- `-i`: Cài đặt một gói phần mềm mới.
- `-e`: Gỡ bỏ một gói phần mềm đã cài đặt.
- `-q`: Truy vấn thông tin về một gói phần mềm.
- `-U`: Cập nhật một gói phần mềm đã cài đặt.
- `--force`: Bỏ qua các cảnh báo và cài đặt gói phần mềm.

## Ví dụ thông dụng
### Cài đặt một gói phần mềm
```bash
rpm -i package.rpm
```

### Gỡ bỏ một gói phần mềm
```bash
rpm -e package-name
```

### Truy vấn thông tin về một gói phần mềm
```bash
rpm -q package-name
```

### Cập nhật một gói phần mềm
```bash
rpm -U package.rpm
```

### Xem danh sách các tệp trong một gói
```bash
rpm -ql package-name
```

## Mẹo
- Luôn kiểm tra các phụ thuộc của gói trước khi cài đặt để tránh lỗi.
- Sử dụng tùy chọn `--force` một cách cẩn thận, vì nó có thể gây ra xung đột với các gói khác.
- Để tìm hiểu thêm về các tùy chọn, bạn có thể sử dụng `man rpm` để xem tài liệu hướng dẫn chi tiết.