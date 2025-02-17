# [Linux] Bash dpkg Cách sử dụng: Quản lý gói phần mềm

## Tổng quan
Lệnh `dpkg` là một công cụ quản lý gói trên hệ điều hành Debian và các bản phân phối dựa trên Debian như Ubuntu. Nó cho phép người dùng cài đặt, gỡ bỏ và quản lý các gói phần mềm trên hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dpkg` như sau:
```
dpkg [options] [arguments]
```

## Các tùy chọn phổ biến
- `-i`, `--install`: Cài đặt một gói phần mềm.
- `-r`, `--remove`: Gỡ bỏ một gói phần mềm.
- `-l`, `--list`: Liệt kê tất cả các gói đã cài đặt.
- `-s`, `--status`: Hiển thị trạng thái của một gói phần mềm.
- `-c`, `--contents`: Hiển thị nội dung của một gói đã được cài đặt.

## Ví dụ thường gặp
1. **Cài đặt một gói phần mềm:**
   ```bash
   sudo dpkg -i ten-goi.deb
   ```

2. **Gỡ bỏ một gói phần mềm:**
   ```bash
   sudo dpkg -r ten-goi
   ```

3. **Liệt kê tất cả các gói đã cài đặt:**
   ```bash
   dpkg -l
   ```

4. **Kiểm tra trạng thái của một gói:**
   ```bash
   dpkg -s ten-goi
   ```

5. **Xem nội dung của một gói:**
   ```bash
   dpkg -c ten-goi.deb
   ```

## Mẹo
- Luôn kiểm tra trạng thái của gói sau khi cài đặt hoặc gỡ bỏ để đảm bảo không có lỗi xảy ra.
- Sử dụng `dpkg` kết hợp với `apt` để quản lý gói hiệu quả hơn, vì `apt` có thể tự động xử lý các phụ thuộc.
- Nếu gặp lỗi khi cài đặt gói, hãy thử sử dụng lệnh `apt-get install -f` để sửa chữa các vấn đề phụ thuộc.