# [리눅스] Bash whoami 사용법

## Tổng quan
Lệnh `whoami` trong Bash được sử dụng để hiển thị tên người dùng hiện tại đang đăng nhập vào hệ thống. Đây là một công cụ hữu ích cho các kỹ sư và nhà phát triển để xác định danh tính của người dùng đang thực hiện các lệnh trong terminal, đặc biệt trong các môi trường đa người dùng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `whoami` rất đơn giản:

```bash
whoami
```

Lệnh này không yêu cầu bất kỳ tùy chọn nào và sẽ trả về tên người dùng hiện tại.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `whoami`:

1. **Hiển thị tên người dùng hiện tại**:
   ```bash
   whoami
   ```
   Kết quả có thể là:
   ```
   username
   ```

2. **Sử dụng trong một script**:
   Bạn có thể sử dụng lệnh `whoami` trong một script để kiểm tra người dùng hiện tại:
   ```bash
   #!/bin/bash
   echo "Người dùng hiện tại là: $(whoami)"
   ```
   Khi chạy script này, nó sẽ in ra tên người dùng hiện tại.

## Mẹo
- **Kiểm tra quyền truy cập**: Sử dụng `whoami` để xác nhận bạn đang hoạt động với quyền người dùng nào, điều này rất quan trọng khi thực hiện các lệnh yêu cầu quyền truy cập cao hơn.
- **Kết hợp với các lệnh khác**: Bạn có thể kết hợp `whoami` với các lệnh khác trong Bash để thực hiện các tác vụ tùy chỉnh dựa trên người dùng hiện tại.

Lệnh `whoami` là một công cụ đơn giản nhưng mạnh mẽ giúp bạn xác định danh tính người dùng trong môi trường dòng lệnh.