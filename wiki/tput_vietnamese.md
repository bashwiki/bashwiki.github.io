# [Linux] Bash tput Cách sử dụng: Điều chỉnh định dạng đầu ra trong terminal

## Tổng quan
Lệnh `tput` trong Bash được sử dụng để điều chỉnh định dạng đầu ra trên terminal. Nó cho phép người dùng thay đổi các thuộc tính như màu sắc, kiểu chữ và vị trí con trỏ, giúp cải thiện trải nghiệm người dùng trong môi trường dòng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `tput` như sau:
```
tput [options] [arguments]
```

## Các tùy chọn phổ biến
- `setaf [n]`: Đặt màu chữ (foreground) với mã màu `n`.
- `setab [n]`: Đặt màu nền (background) với mã màu `n`.
- `bold`: Bật chế độ chữ đậm.
- `smso`: Bật chế độ in nghiêng (standout mode).
- `rmso`: Tắt chế độ in nghiêng.
- `clear`: Xóa màn hình terminal.

## Ví dụ phổ biến
1. **Thay đổi màu chữ**:
   ```bash
   tput setaf 1; echo "Đây là chữ màu đỏ"
   ```

2. **Thay đổi màu nền**:
   ```bash
   tput setab 4; echo "Đây là nền màu xanh dương"
   ```

3. **Bật chế độ chữ đậm**:
   ```bash
   tput bold; echo "Đây là chữ đậm"
   ```

4. **Xóa màn hình**:
   ```bash
   tput clear
   ```

5. **Kết hợp nhiều tùy chọn**:
   ```bash
   tput setaf 2; tput setab 7; echo "Chữ xanh trên nền trắng"
   tput sgr0  # Đặt lại định dạng về mặc định
   ```

## Mẹo
- Sử dụng `tput sgr0` để đặt lại tất cả các thuộc tính về mặc định sau khi thay đổi.
- Bạn có thể tìm hiểu mã màu bằng cách tham khảo tài liệu hoặc thử nghiệm với các giá trị từ 0 đến 7 cho màu cơ bản.
- Kết hợp `tput` với các lệnh khác trong Bash để tạo ra các script tương tác và thân thiện hơn với người dùng.