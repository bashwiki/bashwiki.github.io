# [Linux] Bash bash lệnh: Thực thi lệnh trong shell

## Overview
Lệnh Bash là một công cụ mạnh mẽ cho phép người dùng thực thi các lệnh trong môi trường shell. Nó là một phần của GNU Project và thường được sử dụng để tự động hóa các tác vụ, quản lý hệ thống và thực hiện các lệnh trong dòng lệnh.

## Usage
Cú pháp cơ bản của lệnh Bash như sau:
```bash
bash [options] [arguments]
```

## Common Options
- `-c`: Chạy lệnh được chỉ định trong chuỗi.
- `-i`: Chạy Bash trong chế độ tương tác.
- `-l`: Khởi động một shell đăng nhập.
- `-s`: Đọc lệnh từ stdin.

## Common Examples
1. Chạy một lệnh đơn giản:
   ```bash
   bash -c 'echo "Hello, World!"'
   ```

2. Khởi động một shell tương tác:
   ```bash
   bash -i
   ```

3. Chạy một script từ một tệp:
   ```bash
   bash myscript.sh
   ```

4. Chạy lệnh từ stdin:
   ```bash
   echo 'echo "Running from stdin"' | bash -s
   ```

## Tips
- Sử dụng `bash -l` để khởi động một shell đăng nhập, điều này có thể hữu ích cho việc thiết lập môi trường.
- Khi chạy script, hãy đảm bảo rằng tệp có quyền thực thi bằng cách sử dụng `chmod +x myscript.sh`.
- Thường xuyên kiểm tra các biến môi trường để đảm bảo rằng chúng được thiết lập đúng cách trong shell của bạn.