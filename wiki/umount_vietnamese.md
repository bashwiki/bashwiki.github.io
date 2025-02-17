# [Linux] Bash umount: Ngắt kết nối hệ thống tập tin

## Overview
Lệnh `umount` được sử dụng để ngắt kết nối một hệ thống tập tin đã được gắn kết (mount) trên hệ thống Linux. Khi bạn không còn cần truy cập vào một thiết bị lưu trữ hoặc hệ thống tập tin nào đó, bạn có thể sử dụng lệnh này để giải phóng tài nguyên và đảm bảo rằng không có dữ liệu nào bị mất.

## Usage
Cú pháp cơ bản của lệnh `umount` như sau:

```bash
umount [options] [arguments]
```

## Common Options
- `-a`: Ngắt kết nối tất cả các hệ thống tập tin được gắn kết trong `/etc/mtab`.
- `-f`: Ngắt kết nối một hệ thống tập tin ngay cả khi nó đang được sử dụng.
- `-l`: Ngắt kết nối một hệ thống tập tin một cách "lazy", tức là sẽ ngắt kết nối khi không còn sử dụng nữa.
- `-r`: Ngắt kết nối và cố gắng sửa chữa nếu có lỗi.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `umount`:

1. Ngắt kết nối một thiết bị cụ thể:
   ```bash
   umount /dev/sdb1
   ```

2. Ngắt kết nối một hệ thống tập tin đã được gắn kết tại một thư mục:
   ```bash
   umount /mnt/usb
   ```

3. Ngắt kết nối tất cả các hệ thống tập tin:
   ```bash
   umount -a
   ```

4. Ngắt kết nối một hệ thống tập tin một cách "lazy":
   ```bash
   umount -l /mnt/usb
   ```

## Tips
- Trước khi ngắt kết nối, hãy đảm bảo rằng không có tiến trình nào đang sử dụng hệ thống tập tin đó để tránh mất dữ liệu.
- Sử dụng lệnh `lsof` để kiểm tra xem có tiến trình nào đang sử dụng hệ thống tập tin trước khi thực hiện lệnh `umount`.
- Nếu bạn gặp khó khăn trong việc ngắt kết nối, hãy thử sử dụng tùy chọn `-f` để buộc ngắt kết nối, nhưng hãy cẩn thận với dữ liệu có thể bị mất.