# [Linux] Bash popd Cách sử dụng: Quay lại thư mục trước đó

## Tổng quan
Lệnh `popd` trong Bash được sử dụng để quay lại thư mục trước đó mà bạn đã lưu trong ngăn xếp thư mục. Nó giúp bạn dễ dàng di chuyển giữa các thư mục mà không cần phải nhập lại đường dẫn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `popd` như sau:

```
popd [options]
```

## Các tùy chọn phổ biến
- `-n`: Không thay đổi thư mục hiện tại, chỉ cập nhật ngăn xếp.
- `+n`: Quay lại thư mục ở vị trí thứ n trong ngăn xếp.
- `-n`: Quay lại thư mục ở vị trí âm n trong ngăn xếp.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `popd`:

1. **Quay lại thư mục trước đó**:
   ```bash
   pushd /path/to/directory
   # Thực hiện một số công việc trong thư mục
   popd
   ```

2. **Sử dụng tùy chọn `+n` để quay lại thư mục cụ thể**:
   ```bash
   pushd /path/to/first
   pushd /path/to/second
   pushd /path/to/third
   popd +1  # Quay lại thư mục thứ hai trong ngăn xếp
   ```

3. **Sử dụng tùy chọn `-n` để không thay đổi thư mục hiện tại**:
   ```bash
   pushd /path/to/first
   pushd /path/to/second
   popd -n  # Cập nhật ngăn xếp nhưng không thay đổi thư mục hiện tại
   ```

## Mẹo
- Luôn kiểm tra ngăn xếp thư mục bằng lệnh `dirs` trước khi sử dụng `popd` để biết vị trí hiện tại của các thư mục.
- Sử dụng `pushd` và `popd` cùng nhau để dễ dàng quản lý các thư mục khi làm việc với nhiều dự án.
- Hãy cẩn thận với các tùy chọn `+n` và `-n` để tránh nhầm lẫn trong việc quay lại thư mục.