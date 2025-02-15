# [리눅스] Bash mount 사용법

## Tổng quan
Lệnh `mount` trong Bash được sử dụng để gắn kết (mount) một hệ thống tệp vào một điểm gắn kết trong hệ thống tệp hiện tại. Điều này cho phép người dùng truy cập và quản lý các tệp và thư mục trên thiết bị lưu trữ ngoài, như ổ đĩa cứng, USB, hoặc các phân vùng khác. Lệnh này rất quan trọng trong việc quản lý hệ thống tệp trên các hệ điều hành dựa trên Unix.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mount` như sau:

```bash
mount [tùy chọn] [thiết bị] [điểm gắn kết]
```

### Tùy chọn phổ biến:
- `-t <loại>`: Chỉ định loại hệ thống tệp (ví dụ: ext4, ntfs, vfat).
- `-o <tùy chọn>`: Chỉ định các tùy chọn gắn kết khác nhau (ví dụ: ro cho chỉ đọc, rw cho đọc và ghi).
- `-a`: Gắn tất cả các hệ thống tệp được liệt kê trong `/etc/fstab`.
- `-r`: Gắn hệ thống tệp chỉ đọc.

## Ví dụ
### Ví dụ 1: Gắn một ổ USB
Giả sử bạn muốn gắn một ổ USB có tên là `/dev/sdb1` vào thư mục `/mnt/usb`, bạn có thể sử dụng lệnh sau:

```bash
sudo mount /dev/sdb1 /mnt/usb
```

### Ví dụ 2: Gắn một phân vùng với tùy chọn chỉ đọc
Nếu bạn muốn gắn một phân vùng NTFS chỉ đọc, bạn có thể sử dụng lệnh sau:

```bash
sudo mount -t ntfs -o ro /dev/sdc1 /mnt/ntfs
```

## Mẹo
- Trước khi gắn một thiết bị, hãy chắc chắn rằng nó không bị gắn kết trước đó bằng cách sử dụng lệnh `df` hoặc `lsblk`.
- Để gỡ bỏ một hệ thống tệp đã gắn kết, sử dụng lệnh `umount` theo sau là điểm gắn kết hoặc thiết bị.
- Luôn kiểm tra quyền truy cập và quyền sở hữu của điểm gắn kết để đảm bảo rằng bạn có quyền truy cập cần thiết.
- Đối với các thiết bị lưu trữ di động, hãy luôn gỡ bỏ thiết bị một cách an toàn trước khi rút ra để tránh mất dữ liệu.