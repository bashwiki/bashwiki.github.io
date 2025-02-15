# [리눅스] Bash exec 사용법

## Tổng quan
Lệnh `exec` trong Bash được sử dụng để thay thế một tiến trình hiện tại bằng một tiến trình mới. Điều này có nghĩa là khi bạn sử dụng `exec`, shell hiện tại sẽ không còn tồn tại nữa và sẽ được thay thế hoàn toàn bởi tiến trình mới mà bạn chỉ định. Lệnh này thường được sử dụng để tiết kiệm tài nguyên hệ thống, vì nó không tạo ra một tiến trình con mới, mà thay vào đó thay thế tiến trình hiện tại.

## Cú pháp
Cú pháp cơ bản của lệnh `exec` như sau:

```bash
exec [OPTION] COMMAND [ARGUMENTS...]
```

### Tùy chọn phổ biến
- `-a, --arg`: Chỉ định tên khác cho tiến trình mới.
- `-l, --login`: Thay thế shell hiện tại bằng một shell đăng nhập mới.
- `-c, --command`: Chạy một lệnh cụ thể mà không cần phải tạo một shell mới.

## Ví dụ
### Ví dụ 1: Thay thế shell hiện tại bằng một lệnh
```bash
exec ls -l
```
Trong ví dụ này, lệnh `ls -l` sẽ được thực thi và shell hiện tại sẽ bị thay thế bởi kết quả của lệnh này. Sau khi lệnh hoàn tất, bạn sẽ không quay lại shell.

### Ví dụ 2: Sử dụng exec để chạy một chương trình
```bash
exec /bin/bash
```
Lệnh này sẽ thay thế shell hiện tại bằng một phiên bản mới của Bash. Bạn sẽ có một shell mới mà không cần phải tạo một tiến trình con.

## Mẹo
- Sử dụng `exec` khi bạn muốn tiết kiệm tài nguyên hệ thống, đặc biệt là trong các kịch bản tự động hóa hoặc trong các tập lệnh khởi động.
- Hãy cẩn thận khi sử dụng `exec`, vì sau khi thực hiện, bạn sẽ không thể quay lại shell trước đó.
- Nếu bạn muốn kiểm tra lệnh mà không thay thế shell hiện tại, hãy sử dụng lệnh thông thường mà không có `exec`.