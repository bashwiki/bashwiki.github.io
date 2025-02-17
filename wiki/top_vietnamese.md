# [Linux] Bash top cách sử dụng: Theo dõi tài nguyên hệ thống

## Tổng quan
Lệnh `top` trong Bash được sử dụng để hiển thị thông tin về các tiến trình đang chạy trên hệ thống, cũng như mức sử dụng tài nguyên như CPU và bộ nhớ. Nó cung cấp một cái nhìn trực quan và liên tục về hiệu suất của hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `top` như sau:

```bash
top [options]
```

## Tùy chọn phổ biến
- `-d <seconds>`: Đặt khoảng thời gian cập nhật giữa các lần hiển thị (mặc định là 3 giây).
- `-p <pid>`: Chỉ hiển thị thông tin cho tiến trình có ID được chỉ định.
- `-u <user>`: Chỉ hiển thị các tiến trình của người dùng cụ thể.

## Ví dụ phổ biến
- Để khởi động `top` với thông tin mặc định:
  ```bash
  top
  ```

- Để cập nhật mỗi 5 giây:
  ```bash
  top -d 5
  ```

- Để chỉ hiển thị tiến trình của một người dùng cụ thể:
  ```bash
  top -u username
  ```

- Để theo dõi một tiến trình cụ thể bằng ID:
  ```bash
  top -p 1234
  ```

## Mẹo
- Nhấn `h` trong giao diện `top` để xem hướng dẫn sử dụng nhanh.
- Sử dụng phím `M` để sắp xếp các tiến trình theo mức sử dụng bộ nhớ.
- Nhấn `P` để sắp xếp theo mức sử dụng CPU.
- Để thoát khỏi `top`, nhấn `q`.