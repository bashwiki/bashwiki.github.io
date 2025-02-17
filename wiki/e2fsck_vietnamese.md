# [Linux] Bash e2fsck Cách sử dụng: Kiểm tra và sửa lỗi hệ thống tệp ext2/ext3/ext4

## Tổng quan
Lệnh `e2fsck` được sử dụng để kiểm tra và sửa chữa các lỗi trong hệ thống tệp ext2, ext3 và ext4 trên các hệ điều hành Linux. Nó giúp đảm bảo rằng hệ thống tệp hoạt động bình thường và không có lỗi có thể gây ra mất dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `e2fsck` như sau:

```bash
e2fsck [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-p`: Tự động sửa chữa các lỗi mà không cần xác nhận.
- `-f`: Kiểm tra hệ thống tệp ngay cả khi nó không được đánh dấu là cần kiểm tra.
- `-n`: Chỉ kiểm tra mà không sửa chữa, rất hữu ích để xem lỗi mà không thay đổi gì.
- `-c`: Kiểm tra các khối xấu trên đĩa.
- `-y`: Tự động trả lời "có" cho tất cả các câu hỏi.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `e2fsck`:

1. Kiểm tra một hệ thống tệp:
   ```bash
   e2fsck /dev/sda1
   ```

2. Tự động sửa chữa lỗi mà không cần xác nhận:
   ```bash
   e2fsck -p /dev/sda1
   ```

3. Kiểm tra và sửa chữa hệ thống tệp với xác nhận:
   ```bash
   e2fsck -f /dev/sda1
   ```

4. Kiểm tra mà không sửa chữa:
   ```bash
   e2fsck -n /dev/sda1
   ```

5. Kiểm tra các khối xấu:
   ```bash
   e2fsck -c /dev/sda1
   ```

## Mẹo
- Luôn sao lưu dữ liệu quan trọng trước khi chạy `e2fsck`, đặc biệt là khi sửa chữa hệ thống tệp.
- Nên chạy `e2fsck` khi hệ thống tệp không được gắn kết để tránh các vấn đề không mong muốn.
- Sử dụng tùy chọn `-n` để kiểm tra trước khi thực hiện sửa chữa thực tế, giúp bạn hiểu rõ hơn về các lỗi có thể xảy ra.