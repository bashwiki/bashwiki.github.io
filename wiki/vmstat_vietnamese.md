# [Linux] Bash vmstat Cách sử dụng: Theo dõi hiệu suất hệ thống

## Overview
Lệnh `vmstat` (Virtual Memory Statistics) được sử dụng để theo dõi hiệu suất hệ thống, cung cấp thông tin về bộ nhớ, quy trình, và các hoạt động I/O. Nó giúp người dùng hiểu rõ hơn về tình trạng tài nguyên hệ thống và phát hiện các vấn đề tiềm ẩn.

## Usage
Cú pháp cơ bản của lệnh `vmstat` như sau:
```
vmstat [options] [arguments]
```

## Common Options
- `-a`: Hiển thị thông tin bộ nhớ ảo.
- `-m`: Hiển thị thông tin về bộ nhớ đã sử dụng và bộ nhớ còn lại.
- `-s`: Hiển thị thống kê bộ nhớ tổng quát.
- `-t`: Thêm dấu thời gian vào đầu mỗi dòng đầu ra.
- `interval`: Thời gian (tính bằng giây) giữa các lần cập nhật thông tin.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `vmstat`:

1. **Hiển thị thông tin hệ thống cơ bản:**
   ```bash
   vmstat
   ```

2. **Theo dõi thông tin mỗi 2 giây:**
   ```bash
   vmstat 2
   ```

3. **Hiển thị thông tin bộ nhớ ảo:**
   ```bash
   vmstat -a
   ```

4. **Hiển thị thống kê bộ nhớ tổng quát:**
   ```bash
   vmstat -s
   ```

5. **Theo dõi thông tin với dấu thời gian:**
   ```bash
   vmstat -t 1
   ```

## Tips
- Sử dụng `vmstat` cùng với các lệnh khác như `top` hoặc `htop` để có cái nhìn tổng quan hơn về hiệu suất hệ thống.
- Theo dõi thường xuyên để phát hiện các vấn đề về hiệu suất trước khi chúng trở thành sự cố nghiêm trọng.
- Kết hợp `vmstat` với các công cụ giám sát khác để có dữ liệu chi tiết hơn về hiệu suất hệ thống.