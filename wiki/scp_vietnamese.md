# [Linux] Bash scp cách sử dụng: Chuyển tệp an toàn giữa các máy tính

## Tổng quan
Lệnh `scp` (Secure Copy Protocol) được sử dụng để sao chép tệp và thư mục giữa các máy tính qua mạng một cách an toàn. Nó sử dụng giao thức SSH để đảm bảo tính bảo mật trong quá trình truyền tải dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `scp` như sau:
```bash
scp [tùy chọn] [đối số]
```

## Các tùy chọn phổ biến
- `-r`: Sao chép thư mục và tất cả các tệp bên trong.
- `-P [cổng]`: Chỉ định cổng SSH khác với cổng mặc định (22).
- `-i [tệp khóa]`: Sử dụng tệp khóa SSH để xác thực.
- `-v`: Chế độ chi tiết, hiển thị thông tin về quá trình sao chép.

## Ví dụ thường gặp
1. Sao chép một tệp từ máy tính cục bộ đến máy chủ từ xa:
   ```bash
   scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
   ```

2. Sao chép một tệp từ máy chủ từ xa về máy tính cục bộ:
   ```bash
   scp user@remote_host:/path/to/remote/file.txt /path/to/local/directory/
   ```

3. Sao chép một thư mục từ máy tính cục bộ đến máy chủ từ xa:
   ```bash
   scp -r /path/to/local/directory user@remote_host:/path/to/remote/
   ```

4. Sao chép một tệp sử dụng cổng SSH khác:
   ```bash
   scp -P 2222 /path/to/local/file.txt user@remote_host:/path/to/remote/
   ```

## Mẹo
- Luôn kiểm tra kết nối mạng và quyền truy cập trước khi thực hiện lệnh `scp`.
- Sử dụng tùy chọn `-v` để gỡ lỗi nếu gặp sự cố trong quá trình sao chép.
- Để tăng tốc độ sao chép, bạn có thể sử dụng tùy chọn `-C` để nén dữ liệu trong quá trình truyền tải.