# [Linux] Bash renice: Thay đổi ưu tiên tiến trình

## Overview
Lệnh `renice` được sử dụng để thay đổi mức độ ưu tiên của một hoặc nhiều tiến trình đang chạy trên hệ thống. Mức độ ưu tiên này ảnh hưởng đến cách mà hệ điều hành phân bổ tài nguyên CPU cho các tiến trình.

## Usage
Cú pháp cơ bản của lệnh `renice` như sau:

```bash
renice [options] [arguments]
```

## Common Options
- `-n, --priority`: Xác định mức độ ưu tiên mới cho tiến trình. Giá trị có thể là số nguyên từ -20 (ưu tiên cao nhất) đến 19 (ưu tiên thấp nhất).
- `-p, --pid`: Chỉ định ID tiến trình (PID) mà bạn muốn thay đổi mức độ ưu tiên.
- `-g, --pgrp`: Thay đổi mức độ ưu tiên cho tất cả các tiến trình trong nhóm tiến trình có ID được chỉ định.
- `-u, --user`: Thay đổi mức độ ưu tiên cho tất cả các tiến trình của người dùng được chỉ định.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `renice`:

1. Thay đổi mức độ ưu tiên của một tiến trình cụ thể:
   ```bash
   renice -n 10 -p 1234
   ```
   (Thay đổi mức độ ưu tiên của tiến trình có PID 1234 thành 10.)

2. Thay đổi mức độ ưu tiên cho tất cả các tiến trình của một người dùng:
   ```bash
   renice -n 5 -u username
   ```
   (Thay đổi mức độ ưu tiên của tất cả các tiến trình của người dùng "username" thành 5.)

3. Thay đổi mức độ ưu tiên cho một nhóm tiến trình:
   ```bash
   renice -n -5 -g 5678
   ```
   (Thay đổi mức độ ưu tiên cho tất cả các tiến trình trong nhóm có ID 5678 thành -5.)

## Tips
- Hãy cẩn thận khi thay đổi mức độ ưu tiên của các tiến trình quan trọng, vì điều này có thể ảnh hưởng đến hiệu suất hệ thống.
- Sử dụng lệnh `top` hoặc `htop` để theo dõi các tiến trình và mức độ ưu tiên của chúng trước khi thực hiện thay đổi.
- Chỉ thay đổi mức độ ưu tiên cho các tiến trình mà bạn có quyền truy cập, nếu không bạn sẽ nhận được thông báo lỗi.