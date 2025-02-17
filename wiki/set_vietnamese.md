# [Linux] Bash set: Thiết lập biến và tùy chọn trong Bash

## Overview
Lệnh `set` trong Bash được sử dụng để thiết lập các biến và tùy chọn cho shell. Nó cho phép người dùng điều chỉnh cách mà shell hoạt động và xử lý các biến môi trường.

## Usage
Cú pháp cơ bản của lệnh `set` như sau:

```bash
set [options] [arguments]
```

## Common Options
Dưới đây là một số tùy chọn phổ biến của lệnh `set` cùng với giải thích ngắn gọn:

- `-e`: Dừng thực thi khi gặp lỗi.
- `-u`: Dừng thực thi khi sử dụng biến chưa được định nghĩa.
- `-x`: Hiển thị các lệnh trước khi thực thi chúng, hữu ích cho việc gỡ lỗi.
- `-o`: Thiết lập các tùy chọn khác nhau, ví dụ như `-o noclobber` để ngăn chặn việc ghi đè lên các tệp.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `set`:

1. **Dừng thực thi khi gặp lỗi:**
   ```bash
   set -e
   command1
   command2  # Nếu command1 gặp lỗi, command2 sẽ không được thực thi.
   ```

2. **Hiển thị các lệnh trước khi thực thi:**
   ```bash
   set -x
   echo "Hello, World!"
   ```

3. **Ngăn chặn ghi đè lên tệp:**
   ```bash
   set -o noclobber
   echo "New content" > existing_file.txt  # Sẽ báo lỗi nếu existing_file.txt đã tồn tại.
   ```

4. **Sử dụng biến chưa được định nghĩa:**
   ```bash
   set -u
   echo $undefined_variable  # Sẽ báo lỗi nếu biến chưa được định nghĩa.
   ```

## Tips
- Sử dụng `set -e` để đảm bảo rằng script của bạn dừng lại khi gặp lỗi, giúp dễ dàng phát hiện và sửa lỗi.
- Kết hợp `set -x` với các lệnh phức tạp để theo dõi quá trình thực thi và dễ dàng gỡ lỗi.
- Hãy cẩn thận với `set -u`, vì nó có thể làm cho script của bạn dừng lại nếu bạn quên định nghĩa một biến.