# [Linux] Bash mount cách sử dụng: Gắn kết hệ thống tệp

## Tổng quan
Lệnh `mount` trong Bash được sử dụng để gắn kết một hệ thống tệp vào một điểm gắn kết trong cây thư mục của hệ điều hành. Điều này cho phép người dùng truy cập vào các tệp và thư mục trên thiết bị lưu trữ ngoài như ổ đĩa cứng, USB hay các phân vùng khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mount` như sau:

```bash
mount [options] [device] [mount_point]
```

## Các tùy chọn phổ biến
- `-t type`: Chỉ định loại hệ thống tệp (ví dụ: ext4, ntfs).
- `-o options`: Chỉ định các tùy chọn gắn kết (ví dụ: ro cho chế độ chỉ đọc).
- `-a`: Gắn kết tất cả các hệ thống tệp được chỉ định trong `/etc/fstab`.
- `-r`: Gắn kết hệ thống tệp ở chế độ chỉ đọc.

## Ví dụ phổ biến
1. Gắn kết một ổ USB:
   ```bash
   mount /dev/sdb1 /mnt/usb
   ```

2. Gắn kết một phân vùng NTFS:
   ```bash
   mount -t ntfs-3g /dev/sdc1 /mnt/windows -o rw
   ```

3. Gắn kết tất cả các hệ thống tệp trong `/etc/fstab`:
   ```bash
   mount -a
   ```

4. Gắn kết một phân vùng ở chế độ chỉ đọc:
   ```bash
   mount -o ro /dev/sda1 /mnt/data
   ```

## Mẹo
- Luôn kiểm tra các phân vùng đã gắn kết bằng lệnh `df -h` để đảm bảo rằng bạn không gắn kết một phân vùng đã được sử dụng.
- Đảm bảo rằng bạn có quyền truy cập cần thiết để gắn kết các thiết bị, thường là quyền root.
- Sử dụng lệnh `umount` để gỡ bỏ gắn kết các hệ thống tệp khi không còn cần thiết, tránh mất dữ liệu.