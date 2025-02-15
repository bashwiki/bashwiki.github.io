# [리눅스] Bash sysctl 사용법

## Tổng quan
Lệnh `sysctl` được sử dụng để xem và thay đổi các tham số cấu hình của kernel trong hệ điều hành Linux. Nó cho phép người dùng điều chỉnh các thiết lập hệ thống mà không cần khởi động lại máy, giúp tối ưu hóa hiệu suất và bảo mật của hệ thống. Các tham số này thường được lưu trữ trong `/proc/sys`.

## Cách sử dụng
Cú pháp cơ bản của lệnh `sysctl` như sau:

```bash
sysctl [options] [parameter]
```

### Các tùy chọn phổ biến:
- `-a`: Hiển thị tất cả các tham số kernel và giá trị của chúng.
- `-n`: Chỉ hiển thị giá trị của tham số mà không có tên tham số.
- `-w`: Thay đổi giá trị của một tham số kernel.
- `-p`: Tải các tham số từ một tệp cấu hình.

## Ví dụ
### Ví dụ 1: Xem tất cả các tham số kernel
Để xem tất cả các tham số kernel hiện tại, bạn có thể sử dụng lệnh sau:

```bash
sysctl -a
```

### Ví dụ 2: Thay đổi giá trị của một tham số
Giả sử bạn muốn thay đổi kích thước tối đa của một tệp có thể được mở bởi một tiến trình, bạn có thể sử dụng lệnh sau:

```bash
sysctl -w fs.file-max=100000
```

## Mẹo
- Trước khi thay đổi bất kỳ tham số nào, hãy chắc chắn rằng bạn hiểu rõ về tác động của nó đối với hệ thống.
- Để lưu các thay đổi của bạn và tự động áp dụng chúng khi khởi động lại, bạn có thể thêm các tham số vào tệp `/etc/sysctl.conf`.
- Sử dụng lệnh `sysctl -n` để lấy giá trị của một tham số mà không cần hiển thị tên tham số, giúp bạn dễ dàng sử dụng trong các kịch bản tự động hóa.