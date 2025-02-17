# [Linux] Bash getopts Cách sử dụng: Quản lý tham số dòng lệnh

## Overview
Lệnh `getopts` trong Bash được sử dụng để phân tích các tham số dòng lệnh. Nó cho phép bạn dễ dàng xử lý các tùy chọn và đối số mà người dùng cung cấp khi chạy một script.

## Usage
Cú pháp cơ bản của lệnh `getopts` như sau:

```bash
getopts [options] [arguments]
```

## Common Options
- `-a`: Thêm một tùy chọn mới.
- `-b`: Chỉ định một tham số bắt buộc.
- `-c`: Hiển thị thông tin trợ giúp cho người dùng.
- `-d`: Kích hoạt chế độ gỡ lỗi.

## Common Examples

### Ví dụ 1: Phân tích tùy chọn đơn giản
```bash
#!/bin/bash
while getopts "ab:c" option; do
  case $option in
    a) echo "Tùy chọn a được chọn" ;;
    b) echo "Tùy chọn b với giá trị: $OPTARG" ;;
    c) echo "Tùy chọn c được chọn" ;;
    *) echo "Tùy chọn không hợp lệ" ;;
  esac
done
```

### Ví dụ 2: Sử dụng với tham số
```bash
#!/bin/bash
while getopts "f:" option; do
  case $option in
    f) echo "Đường dẫn tệp: $OPTARG" ;;
    *) echo "Tùy chọn không hợp lệ" ;;
  esac
done
```

### Ví dụ 3: Hiển thị thông tin trợ giúp
```bash
#!/bin/bash
show_help() {
  echo "Sử dụng: $0 [-a] [-b value] [-c]"
}

while getopts "ab:c" option; do
  case $option in
    a) echo "Tùy chọn a được chọn" ;;
    b) echo "Tùy chọn b với giá trị: $OPTARG" ;;
    c) echo "Tùy chọn c được chọn" ;;
    *) show_help; exit 1 ;;
  esac
done
```

## Tips
- Luôn kiểm tra giá trị của `$OPTARG` để đảm bảo rằng tham số được cung cấp đúng cách.
- Sử dụng `getopts` trong một vòng lặp `while` để xử lý nhiều tùy chọn cùng một lúc.
- Đảm bảo cung cấp thông tin trợ giúp cho người dùng để họ biết cách sử dụng script của bạn.