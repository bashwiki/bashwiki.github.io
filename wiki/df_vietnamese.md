# [Linux] Bash df Cách sử dụng: Hiển thị thông tin về dung lượng ổ đĩa

## Overview
Lệnh `df` trong Bash được sử dụng để hiển thị thông tin về dung lượng ổ đĩa, bao gồm tổng dung lượng, dung lượng đã sử dụng, dung lượng còn trống và điểm gắn kết của các hệ thống tệp. Đây là một công cụ hữu ích để theo dõi tình trạng ổ đĩa của hệ thống.

## Usage
Cú pháp cơ bản của lệnh `df` như sau:
```bash
df [options] [arguments]
```

## Common Options
- `-h`: Hiển thị dung lượng theo định dạng dễ đọc (KB, MB, GB).
- `-T`: Hiển thị loại hệ thống tệp.
- `-a`: Hiển thị tất cả các hệ thống tệp, bao gồm cả những hệ thống tệp có dung lượng 0.
- `-i`: Hiển thị thông tin về số lượng inode thay vì dung lượng ổ đĩa.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `df`:

1. Hiển thị thông tin dung lượng ổ đĩa:
   ```bash
   df
   ```

2. Hiển thị thông tin với định dạng dễ đọc:
   ```bash
   df -h
   ```

3. Hiển thị loại hệ thống tệp:
   ```bash
   df -T
   ```

4. Hiển thị thông tin cho tất cả các hệ thống tệp:
   ```bash
   df -a
   ```

5. Hiển thị thông tin về inode:
   ```bash
   df -i
   ```

## Tips
- Sử dụng tùy chọn `-h` để dễ dàng đọc và hiểu thông tin dung lượng ổ đĩa.
- Kết hợp `df` với lệnh `grep` để tìm kiếm thông tin về một hệ thống tệp cụ thể.
- Thường xuyên kiểm tra dung lượng ổ đĩa để tránh tình trạng đầy ổ đĩa, có thể gây ra sự cố cho hệ thống.