# [리눅스] Bash scp 사용법

## Tổng quan
`scp` (Secure Copy Protocol) là một lệnh trong Bash được sử dụng để sao chép tệp tin và thư mục giữa các máy tính qua một kết nối SSH (Secure Shell). Lệnh này giúp đảm bảo rằng dữ liệu được truyền tải một cách an toàn và bảo mật. `scp` thường được sử dụng để sao chép tệp từ máy cục bộ đến máy từ xa hoặc ngược lại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `scp` như sau:

```
scp [tùy chọn] [nguồn] [đích]
```

Trong đó:
- **nguồn**: Đường dẫn đến tệp hoặc thư mục bạn muốn sao chép. Có thể là một tệp trên máy cục bộ hoặc trên máy từ xa (được định dạng là `user@host:/path/to/file`).
- **đích**: Đường dẫn đến nơi bạn muốn sao chép tệp hoặc thư mục đến. Tương tự, có thể là máy cục bộ hoặc máy từ xa.

### Một số tùy chọn phổ biến:
- `-r`: Sao chép thư mục một cách đệ quy.
- `-P`: Chỉ định cổng SSH khác với cổng mặc định (22).
- `-i`: Chỉ định tệp khóa riêng để xác thực.

## Ví dụ
### Ví dụ 1: Sao chép tệp từ máy cục bộ đến máy từ xa
```bash
scp /path/to/local/file.txt user@remote_host:/path/to/remote/directory/
```
Lệnh này sẽ sao chép tệp `file.txt` từ máy cục bộ đến thư mục chỉ định trên máy từ xa.

### Ví dụ 2: Sao chép thư mục từ máy từ xa về máy cục bộ
```bash
scp -r user@remote_host:/path/to/remote/directory/ /path/to/local/directory/
```
Lệnh này sẽ sao chép toàn bộ thư mục từ máy từ xa về thư mục chỉ định trên máy cục bộ.

## Mẹo
- Đảm bảo rằng bạn có quyền truy cập vào máy từ xa và đã cấu hình SSH đúng cách trước khi sử dụng `scp`.
- Sử dụng tùy chọn `-v` để bật chế độ chi tiết, giúp bạn theo dõi quá trình sao chép và phát hiện lỗi nếu có.
- Nếu bạn thường xuyên sao chép tệp giữa hai máy, hãy xem xét việc thiết lập xác thực bằng khóa SSH để tiết kiệm thời gian nhập mật khẩu.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `scp` trong Bash!