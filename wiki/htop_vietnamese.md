# [Linux] Bash htop Cách sử dụng: Quản lý tiến trình hệ thống

## Tổng quan
Lệnh `htop` là một công cụ tương tác để theo dõi và quản lý các tiến trình đang chạy trên hệ thống. Nó cung cấp giao diện đồ họa thân thiện hơn so với lệnh `top`, cho phép người dùng dễ dàng theo dõi tài nguyên hệ thống như CPU, RAM và các tiến trình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `htop` như sau:

```bash
htop [options] [arguments]
```

## Các tùy chọn phổ biến
- `-h`, `--help`: Hiển thị thông tin trợ giúp về cách sử dụng htop.
- `-s`, `--sort`: Sắp xếp danh sách tiến trình theo tiêu chí nhất định (ví dụ: CPU, bộ nhớ).
- `-p`, `--pid`: Theo dõi một hoặc nhiều tiến trình cụ thể bằng cách chỉ định ID tiến trình.
- `-u`, `--user`: Hiển thị tiến trình của một người dùng cụ thể.

## Ví dụ thường gặp
- Mở htop để theo dõi tất cả các tiến trình:
    ```bash
    htop
    ```

- Sắp xếp tiến trình theo mức sử dụng CPU:
    ```bash
    htop -s PERCENT_CPU
    ```

- Theo dõi một tiến trình cụ thể với ID 1234:
    ```bash
    htop -p 1234
    ```

- Hiển thị tiến trình của người dùng có tên "user1":
    ```bash
    htop -u user1
    ```

## Mẹo
- Sử dụng phím mũi tên để điều hướng giữa các tiến trình và nhấn `F9` để gửi tín hiệu đến tiến trình đã chọn.
- Bạn có thể nhấn `F2` để truy cập vào menu cấu hình và tùy chỉnh giao diện hiển thị theo nhu cầu của mình.
- Để thoát khỏi htop, chỉ cần nhấn `q`.