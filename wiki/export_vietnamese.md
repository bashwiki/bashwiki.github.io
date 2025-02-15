# [리눅스] Bash export 사용법

## Tổng quan
Lệnh `export` trong Bash được sử dụng để thiết lập biến môi trường cho các tiến trình con. Khi bạn sử dụng `export`, biến mà bạn đã định nghĩa sẽ trở thành một biến môi trường, cho phép các chương trình và script khác truy cập và sử dụng giá trị của nó. Điều này rất hữu ích khi bạn muốn chia sẻ thông tin giữa các shell hoặc khi bạn cần cấu hình môi trường cho các ứng dụng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `export` như sau:

```bash
export VAR_NAME=value
```

Trong đó:
- `VAR_NAME` là tên của biến mà bạn muốn xuất.
- `value` là giá trị mà bạn muốn gán cho biến đó.

Ngoài ra, bạn cũng có thể xuất một biến đã được định nghĩa trước đó mà không cần gán giá trị mới:

```bash
export VAR_NAME
```

### Tùy chọn phổ biến
- `-p`: Hiển thị tất cả các biến môi trường hiện có và giá trị của chúng.

## Ví dụ
### Ví dụ 1: Xuất một biến mới
```bash
export MY_VAR="Hello, World!"
```
Sau khi thực hiện lệnh trên, biến `MY_VAR` sẽ có giá trị "Hello, World!" và có thể được truy cập từ các tiến trình con.

### Ví dụ 2: Xuất một biến đã được định nghĩa
```bash
MY_VAR="Hello, World!"
export MY_VAR
```
Trong ví dụ này, biến `MY_VAR` được định nghĩa trước và sau đó được xuất để có thể sử dụng trong các tiến trình con.

## Mẹo
- Để kiểm tra các biến môi trường đã được xuất, bạn có thể sử dụng lệnh `printenv` hoặc `env`.
- Hãy cẩn thận khi đặt tên biến; tránh sử dụng tên biến trùng với các biến hệ thống hoặc biến môi trường đã tồn tại để tránh xung đột.
- Để giữ cho môi trường của bạn sạch sẽ, hãy xem xét việc xóa các biến không còn cần thiết bằng cách sử dụng lệnh `unset VAR_NAME`.

Lệnh `export` là một công cụ mạnh mẽ trong Bash, giúp bạn quản lý và chia sẻ thông tin giữa các tiến trình một cách hiệu quả.