# [Linux] Bash tune2fs cách sử dụng: Chỉnh sửa các thuộc tính của hệ thống tệp ext2/ext3/ext4

## Overview
Lệnh `tune2fs` được sử dụng để điều chỉnh các thuộc tính của hệ thống tệp ext2, ext3 và ext4 trên Linux. Nó cho phép người dùng thay đổi các thông số như kích thước khối, thời gian kiểm tra, và nhiều tùy chọn khác để tối ưu hóa hiệu suất và bảo trì hệ thống tệp.

## Usage
Cú pháp cơ bản của lệnh `tune2fs` như sau:
```
tune2fs [options] [arguments]
```

## Common Options
- `-c <count>`: Đặt số lần tối đa mà hệ thống tệp có thể được gắn kết trước khi kiểm tra.
- `-i <interval>`: Đặt khoảng thời gian giữa các lần kiểm tra hệ thống tệp.
- `-m <reserved-blocks>`: Đặt tỷ lệ phần trăm không gian đĩa được dự trữ cho người dùng root.
- `-O <feature>`: Bật một tính năng mới cho hệ thống tệp.
- `-L <label>`: Đặt nhãn cho hệ thống tệp.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng `tune2fs`:

1. Đặt số lần tối đa gắn kết trước khi kiểm tra:
   ```bash
   tune2fs -c 20 /dev/sda1
   ```

2. Đặt khoảng thời gian giữa các lần kiểm tra là 30 ngày:
   ```bash
   tune2fs -i 30d /dev/sda1
   ```

3. Đặt tỷ lệ phần trăm không gian đĩa dự trữ cho root là 5%:
   ```bash
   tune2fs -m 5 /dev/sda1
   ```

4. Bật tính năng "has_journal" cho hệ thống tệp:
   ```bash
   tune2fs -O has_journal /dev/sda1
   ```

5. Đặt nhãn cho hệ thống tệp:
   ```bash
   tune2fs -L MyLabel /dev/sda1
   ```

## Tips
- Trước khi thực hiện bất kỳ thay đổi nào với `tune2fs`, hãy sao lưu dữ liệu quan trọng để tránh mất mát dữ liệu.
- Kiểm tra trạng thái của hệ thống tệp bằng lệnh `dumpe2fs` trước khi thay đổi các thuộc tính.
- Sử dụng `tune2fs` với quyền root để đảm bảo bạn có đủ quyền truy cập để thực hiện các thay đổi.