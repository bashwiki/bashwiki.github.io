# [Linux] Bash compgen Cách sử dụng: Lệnh tạo danh sách các tên

## Overview
Lệnh `compgen` trong Bash được sử dụng để tạo danh sách các tên, giúp người dùng có thể hoàn thành tự động các lệnh, biến hoặc tên tệp. Nó rất hữu ích trong việc phát triển shell script và tương tác với dòng lệnh.

## Usage
Cú pháp cơ bản của lệnh `compgen` như sau:
```bash
compgen [options] [arguments]
```

## Common Options
- `-A`: Chỉ định loại đối tượng mà bạn muốn tạo danh sách, ví dụ như `alias`, `function`, `variable`, v.v.
- `-a`: Tạo danh sách tất cả các alias hiện có.
- `-b`: Tạo danh sách tất cả các built-in commands.
- `-k`: Tạo danh sách tất cả các từ khóa trong Bash.
- `-c`: Tạo danh sách tất cả các lệnh có thể thực thi.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `compgen`:

1. **Liệt kê tất cả các alias:**
   ```bash
   compgen -a
   ```

2. **Liệt kê tất cả các built-in commands:**
   ```bash
   compgen -b
   ```

3. **Liệt kê tất cả các từ khóa trong Bash:**
   ```bash
   compgen -k
   ```

4. **Liệt kê tất cả các lệnh có thể thực thi:**
   ```bash
   compgen -c
   ```

5. **Tạo danh sách các biến môi trường:**
   ```bash
   compgen -v
   ```

## Tips
- Sử dụng `compgen` kết hợp với `grep` để lọc kết quả, ví dụ: `compgen -c | grep 'git'` để tìm các lệnh liên quan đến git.
- Bạn có thể sử dụng `compgen` trong các script để tự động hoàn thành tên biến hoặc lệnh, giúp tiết kiệm thời gian và giảm lỗi.
- Hãy thử nghiệm với các tùy chọn khác nhau để khám phá tất cả các khả năng của `compgen`.