# [Linux] Bash help Cách sử dụng: Hiển thị thông tin trợ giúp cho các lệnh

## Tổng quan
Lệnh `help` trong Bash được sử dụng để hiển thị thông tin trợ giúp cho các built-in commands. Nó giúp người dùng hiểu cách sử dụng các lệnh này, bao gồm cú pháp và các tùy chọn có sẵn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `help` như sau:
```
help [options] [arguments]
```

## Các tùy chọn phổ biến
- `-s`, `--silent`: Không hiển thị tiêu đề.
- `-m`, `--man`: Hiển thị thông tin trợ giúp theo định dạng của trang man.
- `-d`, `--description`: Hiển thị chỉ phần mô tả của lệnh.

## Ví dụ phổ biến
Dưới đây là một số ví dụ về cách sử dụng lệnh `help`:

1. Hiển thị thông tin trợ giúp cho lệnh `cd`:
   ```bash
   help cd
   ```

2. Hiển thị thông tin trợ giúp cho lệnh `echo`:
   ```bash
   help echo
   ```

3. Hiển thị thông tin trợ giúp cho tất cả các lệnh built-in:
   ```bash
   help
   ```

4. Hiển thị thông tin trợ giúp cho lệnh `set` mà không có tiêu đề:
   ```bash
   help -s set
   ```

## Mẹo
- Sử dụng `help` để nhanh chóng tìm hiểu về các lệnh built-in mà bạn chưa quen thuộc.
- Kết hợp với các tùy chọn để có được thông tin chi tiết hơn hoặc theo định dạng mà bạn muốn.
- Thường xuyên tham khảo thông tin trợ giúp khi làm việc với các lệnh mới để tránh nhầm lẫn.