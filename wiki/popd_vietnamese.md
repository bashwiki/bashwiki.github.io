# [리눅스] Bash popd 사용법

## Tổng quan
Lệnh `popd` trong Bash được sử dụng để xóa thư mục khỏi ngăn xếp thư mục hiện tại và chuyển đến thư mục đó. Ngăn xếp thư mục là một cấu trúc dữ liệu cho phép bạn lưu trữ nhiều thư mục và dễ dàng điều hướng giữa chúng. `popd` thường được sử dụng kết hợp với lệnh `pushd`, cho phép người dùng quay lại thư mục trước đó một cách nhanh chóng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `popd` như sau:

```bash
popd [options]
```

### Tùy chọn phổ biến
- `-n`: Không thay đổi thư mục hiện tại, chỉ xóa thư mục khỏi ngăn xếp.
- `+N`: Chỉ định một vị trí cụ thể trong ngăn xếp để xóa. Ví dụ, `+1` sẽ xóa thư mục ở vị trí thứ hai trong ngăn xếp.

## Ví dụ
### Ví dụ 1: Quay lại thư mục trước đó
Giả sử bạn đang ở trong thư mục `/home/user/documents` và đã sử dụng `pushd` để chuyển đến `/var/log`. Bạn có thể sử dụng `popd` để quay lại thư mục trước đó:

```bash
pushd /var/log
# Chuyển đến thư mục /var/log
popd
# Quay lại thư mục /home/user/documents
```

### Ví dụ 2: Sử dụng tùy chọn -n
Nếu bạn muốn xóa thư mục khỏi ngăn xếp mà không thay đổi thư mục hiện tại, bạn có thể sử dụng tùy chọn `-n`:

```bash
pushd /tmp
# Chuyển đến thư mục /tmp
popd -n
# Xóa /tmp khỏi ngăn xếp nhưng vẫn ở trong thư mục /tmp
```

## Mẹo
- Sử dụng `dirs` để xem danh sách các thư mục trong ngăn xếp trước khi sử dụng `popd`. Điều này giúp bạn biết được vị trí hiện tại của các thư mục trong ngăn xếp.
- Kết hợp `pushd` và `popd` để tạo ra một quy trình làm việc hiệu quả hơn khi bạn thường xuyên chuyển đổi giữa nhiều thư mục.