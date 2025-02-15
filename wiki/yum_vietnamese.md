# [리눅스] Bash yum 사용법

## Tổng quan
`yum` (Yellowdog Updater, Modified) là một công cụ quản lý gói dành cho các hệ điều hành dựa trên RPM (Red Hat Package Manager), như Red Hat Enterprise Linux, CentOS và Fedora. Mục đích chính của `yum` là giúp người dùng cài đặt, cập nhật và quản lý các gói phần mềm một cách dễ dàng và hiệu quả. `yum` tự động xử lý các phụ thuộc giữa các gói, giúp người dùng không phải lo lắng về việc tìm kiếm và cài đặt các gói cần thiết.

## Cách sử dụng
Cú pháp cơ bản của lệnh `yum` như sau:

```
yum [tùy chọn] [hành động] [gói]
```

### Các tùy chọn phổ biến:
- `install`: Cài đặt một gói phần mềm.
- `remove`: Gỡ bỏ một gói phần mềm.
- `update`: Cập nhật các gói đã cài đặt lên phiên bản mới nhất.
- `search`: Tìm kiếm gói phần mềm trong kho lưu trữ.
- `info`: Hiển thị thông tin chi tiết về một gói phần mềm.
- `list`: Liệt kê các gói đã cài đặt hoặc có sẵn trong kho lưu trữ.

## Ví dụ
### Ví dụ 1: Cài đặt một gói phần mềm
Để cài đặt gói phần mềm `httpd` (Apache HTTP Server), bạn có thể sử dụng lệnh sau:

```bash
yum install httpd
```

### Ví dụ 2: Cập nhật tất cả các gói đã cài đặt
Để cập nhật tất cả các gói phần mềm trên hệ thống, bạn có thể sử dụng lệnh sau:

```bash
yum update
```

## Mẹo
- Trước khi thực hiện các thao tác cài đặt hoặc cập nhật, hãy luôn kiểm tra xem có phiên bản mới của `yum` hay không bằng cách sử dụng lệnh `yum check-update`.
- Sử dụng tùy chọn `-y` để tự động xác nhận tất cả các yêu cầu trong quá trình cài đặt hoặc cập nhật, giúp tiết kiệm thời gian:

```bash
yum install -y httpd
```

- Để tiết kiệm băng thông, bạn có thể sử dụng tùy chọn `--downloadonly` để tải xuống gói mà không cài đặt ngay lập tức.

Hy vọng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng lệnh `yum` trong Bash!