# [Linux] Bash date cách sử dụng: Lấy và định dạng ngày giờ hiện tại

## Overview
Lệnh `date` trong Bash được sử dụng để hiển thị hoặc thiết lập ngày và giờ hệ thống. Nó cho phép người dùng xem thông tin thời gian hiện tại theo nhiều định dạng khác nhau.

## Usage
Cú pháp cơ bản của lệnh là:

```bash
date [options] [arguments]
```

## Common Options
- `+FORMAT`: Định dạng đầu ra theo chuỗi FORMAT.
- `-u`: Hiển thị thời gian theo giờ UTC (Coordinated Universal Time).
- `-d STRING`: Hiển thị ngày giờ cho một chuỗi cụ thể.
- `-s STRING`: Thiết lập ngày giờ hệ thống từ chuỗi cụ thể.

## Common Examples
- Hiển thị ngày giờ hiện tại:
    ```bash
    date
    ```

- Hiển thị ngày giờ theo định dạng cụ thể (ví dụ: năm-tháng-ngày):
    ```bash
    date +"%Y-%m-%d"
    ```

- Hiển thị thời gian theo giờ UTC:
    ```bash
    date -u
    ```

- Hiển thị ngày giờ cho một chuỗi cụ thể (ví dụ: "2 days ago"):
    ```bash
    date -d "2 days ago"
    ```

- Thiết lập ngày giờ hệ thống (cần quyền root):
    ```bash
    sudo date -s "2023-10-01 12:00:00"
    ```

## Tips
- Sử dụng định dạng `%H:%M:%S` để chỉ hiển thị giờ, phút và giây.
- Bạn có thể lưu đầu ra của lệnh `date` vào một biến để sử dụng sau này:
    ```bash
    current_date=$(date +"%Y-%m-%d")
    ```
- Kiểm tra múi giờ hiện tại bằng lệnh `date +%Z`.