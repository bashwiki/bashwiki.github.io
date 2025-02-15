# [리눅스] Bash builtin 사용법

## Tổng quan
Lệnh `builtin` trong Bash được sử dụng để gọi các lệnh nội bộ (built-in commands) của shell mà không cần phải tìm kiếm trong các tệp thực thi bên ngoài. Mục đích chính của lệnh này là cho phép người dùng thực thi các lệnh nội bộ mà không bị ảnh hưởng bởi các lệnh cùng tên trong các tệp thực thi, giúp đảm bảo rằng lệnh nội bộ sẽ được thực thi.

## Cú pháp
Cú pháp cơ bản của lệnh `builtin` như sau:

```bash
builtin [lệnh] [các tham số]
```

Trong đó:
- `[lệnh]`: Tên của lệnh nội bộ mà bạn muốn gọi.
- `[các tham số]`: Các tham số tùy chọn mà bạn muốn truyền cho lệnh.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `builtin`.

### Ví dụ 1: Sử dụng `builtin` để gọi lệnh `echo`
```bash
builtin echo "Đây là một lệnh echo nội bộ."
```
Lệnh này sẽ gọi lệnh `echo` nội bộ của Bash và in ra chuỗi "Đây là một lệnh echo nội bộ."

### Ví dụ 2: Sử dụng `builtin` với `cd`
```bash
builtin cd /home/user
```
Lệnh này sẽ thay đổi thư mục làm việc hiện tại đến `/home/user` bằng cách sử dụng lệnh `cd` nội bộ, đảm bảo rằng bạn đang sử dụng lệnh nội bộ thay vì một tệp thực thi có tên tương tự.

## Mẹo
- Sử dụng lệnh `builtin` khi bạn muốn chắc chắn rằng bạn đang sử dụng lệnh nội bộ của Bash, đặc biệt khi có khả năng có xung đột với các lệnh bên ngoài.
- Kiểm tra danh sách các lệnh nội bộ có sẵn bằng cách sử dụng lệnh `help` trong Bash, điều này sẽ giúp bạn hiểu rõ hơn về các lệnh mà bạn có thể sử dụng với `builtin`.