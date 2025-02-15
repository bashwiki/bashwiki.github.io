# [리눅스] Bash dnf 사용법

## Tổng quan
`dnf` (Dandified YUM) là một trình quản lý gói cho các hệ điều hành dựa trên RPM, như Fedora, CentOS và RHEL. Nó được thiết kế để thay thế `yum`, cung cấp một cách hiệu quả và dễ sử dụng hơn để cài đặt, cập nhật và quản lý các gói phần mềm. `dnf` hỗ trợ các tính năng như quản lý phụ thuộc, cài đặt hàng loạt và khả năng mở rộng tốt hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dnf` như sau:

```bash
dnf [tùy chọn] [lệnh] [gói]
```

### Các tùy chọn phổ biến:
- `install`: Cài đặt một hoặc nhiều gói.
- `remove`: Gỡ bỏ một hoặc nhiều gói.
- `update`: Cập nhật tất cả các gói đã cài đặt lên phiên bản mới nhất.
- `search`: Tìm kiếm gói trong kho lưu trữ.
- `info`: Hiển thị thông tin chi tiết về một gói cụ thể.
- `list`: Liệt kê các gói đã cài đặt hoặc có sẵn trong kho.

## Ví dụ
### Ví dụ 1: Cài đặt một gói
Để cài đặt gói `httpd` (Apache), bạn có thể sử dụng lệnh sau:

```bash
dnf install httpd
```

### Ví dụ 2: Cập nhật tất cả các gói
Để cập nhật tất cả các gói đã cài đặt lên phiên bản mới nhất, bạn có thể sử dụng lệnh:

```bash
dnf update
```

## Mẹo
- **Sử dụng `dnf clean all`**: Sau khi cài đặt hoặc cập nhật, bạn có thể giải phóng không gian bằng cách xóa bộ nhớ cache của `dnf` với lệnh này.
- **Kiểm tra thông tin gói**: Trước khi cài đặt, bạn có thể sử dụng `dnf info <tên_gói>` để xem thông tin chi tiết về gói đó, giúp bạn quyết định xem có nên cài đặt hay không.
- **Sử dụng `--assumeyes`**: Nếu bạn muốn tự động xác nhận tất cả các yêu cầu trong quá trình cài đặt hoặc cập nhật, bạn có thể thêm tùy chọn này vào lệnh của mình.

Hy vọng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng lệnh `dnf` trong Bash!