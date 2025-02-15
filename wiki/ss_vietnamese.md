# [리눅스] Bash ss 사용법

## Tổng quan
Lệnh `ss` là một công cụ mạnh mẽ trong Bash được sử dụng để hiển thị thông tin về các kết nối mạng trên hệ thống. Nó cho phép người dùng xem các kết nối TCP, UDP, và các thông tin liên quan đến socket, giúp theo dõi và phân tích trạng thái mạng một cách hiệu quả. `ss` thường được sử dụng như một thay thế cho lệnh `netstat`, với hiệu suất tốt hơn và khả năng hiển thị thông tin chi tiết hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ss` như sau:

```bash
ss [tùy chọn]
```

Một số tùy chọn phổ biến của lệnh `ss` bao gồm:

- `-t`: Hiển thị các kết nối TCP.
- `-u`: Hiển thị các kết nối UDP.
- `-l`: Hiển thị các socket đang lắng nghe.
- `-p`: Hiển thị thông tin về tiến trình đang sử dụng socket.
- `-n`: Hiển thị địa chỉ IP và số cổng mà không cần phân giải tên.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `ss`:

1. Để hiển thị tất cả các kết nối TCP hiện tại:

   ```bash
   ss -t
   ```

2. Để hiển thị tất cả các socket UDP đang lắng nghe:

   ```bash
   ss -ul
   ```

3. Để xem thông tin chi tiết về các kết nối TCP cùng với tiến trình sử dụng:

   ```bash
   ss -tp
   ```

## Mẹo
- Sử dụng tùy chọn `-n` để tăng tốc độ hiển thị thông tin bằng cách tránh phân giải tên miền, điều này rất hữu ích khi bạn cần xem nhanh các kết nối.
- Kết hợp các tùy chọn để có được cái nhìn tổng quan hơn về trạng thái mạng, ví dụ: `ss -tunlp` sẽ hiển thị tất cả các kết nối TCP và UDP cùng với thông tin về tiến trình.
- Lưu ý rằng bạn có thể cần quyền truy cập root để xem thông tin về một số socket hoặc tiến trình nhất định.