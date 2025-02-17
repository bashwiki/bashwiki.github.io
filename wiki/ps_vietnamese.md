# [Linux] Bash ps Cách sử dụng: Hiển thị thông tin tiến trình

## Tổng quan
Lệnh `ps` trong Bash được sử dụng để hiển thị thông tin về các tiến trình đang chạy trên hệ thống. Nó cho phép người dùng xem các tiến trình, trạng thái của chúng và các thông tin khác liên quan.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ps` như sau:
```
ps [options] [arguments]
```

## Các tùy chọn phổ biến
- `-e` hoặc `-A`: Hiển thị tất cả các tiến trình.
- `-f`: Hiển thị thông tin chi tiết về tiến trình.
- `-u [user]`: Hiển thị tiến trình của một người dùng cụ thể.
- `-aux`: Hiển thị tất cả các tiến trình với thông tin chi tiết.
- `--sort`: Sắp xếp danh sách tiến trình theo một tiêu chí nhất định.

## Ví dụ phổ biến
- Hiển thị tất cả các tiến trình đang chạy:
  ```bash
  ps -e
  ```

- Hiển thị thông tin chi tiết về các tiến trình:
  ```bash
  ps -f
  ```

- Hiển thị tiến trình của người dùng cụ thể:
  ```bash
  ps -u username
  ```

- Hiển thị tất cả các tiến trình với thông tin chi tiết:
  ```bash
  ps aux
  ```

- Sắp xếp danh sách tiến trình theo mức sử dụng CPU:
  ```bash
  ps aux --sort=-%cpu
  ```

## Mẹo
- Sử dụng `ps aux | grep [tên tiến trình]` để tìm kiếm một tiến trình cụ thể.
- Kết hợp `ps` với các lệnh khác như `grep` để lọc thông tin cần thiết.
- Thường xuyên kiểm tra tiến trình để phát hiện các vấn đề về hiệu suất hệ thống.