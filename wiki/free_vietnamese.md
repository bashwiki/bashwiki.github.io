# [Linux] Bash free: Hiển thị thông tin bộ nhớ hệ thống

## Overview
Lệnh `free` trong Bash được sử dụng để hiển thị thông tin về bộ nhớ hệ thống, bao gồm bộ nhớ RAM và bộ nhớ swap. Nó giúp người dùng theo dõi tình trạng sử dụng bộ nhớ của hệ thống một cách nhanh chóng và dễ dàng.

## Usage
Cú pháp cơ bản của lệnh `free` như sau:
```bash
free [options] [arguments]
```

## Common Options
- `-h`: Hiển thị thông tin bộ nhớ theo định dạng dễ đọc (kB, MB, GB).
- `-m`: Hiển thị thông tin bộ nhớ theo megabyte.
- `-g`: Hiển thị thông tin bộ nhớ theo gigabyte.
- `-s <seconds>`: Cập nhật thông tin bộ nhớ sau mỗi khoảng thời gian xác định (tính bằng giây).
- `-t`: Hiển thị tổng số bộ nhớ sử dụng và bộ nhớ khả dụng.

## Common Examples
Dưới đây là một số ví dụ thực tế khi sử dụng lệnh `free`.

1. Hiển thị thông tin bộ nhớ cơ bản:
   ```bash
   free
   ```

2. Hiển thị thông tin bộ nhớ theo megabyte:
   ```bash
   free -m
   ```

3. Hiển thị thông tin bộ nhớ theo gigabyte:
   ```bash
   free -g
   ```

4. Cập nhật thông tin bộ nhớ mỗi 5 giây:
   ```bash
   free -s 5
   ```

5. Hiển thị tổng số bộ nhớ sử dụng và bộ nhớ khả dụng:
   ```bash
   free -t
   ```

## Tips
- Sử dụng tùy chọn `-h` để dễ dàng đọc thông tin bộ nhớ mà không cần phải tính toán.
- Kết hợp lệnh `free` với lệnh `watch` để theo dõi tình trạng bộ nhớ theo thời gian thực:
  ```bash
  watch free -h
  ```
- Thường xuyên kiểm tra tình trạng bộ nhớ có thể giúp bạn phát hiện sớm các vấn đề về hiệu suất hệ thống.