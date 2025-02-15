# [리눅스] Bash unxz 사용법

## Tổng quan
Lệnh `unxz` là một công cụ trong môi trường Bash được sử dụng để giải nén các tệp tin đã được nén bằng thuật toán nén XZ. XZ là một định dạng nén hiệu quả cao, thường được sử dụng để giảm kích thước tệp tin mà không làm mất dữ liệu. Lệnh `unxz` giúp người dùng phục hồi các tệp tin nén trở lại trạng thái ban đầu của chúng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `unxz` như sau:

```bash
unxz [tùy chọn] [tệp tin]
```

### Các tùy chọn phổ biến
- `-k`, `--keep`: Giữ lại tệp tin gốc sau khi giải nén.
- `-f`, `--force`: Buộc ghi đè lên tệp tin đã tồn tại mà không cần xác nhận.
- `-v`, `--verbose`: Hiển thị thông tin chi tiết về quá trình giải nén.

## Ví dụ
### Ví dụ 1: Giải nén một tệp tin
Để giải nén một tệp tin có tên là `example.xz`, bạn có thể sử dụng lệnh sau:

```bash
unxz example.xz
```

Lệnh này sẽ tạo ra tệp tin `example` (không có phần mở rộng) từ tệp tin nén `example.xz`.

### Ví dụ 2: Giữ lại tệp tin gốc
Nếu bạn muốn giữ lại tệp tin gốc sau khi giải nén, bạn có thể sử dụng tùy chọn `-k` như sau:

```bash
unxz -k example.xz
```

Lệnh này sẽ tạo ra tệp tin `example` và vẫn giữ lại tệp tin nén `example.xz`.

## Mẹo
- Khi làm việc với nhiều tệp tin nén, bạn có thể sử dụng ký tự đại diện (*) để giải nén tất cả các tệp tin nén trong thư mục hiện tại. Ví dụ:

```bash
unxz *.xz
```

- Hãy cẩn thận khi sử dụng tùy chọn `-f`, vì nó có thể ghi đè lên các tệp tin mà bạn không muốn mất. Luôn kiểm tra kỹ trước khi thực hiện lệnh này.