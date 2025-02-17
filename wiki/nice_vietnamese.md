# [Linux] Bash nice cách sử dụng: Quản lý độ ưu tiên của tiến trình

## Overview
Lệnh `nice` trong Bash được sử dụng để điều chỉnh độ ưu tiên của các tiến trình khi chúng chạy trên hệ thống. Bằng cách thay đổi độ ưu tiên, bạn có thể kiểm soát tài nguyên CPU mà một tiến trình sử dụng, giúp hệ thống hoạt động mượt mà hơn.

## Usage
Cú pháp cơ bản của lệnh `nice` như sau:

```bash
nice [options] [arguments]
```

## Common Options
- `-n, --adjustment=N`: Điều chỉnh độ ưu tiên của tiến trình. Giá trị N có thể là số dương hoặc âm.
- `-h, --help`: Hiển thị hướng dẫn sử dụng.
- `--version`: Hiển thị phiên bản của lệnh.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `nice`:

1. Chạy một tiến trình với độ ưu tiên thấp hơn:
   ```bash
   nice -n 10 ./my_script.sh
   ```

2. Chạy một lệnh với độ ưu tiên cao hơn:
   ```bash
   nice -n -5 ./my_heavy_process
   ```

3. Kiểm tra độ ưu tiên của một tiến trình đang chạy:
   ```bash
   ps -o pid,ni,cmd
   ```

4. Chạy một lệnh `make` với độ ưu tiên thấp:
   ```bash
   nice -n 15 make
   ```

## Tips
- Sử dụng giá trị âm để tăng độ ưu tiên cho các tiến trình quan trọng.
- Tránh sử dụng độ ưu tiên quá cao cho các tiến trình không cần thiết, vì điều này có thể làm chậm các tiến trình khác.
- Kiểm tra độ ưu tiên của các tiến trình đang chạy bằng lệnh `ps` để quản lý tài nguyên hiệu quả hơn.