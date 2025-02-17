# [Linux] Bash shopt: [quản lý các tùy chọn shell]

## Overview
Lệnh `shopt` trong Bash được sử dụng để quản lý các tùy chọn shell. Nó cho phép người dùng bật hoặc tắt các tính năng bổ sung của shell, giúp tùy chỉnh hành vi của môi trường làm việc.

## Usage
Cú pháp cơ bản của lệnh `shopt` như sau:
```bash
shopt [options] [arguments]
```

## Common Options
- `-s`: Bật một tùy chọn.
- `-u`: Tắt một tùy chọn.
- `-p`: Hiển thị tất cả các tùy chọn hiện tại và trạng thái của chúng.

## Common Examples

### Bật một tùy chọn
Để bật tùy chọn `cdable_vars`, cho phép sử dụng biến trong lệnh `cd`, bạn có thể sử dụng:
```bash
shopt -s cdable_vars
```

### Tắt một tùy chọn
Để tắt tùy chọn `cdable_vars`, bạn có thể sử dụng:
```bash
shopt -u cdable_vars
```

### Hiển thị tất cả các tùy chọn
Để xem tất cả các tùy chọn hiện tại và trạng thái của chúng, bạn có thể sử dụng:
```bash
shopt -p
```

### Kiểm tra trạng thái của một tùy chọn
Để kiểm tra xem một tùy chọn cụ thể đã được bật hay chưa, bạn có thể sử dụng:
```bash
shopt cdable_vars
```

## Tips
- Hãy kiểm tra các tùy chọn có sẵn bằng cách sử dụng `shopt -p` để biết những gì có thể được tùy chỉnh.
- Sử dụng `shopt` trong tệp cấu hình `.bashrc` của bạn để tự động áp dụng các tùy chọn khi mở terminal.
- Cẩn thận với các tùy chọn có thể ảnh hưởng đến cách thức hoạt động của các lệnh khác trong shell.