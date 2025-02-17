# [Linux] Bash userdel: Xóa người dùng trong hệ thống

## Overview
Lệnh `userdel` trong Bash được sử dụng để xóa một tài khoản người dùng khỏi hệ thống. Khi một tài khoản bị xóa, tất cả các thông tin liên quan đến tài khoản đó cũng sẽ bị xóa, bao gồm cả thư mục chính và các tệp tin liên quan (nếu được chỉ định).

## Usage
Cú pháp cơ bản của lệnh `userdel` như sau:

```bash
userdel [options] [arguments]
```

## Common Options
- `-r`: Xóa thư mục chính của người dùng và các tệp tin liên quan.
- `-f`: Buộc xóa người dùng ngay cả khi người dùng đang đăng nhập.
- `-Z`: Xóa nhãn SELinux của người dùng.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `userdel`:

1. **Xóa một người dùng mà không xóa thư mục chính**:
   ```bash
   userdel username
   ```

2. **Xóa một người dùng và thư mục chính của họ**:
   ```bash
   userdel -r username
   ```

3. **Buộc xóa người dùng ngay cả khi họ đang đăng nhập**:
   ```bash
   userdel -f username
   ```

4. **Xóa một người dùng và xóa nhãn SELinux**:
   ```bash
   userdel -Z username
   ```

## Tips
- Trước khi xóa một người dùng, hãy đảm bảo rằng bạn đã sao lưu tất cả dữ liệu quan trọng của họ.
- Kiểm tra xem người dùng có đang đăng nhập hay không bằng cách sử dụng lệnh `who` trước khi thực hiện lệnh `userdel -f`.
- Sử dụng tùy chọn `-r` một cách cẩn thận, vì nó sẽ xóa toàn bộ thư mục chính và không thể khôi phục lại.