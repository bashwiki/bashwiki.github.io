# [Linux] Bash stat Cách sử dụng: Lấy thông tin về tệp tin

## Overview
Lệnh `stat` trong Bash được sử dụng để hiển thị thông tin chi tiết về một tệp tin hoặc thư mục, bao gồm kích thước, quyền truy cập, thời gian sửa đổi và nhiều thông tin khác.

## Usage
Cú pháp cơ bản của lệnh `stat` như sau:

```bash
stat [options] [arguments]
```

## Common Options
- `-c, --format=FORMAT`: Chỉ định định dạng đầu ra.
- `-f, --file-system`: Hiển thị thông tin về hệ thống tệp.
- `--help`: Hiển thị trợ giúp sử dụng.
- `--version`: Hiển thị phiên bản của lệnh.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `stat`:

1. **Xem thông tin cơ bản về một tệp tin:**
   ```bash
   stat filename.txt
   ```

2. **Sử dụng định dạng tùy chỉnh để hiển thị chỉ kích thước tệp:**
   ```bash
   stat -c %s filename.txt
   ```

3. **Hiển thị thông tin về hệ thống tệp:**
   ```bash
   stat -f /
   ```

4. **Xem thông tin chi tiết về một thư mục:**
   ```bash
   stat /path/to/directory
   ```

## Tips
- Sử dụng tùy chọn `-c` để tùy chỉnh đầu ra theo nhu cầu của bạn, giúp dễ dàng trích xuất thông tin cần thiết.
- Kết hợp `stat` với các lệnh khác như `grep` để lọc thông tin cụ thể.
- Thường xuyên kiểm tra quyền truy cập và thời gian sửa đổi của tệp tin để quản lý tệp hiệu quả hơn.