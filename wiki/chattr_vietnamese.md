# [리눅스] Bash chattr 사용법

## Tổng quan
Lệnh `chattr` (change attribute) trong Linux được sử dụng để thay đổi thuộc tính của các tệp tin và thư mục. Mục đích chính của lệnh này là để bảo vệ tệp tin khỏi các thay đổi không mong muốn, như việc xóa hoặc ghi đè. Các thuộc tính này có thể giúp quản lý quyền truy cập và bảo mật cho các tệp tin quan trọng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `chattr` như sau:

```bash
chattr [options] [attributes] [file...]
```

### Các tùy chọn phổ biến:
- `+`: Thêm thuộc tính.
- `-`: Xóa thuộc tính.
- `=`: Đặt thuộc tính cụ thể.
- `a`: Chỉ cho phép ghi vào tệp tin (append only).
- `i`: Không cho phép thay đổi tệp tin (immutable).
- `s`: Xóa tệp tin ngay lập tức khi nó bị xóa (secure deletion).

## Ví dụ
### Ví dụ 1: Đặt thuộc tính không thay đổi cho một tệp tin
Giả sử bạn muốn bảo vệ tệp tin `important.txt` khỏi bất kỳ thay đổi nào, bạn có thể sử dụng lệnh sau:

```bash
chattr +i important.txt
```

Sau khi thực hiện lệnh này, tệp tin `important.txt` sẽ không thể bị xóa hoặc sửa đổi cho đến khi thuộc tính này được gỡ bỏ.

### Ví dụ 2: Thêm thuộc tính ghi vào cho một tệp tin
Nếu bạn muốn chỉ cho phép thêm dữ liệu vào tệp tin `log.txt`, bạn có thể sử dụng lệnh sau:

```bash
chattr +a log.txt
```

Bây giờ, bạn chỉ có thể thêm dữ liệu vào `log.txt` mà không thể ghi đè lên nội dung hiện có.

## Mẹo
- Hãy cẩn thận khi sử dụng thuộc tính `i` vì nó có thể gây khó khăn trong việc quản lý tệp tin nếu bạn quên gỡ bỏ thuộc tính này.
- Kiểm tra thuộc tính hiện tại của tệp tin bằng lệnh `lsattr` để biết các thuộc tính đang áp dụng cho tệp tin đó.
- Sử dụng `chattr` với quyền root để thay đổi thuộc tính của các tệp tin hệ thống hoặc tệp tin của người dùng khác.