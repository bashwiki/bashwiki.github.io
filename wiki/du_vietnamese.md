# [리눅스] Bash du 사용법

## Tổng quan
Lệnh `du` (Disk Usage) trong Bash được sử dụng để ước lượng kích thước của các tệp và thư mục trong hệ thống tệp. Mục đích chính của lệnh này là giúp người dùng hiểu rõ hơn về cách mà không gian lưu trữ được sử dụng trên đĩa cứng, từ đó có thể quản lý tài nguyên một cách hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `du` như sau:

```bash
du [tùy chọn] [tệp hoặc thư mục]
```

### Các tùy chọn phổ biến:
- `-h`: Hiển thị kích thước theo định dạng dễ đọc (human-readable), ví dụ như KB, MB, GB.
- `-s`: Tóm tắt kích thước của thư mục mà không liệt kê từng tệp con.
- `-a`: Hiển thị kích thước của tất cả các tệp và thư mục con.
- `-c`: Tính tổng kích thước của tất cả các tệp và thư mục được liệt kê.
- `--max-depth=N`: Giới hạn độ sâu của thư mục được hiển thị, nơi N là số nguyên.

## Ví dụ
### Ví dụ 1: Kiểm tra kích thước của một thư mục
Để kiểm tra kích thước của thư mục hiện tại, bạn có thể sử dụng lệnh sau:

```bash
du -sh .
```
Lệnh này sẽ hiển thị kích thước tổng cộng của thư mục hiện tại theo định dạng dễ đọc.

### Ví dụ 2: Liệt kê kích thước của tất cả các thư mục con
Để xem kích thước của tất cả các thư mục con trong thư mục hiện tại, bạn có thể sử dụng:

```bash
du -h --max-depth=1
```
Lệnh này sẽ hiển thị kích thước của từng thư mục con trong thư mục hiện tại mà không đi sâu vào các thư mục con hơn nữa.

## Mẹo
- Sử dụng tùy chọn `-c` để có cái nhìn tổng quan về không gian lưu trữ của nhiều thư mục cùng một lúc.
- Kết hợp lệnh `du` với lệnh `sort` để sắp xếp các thư mục theo kích thước, ví dụ:

```bash
du -h | sort -hr
```
Điều này sẽ giúp bạn nhanh chóng xác định các thư mục chiếm nhiều không gian nhất trên đĩa cứng.
- Hãy cẩn thận khi sử dụng lệnh `du` trên các hệ thống có nhiều tệp lớn, vì nó có thể mất thời gian để hoàn thành.