# [Linux] Bash yum cách sử dụng: Quản lý gói phần mềm

## Tổng quan
Lệnh `yum` (Yellowdog Updater, Modified) là một công cụ quản lý gói phần mềm trên các hệ điều hành dựa trên RPM như CentOS, Fedora và Red Hat. Nó cho phép người dùng cài đặt, cập nhật, xóa và quản lý các gói phần mềm một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `yum` như sau:
```bash
yum [options] [arguments]
```

## Các tùy chọn phổ biến
- `install`: Cài đặt gói phần mềm.
- `remove`: Gỡ bỏ gói phần mềm.
- `update`: Cập nhật gói phần mềm đã cài đặt.
- `search`: Tìm kiếm gói phần mềm.
- `info`: Hiển thị thông tin chi tiết về gói phần mềm.
- `list`: Liệt kê các gói phần mềm có sẵn.

## Ví dụ thường gặp
- Cài đặt một gói phần mềm:
  ```bash
  yum install httpd
  ```

- Gỡ bỏ một gói phần mềm:
  ```bash
  yum remove httpd
  ```

- Cập nhật tất cả các gói phần mềm:
  ```bash
  yum update
  ```

- Tìm kiếm một gói phần mềm:
  ```bash
  yum search nginx
  ```

- Hiển thị thông tin chi tiết về một gói phần mềm:
  ```bash
  yum info httpd
  ```

- Liệt kê tất cả các gói đã cài đặt:
  ```bash
  yum list installed
  ```

## Mẹo
- Luôn chạy `yum update` thường xuyên để đảm bảo hệ thống của bạn được cập nhật với các bản vá bảo mật mới nhất.
- Sử dụng `yum clean all` để giải phóng dung lượng ổ đĩa bằng cách xóa bộ nhớ cache của yum.
- Kiểm tra các gói có thể cài đặt trước khi thực hiện cài đặt bằng cách sử dụng `yum list available`.