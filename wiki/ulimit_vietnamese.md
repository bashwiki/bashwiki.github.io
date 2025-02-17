# [Linux] Bash ulimit: Quản lý giới hạn tài nguyên hệ thống

## Overview
Lệnh `ulimit` trong Bash được sử dụng để quản lý các giới hạn tài nguyên mà một người dùng hoặc một tiến trình có thể sử dụng trong hệ thống. Điều này giúp bảo vệ hệ thống khỏi việc sử dụng quá mức tài nguyên, như bộ nhớ hoặc số lượng tiến trình.

## Usage
Cú pháp cơ bản của lệnh `ulimit` như sau:

```bash
ulimit [options] [arguments]
```

## Common Options
- `-a`: Hiển thị tất cả các giới hạn hiện tại.
- `-c`: Đặt hoặc hiển thị kích thước tối đa của file core dump.
- `-d`: Đặt hoặc hiển thị kích thước tối đa của bộ nhớ dữ liệu.
- `-f`: Đặt hoặc hiển thị kích thước tối đa của file.
- `-l`: Đặt hoặc hiển thị kích thước tối đa của bộ nhớ có thể được khóa.
- `-m`: Đặt hoặc hiển thị kích thước tối đa của bộ nhớ vật lý.
- `-n`: Đặt hoặc hiển thị số lượng file tối đa mà một tiến trình có thể mở.
- `-s`: Đặt hoặc hiển thị kích thước tối đa của stack.
- `-t`: Đặt hoặc hiển thị thời gian tối đa cho một tiến trình.
- `-u`: Đặt hoặc hiển thị số lượng tiến trình tối đa mà một người dùng có thể tạo ra.

## Common Examples
- Hiển thị tất cả các giới hạn hiện tại:
    ```bash
    ulimit -a
    ```

- Đặt kích thước tối đa của file core dump là 100MB:
    ```bash
    ulimit -c 100000
    ```

- Đặt số lượng file tối đa mà một tiến trình có thể mở là 1024:
    ```bash
    ulimit -n 1024
    ```

- Đặt kích thước tối đa của stack là 8MB:
    ```bash
    ulimit -s 8192
    ```

## Tips
- Nên kiểm tra các giới hạn hiện tại trước khi thay đổi để tránh gây ra sự cố cho hệ thống.
- Sử dụng lệnh `ulimit` trong các script để đảm bảo rằng các tiến trình chạy trong môi trường đã được cấu hình đúng.
- Một số giới hạn có thể yêu cầu quyền root để thay đổi, vì vậy hãy đảm bảo bạn có quyền thích hợp khi thực hiện các thay đổi.