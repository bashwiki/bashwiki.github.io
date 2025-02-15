# [리눅스] Bash umount 사용법

## Tổng quan
Lệnh `umount` trong Bash được sử dụng để gỡ bỏ (unmount) một hệ thống tệp (filesystem) đã được gắn kết (mounted) trên một điểm gắn kết (mount point). Mục đích chính của lệnh này là giải phóng tài nguyên hệ thống và đảm bảo rằng không có dữ liệu nào bị mất khi ngắt kết nối thiết bị lưu trữ hoặc hệ thống tệp.

## Cú pháp
Cú pháp cơ bản của lệnh `umount` như sau:

```bash
umount [tùy chọn] <điểm_gắn_kết|thiết_bị>
```

### Tùy chọn phổ biến
- `-a`: Gỡ bỏ tất cả các hệ thống tệp được gắn kết trong tệp `/etc/mtab`.
- `-f`: Gỡ bỏ hệ thống tệp ngay cả khi nó đang bận (force unmount).
- `-l`: Gỡ bỏ hệ thống tệp một cách lười biếng (lazy unmount), nghĩa là nó sẽ được gỡ bỏ khi không còn sử dụng nữa.
- `-r`: Gỡ bỏ hệ thống tệp và cố gắng khôi phục nếu có lỗi xảy ra.

## Ví dụ
### Ví dụ 1: Gỡ bỏ một hệ thống tệp cụ thể
Giả sử bạn đã gắn kết một thiết bị USB vào `/mnt/usb`, bạn có thể gỡ bỏ nó bằng cách sử dụng lệnh sau:

```bash
umount /mnt/usb
```

### Ví dụ 2: Gỡ bỏ tất cả các hệ thống tệp
Nếu bạn muốn gỡ bỏ tất cả các hệ thống tệp được gắn kết, bạn có thể sử dụng tùy chọn `-a`:

```bash
umount -a
```

## Mẹo
- Trước khi gỡ bỏ một hệ thống tệp, hãy đảm bảo rằng không có tiến trình nào đang sử dụng nó. Bạn có thể sử dụng lệnh `lsof` để kiểm tra các tệp đang mở.
- Sử dụng tùy chọn `-l` nếu bạn không thể gỡ bỏ hệ thống tệp ngay lập tức do nó đang bận, điều này sẽ giúp tránh mất dữ liệu.
- Luôn kiểm tra trạng thái của hệ thống tệp sau khi gỡ bỏ để đảm bảo rằng không có lỗi xảy ra.