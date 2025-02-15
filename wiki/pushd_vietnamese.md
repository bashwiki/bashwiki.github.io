# [리눅스] Bash pushd 사용법

## Tổng quan
Lệnh `pushd` trong Bash được sử dụng để thay đổi thư mục làm việc hiện tại và đồng thời lưu trữ thư mục trước đó vào một ngăn xếp. Điều này cho phép người dùng dễ dàng quay lại thư mục trước đó bằng cách sử dụng lệnh `popd`. `pushd` rất hữu ích cho những người làm việc với nhiều thư mục khác nhau trong quá trình phát triển hoặc quản lý dự án.

## Cách sử dụng
Cú pháp cơ bản của lệnh `pushd` như sau:

```bash
pushd [thư_mục]
```

Trong đó:
- `thư_mục`: Đường dẫn đến thư mục mà bạn muốn chuyển đến. Nếu không chỉ định, `pushd` sẽ hoán đổi giữa hai thư mục đầu tiên trong ngăn xếp.

### Tùy chọn phổ biến
- `+n`: Chuyển đến thư mục thứ `n` trong ngăn xếp mà không thay đổi vị trí của các thư mục khác.
- `-n`: Chuyển đến thư mục thứ `n` trong ngăn xếp và đồng thời xóa thư mục đó khỏi ngăn xếp.

## Ví dụ
### Ví dụ 1: Chuyển đến thư mục mới
```bash
pushd /home/user/documents
```
Lệnh này sẽ chuyển đến thư mục `/home/user/documents` và lưu thư mục hiện tại vào ngăn xếp.

### Ví dụ 2: Quay lại thư mục trước đó
```bash
pushd /var/log
popd
```
Trong ví dụ này, lệnh `pushd` chuyển đến thư mục `/var/log`, và lệnh `popd` sẽ quay lại thư mục trước đó mà bạn đã lưu vào ngăn xếp.

## Mẹo
- Sử dụng `dirs` để xem danh sách các thư mục trong ngăn xếp hiện tại. Điều này giúp bạn theo dõi vị trí của mình khi làm việc với nhiều thư mục.
- Kết hợp `pushd` và `popd` để tạo ra các kịch bản tự động hóa hiệu quả, giúp tiết kiệm thời gian khi chuyển đổi giữa các thư mục trong quy trình làm việc hàng ngày.