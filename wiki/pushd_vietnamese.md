# [Linux] Bash pushd cách sử dụng: Chuyển đổi thư mục dễ dàng

## Tổng quan
Lệnh `pushd` trong Bash được sử dụng để thay đổi thư mục làm việc hiện tại và đồng thời lưu trữ thư mục trước đó vào một ngăn xếp. Điều này cho phép bạn dễ dàng quay lại thư mục trước đó bằng cách sử dụng lệnh `popd`.

## Cách sử dụng
Cú pháp cơ bản của lệnh `pushd` như sau:
```
pushd [tùy chọn] [thư mục]
```

## Tùy chọn phổ biến
- `+n`: Chuyển đến thư mục ở vị trí thứ n trong ngăn xếp.
- `-n`: Chuyển đến thư mục ở vị trí thứ n từ dưới lên trong ngăn xếp.
- `-`: Quay lại thư mục trước đó.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `pushd`:

1. Chuyển đến một thư mục cụ thể và lưu thư mục hiện tại:
   ```bash
   pushd /path/to/directory
   ```

2. Quay lại thư mục trước đó:
   ```bash
   popd
   ```

3. Chuyển đến thư mục thứ hai trong ngăn xếp:
   ```bash
   pushd +1
   ```

4. Chuyển đến thư mục thứ hai từ dưới lên:
   ```bash
   pushd -1
   ```

## Mẹo
- Sử dụng `pushd` và `popd` để quản lý nhiều thư mục mà không cần phải ghi nhớ đường dẫn.
- Kiểm tra ngăn xếp thư mục hiện tại bằng lệnh `dirs` để xem danh sách các thư mục đã được lưu.
- Kết hợp `pushd` với các lệnh khác để tự động hóa quy trình làm việc của bạn.