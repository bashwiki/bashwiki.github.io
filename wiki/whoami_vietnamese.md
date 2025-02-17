# [Linux] Bash whoami Cách sử dụng: Xác định tên người dùng hiện tại

## Tổng quan
Lệnh `whoami` trong Bash được sử dụng để hiển thị tên người dùng hiện tại đang đăng nhập vào hệ thống. Đây là một công cụ hữu ích để xác định danh tính của người dùng trong môi trường dòng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `whoami` như sau:

```
whoami [options] [arguments]
```

## Tùy chọn phổ biến
- Không có tùy chọn đặc biệt nào cho lệnh `whoami`, nó chỉ đơn giản là hiển thị tên người dùng hiện tại.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `whoami`:

1. **Hiển thị tên người dùng hiện tại:**
   ```bash
   whoami
   ```

2. **Sử dụng trong một script:**
   ```bash
   echo "Bạn đang đăng nhập với tên người dùng: $(whoami)"
   ```

3. **Kết hợp với lệnh khác:**
   ```bash
   sudo -u $(whoami) command
   ```

## Mẹo
- Sử dụng lệnh `whoami` trong các script để xác định quyền truy cập của người dùng.
- Kết hợp lệnh `whoami` với các lệnh khác để thực hiện các tác vụ dựa trên quyền của người dùng hiện tại.