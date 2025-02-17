# [Linux] Bash ss cách sử dụng: Xem thông tin kết nối mạng

## Tổng quan
Lệnh `ss` được sử dụng để hiển thị thông tin về các kết nối mạng trên hệ thống Linux. Nó cung cấp thông tin chi tiết về các kết nối TCP, UDP, và các loại giao thức khác, giúp người dùng theo dõi và quản lý mạng hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ss` như sau:

```bash
ss [options] [arguments]
```

## Các tùy chọn phổ biến
- `-t`: Hiển thị các kết nối TCP.
- `-u`: Hiển thị các kết nối UDP.
- `-l`: Hiển thị các kết nối đang lắng nghe.
- `-p`: Hiển thị thông tin về tiến trình sử dụng kết nối.
- `-n`: Hiển thị địa chỉ IP và số cổng mà không phân giải tên miền.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `ss`:

1. Hiển thị tất cả các kết nối TCP:
   ```bash
   ss -t
   ```

2. Hiển thị tất cả các kết nối UDP:
   ```bash
   ss -u
   ```

3. Hiển thị các kết nối đang lắng nghe:
   ```bash
   ss -l
   ```

4. Hiển thị thông tin chi tiết về các kết nối TCP, bao gồm cả tiến trình:
   ```bash
   ss -t -p
   ```

5. Hiển thị tất cả các kết nối mà không phân giải tên miền:
   ```bash
   ss -n
   ```

## Mẹo
- Sử dụng kết hợp các tùy chọn để có được thông tin chi tiết hơn. Ví dụ, `ss -tunlp` sẽ hiển thị tất cả các kết nối TCP và UDP đang lắng nghe cùng với thông tin tiến trình.
- Thường xuyên kiểm tra các kết nối mạng để phát hiện các vấn đề tiềm ẩn hoặc các kết nối không mong muốn.
- Kết hợp lệnh `ss` với các công cụ khác như `grep` để lọc thông tin theo nhu cầu cụ thể của bạn.