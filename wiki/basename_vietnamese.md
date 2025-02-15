# [리눅스] Bash basename 사용법

## Tổng quan
Lệnh `basename` trong Bash được sử dụng để trích xuất tên tệp từ một đường dẫn đầy đủ. Mục đích chính của lệnh này là giúp người dùng dễ dàng lấy tên tệp mà không cần phải xử lý toàn bộ đường dẫn. Điều này rất hữu ích trong các kịch bản tự động hóa hoặc khi bạn cần làm việc với các tệp mà không muốn giữ lại thông tin về thư mục chứa chúng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `basename` như sau:

```bash
basename [OPTION]... NAME [SUFFIX]...
```

Trong đó:
- `NAME`: Đường dẫn đầy đủ của tệp mà bạn muốn lấy tên.
- `SUFFIX`: (Tùy chọn) Một phần mở rộng mà bạn muốn loại bỏ khỏi tên tệp.

### Tùy chọn phổ biến
- `-a`: Xử lý nhiều tệp và trả về tên của từng tệp.
- `-s`: Loại bỏ phần mở rộng được chỉ định từ tên tệp.

## Ví dụ
Dưới đây là một vài ví dụ minh họa cách sử dụng lệnh `basename`.

### Ví dụ 1: Lấy tên tệp từ đường dẫn
```bash
basename /home/user/documents/file.txt
```
Kết quả sẽ là:
```
file.txt
```

### Ví dụ 2: Loại bỏ phần mở rộng
```bash
basename /home/user/documents/file.txt .txt
```
Kết quả sẽ là:
```
file
```

## Mẹo
- Khi làm việc với nhiều tệp, bạn có thể sử dụng tùy chọn `-a` để lấy tên của tất cả các tệp trong một lần:
```bash
basename -a /home/user/documents/file1.txt /home/user/documents/file2.txt
```
- Hãy chú ý đến việc sử dụng đúng phần mở rộng khi loại bỏ nó, vì nếu phần mở rộng không khớp, tên tệp sẽ không bị thay đổi.

Lệnh `basename` là một công cụ đơn giản nhưng mạnh mẽ trong Bash, giúp bạn quản lý và xử lý tên tệp một cách hiệu quả.