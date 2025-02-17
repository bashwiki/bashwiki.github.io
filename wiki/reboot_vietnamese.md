# [Linux] Bash reboot cách sử dụng: Khởi động lại hệ thống

## Overview
Lệnh `reboot` trong Bash được sử dụng để khởi động lại hệ thống. Khi lệnh này được thực thi, nó sẽ tắt tất cả các tiến trình đang chạy và khởi động lại máy tính hoặc máy chủ.

## Usage
Cú pháp cơ bản của lệnh `reboot` như sau:
```
reboot [options] [arguments]
```

## Common Options
- `-f`: Bỏ qua các thông báo và khởi động lại ngay lập tức.
- `-p`: Tắt máy và không khởi động lại (tương tự như lệnh `poweroff`).
- `--help`: Hiển thị thông tin trợ giúp về lệnh `reboot`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `reboot`:

1. Khởi động lại hệ thống ngay lập tức:
   ```bash
   reboot
   ```

2. Khởi động lại mà không thông báo:
   ```bash
   reboot -f
   ```

3. Tắt máy mà không khởi động lại:
   ```bash
   reboot -p
   ```

4. Hiển thị thông tin trợ giúp về lệnh `reboot`:
   ```bash
   reboot --help
   ```

## Tips
- Trước khi sử dụng lệnh `reboot`, hãy đảm bảo rằng bạn đã lưu tất cả công việc đang làm để tránh mất dữ liệu.
- Sử dụng tùy chọn `-f` chỉ khi cần thiết, vì nó có thể dẫn đến mất dữ liệu nếu có tiến trình đang chạy.
- Nếu bạn đang quản lý một máy chủ, hãy thông báo cho người dùng trước khi khởi động lại để họ có thể chuẩn bị.