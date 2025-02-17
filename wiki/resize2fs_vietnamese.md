# [Linux] Bash resize2fs Cách sử dụng: Thay đổi kích thước hệ thống tệp ext2/ext3/ext4

## Tổng quan
Lệnh `resize2fs` được sử dụng để thay đổi kích thước của hệ thống tệp ext2, ext3 và ext4. Lệnh này cho phép người dùng mở rộng hoặc thu nhỏ kích thước của hệ thống tệp mà không làm mất dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `resize2fs` như sau:
```bash
resize2fs [tùy chọn] [đối số]
```

## Các tùy chọn phổ biến
- `-f`: Buộc thay đổi kích thước ngay cả khi hệ thống tệp đang được sử dụng.
- `-p`: Hiển thị tiến trình trong khi thay đổi kích thước.
- `[kích thước]`: Kích thước mới mà bạn muốn thay đổi cho hệ thống tệp, có thể được chỉ định bằng đơn vị như K, M, G.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `resize2fs`:

1. Mở rộng hệ thống tệp để sử dụng toàn bộ không gian có sẵn trên phân vùng:
   ```bash
   resize2fs /dev/sda1
   ```

2. Thay đổi kích thước hệ thống tệp thành 20GB:
   ```bash
   resize2fs /dev/sda1 20G
   ```

3. Hiển thị tiến trình khi thay đổi kích thước:
   ```bash
   resize2fs -p /dev/sda1
   ```

4. Buộc thay đổi kích thước ngay cả khi hệ thống tệp đang được sử dụng:
   ```bash
   resize2fs -f /dev/sda1
   ```

## Mẹo
- Trước khi thay đổi kích thước hệ thống tệp, hãy luôn sao lưu dữ liệu quan trọng để tránh mất mát dữ liệu.
- Đảm bảo rằng phân vùng đã được unmount (ngắt kết nối) nếu bạn đang thu nhỏ kích thước hệ thống tệp.
- Kiểm tra tình trạng của hệ thống tệp bằng lệnh `e2fsck` trước khi thực hiện thay đổi kích thước để đảm bảo không có lỗi nào.