# [Linux] Bash builtin `builtin`: Truy cập các lệnh nội bộ

## Overview
Lệnh `builtin` trong Bash cho phép người dùng gọi các lệnh nội bộ của shell mà không cần phải sử dụng các lệnh bên ngoài. Điều này hữu ích khi bạn muốn đảm bảo rằng bạn đang sử dụng phiên bản lệnh nội bộ của một lệnh nào đó, thay vì phiên bản bên ngoài.

## Usage
Cú pháp cơ bản của lệnh `builtin` như sau:
```bash
builtin [options] [arguments]
```

## Common Options
- `-h`, `--help`: Hiển thị thông tin trợ giúp về lệnh `builtin`.
- `-p`: Hiển thị danh sách các lệnh nội bộ có sẵn trong shell.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `builtin`:

1. **Gọi lệnh `echo` nội bộ**:
   ```bash
   builtin echo "Đây là lệnh echo nội bộ."
   ```

2. **Kiểm tra xem lệnh `cd` có phải là lệnh nội bộ không**:
   ```bash
   builtin cd /home/user
   ```

3. **Hiển thị danh sách các lệnh nội bộ**:
   ```bash
   builtin -p
   ```

4. **Sử dụng `builtin` để gọi `type`**:
   ```bash
   builtin type -a echo
   ```

## Tips
- Sử dụng `builtin` khi bạn muốn tránh xung đột với các lệnh bên ngoài có cùng tên.
- Kiểm tra các lệnh nội bộ có sẵn bằng cách sử dụng tùy chọn `-p` để biết thêm thông tin.
- Kết hợp `builtin` với các lệnh khác để tối ưu hóa hiệu suất khi làm việc trong shell.