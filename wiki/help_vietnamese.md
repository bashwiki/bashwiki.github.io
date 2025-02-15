# [리눅스] Bash help 사용법

## Tổng quan
Lệnh `help` trong Bash được sử dụng để hiển thị thông tin trợ giúp về các lệnh tích hợp (built-in commands) của Bash. Mục đích chính của lệnh này là cung cấp cho người dùng thông tin chi tiết về cách sử dụng các lệnh tích hợp, bao gồm cú pháp, tùy chọn và ví dụ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `help` như sau:

```bash
help [tùy chọn] [lệnh]
```

- **tùy chọn**: Một số tùy chọn có thể được sử dụng với lệnh `help`, bao gồm:
  - `-s`: Hiển thị thông tin ngắn gọn về lệnh.
  - `-m`: Hiển thị thông tin trợ giúp theo định dạng Markdown.

- **lệnh**: Tên của lệnh tích hợp mà bạn muốn tìm hiểu thêm.

Nếu không có lệnh nào được chỉ định, lệnh `help` sẽ hiển thị danh sách tất cả các lệnh tích hợp có sẵn trong Bash.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `help`:

1. Hiển thị thông tin trợ giúp về lệnh `cd`:
   ```bash
   help cd
   ```

2. Hiển thị danh sách tất cả các lệnh tích hợp:
   ```bash
   help
   ```

3. Hiển thị thông tin ngắn gọn về lệnh `echo`:
   ```bash
   help -s echo
   ```

## Mẹo
- Sử dụng lệnh `help` để nhanh chóng tìm hiểu về các lệnh tích hợp mà bạn chưa quen thuộc.
- Khi bạn gặp khó khăn với một lệnh tích hợp, hãy thử sử dụng `help [lệnh]` để xem thông tin trợ giúp cụ thể.
- Kết hợp lệnh `help` với các lệnh khác trong Bash để nâng cao khả năng sử dụng và hiểu biết về môi trường dòng lệnh.