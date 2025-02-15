# [리눅스] Bash egrep 사용법

## Tổng quan
`egrep` là một lệnh trong Bash được sử dụng để tìm kiếm các mẫu trong văn bản. Nó là một phiên bản mở rộng của lệnh `grep`, cho phép sử dụng các biểu thức chính quy mở rộng (extended regular expressions). `egrep` rất hữu ích trong việc tìm kiếm các chuỗi phức tạp trong các tệp tin hoặc đầu ra của các lệnh khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `egrep` như sau:

```bash
egrep [tùy chọn] mẫu [tệp tin...]
```

### Các tùy chọn phổ biến:
- `-i`: Không phân biệt chữ hoa chữ thường.
- `-v`: In ra các dòng không khớp với mẫu.
- `-c`: Đếm số dòng khớp với mẫu.
- `-n`: Hiển thị số dòng cùng với kết quả.
- `-r`: Tìm kiếm đệ quy trong các thư mục.

## Ví dụ
### Ví dụ 1: Tìm kiếm một chuỗi trong một tệp
Giả sử bạn có một tệp tin tên là `data.txt` và bạn muốn tìm kiếm tất cả các dòng chứa từ "error":

```bash
egrep "error" data.txt
```

### Ví dụ 2: Tìm kiếm không phân biệt chữ hoa chữ thường
Nếu bạn muốn tìm kiếm từ "warning" mà không phân biệt chữ hoa chữ thường, bạn có thể sử dụng tùy chọn `-i`:

```bash
egrep -i "warning" data.txt
```

## Mẹo
- Sử dụng `egrep` với tùy chọn `-r` để tìm kiếm trong toàn bộ thư mục và các tệp con, giúp tiết kiệm thời gian khi làm việc với nhiều tệp.
- Kết hợp `egrep` với các lệnh khác như `find` để tìm kiếm các tệp cụ thể có chứa mẫu bạn đang tìm kiếm.
- Để kiểm tra các mẫu phức tạp, hãy thử sử dụng `egrep` trong một môi trường thử nghiệm trước khi áp dụng vào các tệp quan trọng.