# [Linux] Bash exit lệnh: Thoát khỏi shell hoặc script

## Tổng quan
Lệnh `exit` trong Bash được sử dụng để thoát khỏi một shell hoặc một script. Khi lệnh này được thực thi, nó sẽ kết thúc phiên làm việc hiện tại và trả về một mã thoát cho hệ thống. Mã thoát này có thể được sử dụng để xác định trạng thái của quá trình trước đó.

## Cú pháp
Cú pháp cơ bản của lệnh `exit` như sau:
```bash
exit [options] [arguments]
```

## Tùy chọn phổ biến
- `n`: Chỉ định mã thoát (0-255). Nếu không có mã thoát nào được chỉ định, lệnh sẽ trả về mã thoát của lệnh cuối cùng đã thực thi.
- `-h`: Hiển thị trợ giúp về lệnh `exit`.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `exit`:

1. Thoát khỏi shell mà không chỉ định mã thoát:
   ```bash
   exit
   ```

2. Thoát khỏi shell và trả về mã thoát 0 (thành công):
   ```bash
   exit 0
   ```

3. Thoát khỏi shell và trả về mã thoát 1 (thất bại):
   ```bash
   exit 1
   ```

4. Sử dụng trong một script để thoát khi có lỗi:
   ```bash
   #!/bin/bash
   if [ ! -f "file.txt" ]; then
       echo "File không tồn tại!"
       exit 1
   fi
   ```

## Mẹo
- Luôn sử dụng mã thoát 0 để chỉ ra rằng script đã thực thi thành công và mã thoát khác để chỉ ra lỗi.
- Kiểm tra mã thoát của lệnh trước đó bằng cách sử dụng biến `$?` để xử lý các tình huống lỗi một cách hiệu quả.
- Khi viết script, hãy đảm bảo rằng bạn có các điều kiện thoát hợp lý để tránh việc script chạy không cần thiết.