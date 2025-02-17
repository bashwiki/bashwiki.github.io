# [Linux] Bash netstat Cách sử dụng: Kiểm tra kết nối mạng

## Tổng quan
Lệnh `netstat` là một công cụ mạnh mẽ trong Bash, được sử dụng để hiển thị thông tin về các kết nối mạng, bảng định tuyến, và các giao thức mạng đang hoạt động trên hệ thống. Nó giúp người dùng theo dõi và quản lý các kết nối mạng một cách hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `netstat` như sau:
```
netstat [tùy chọn] [tham số]
```

## Các tùy chọn phổ biến
- `-a`: Hiển thị tất cả các kết nối và cổng đang lắng nghe.
- `-t`: Hiển thị các kết nối TCP.
- `-u`: Hiển thị các kết nối UDP.
- `-n`: Hiển thị địa chỉ IP và số cổng thay vì tên miền và tên dịch vụ.
- `-l`: Hiển thị các cổng đang lắng nghe.
- `-p`: Hiển thị PID và tên của chương trình đang sử dụng kết nối.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `netstat`:

1. Hiển thị tất cả các kết nối và cổng đang lắng nghe:
   ```bash
   netstat -a
   ```

2. Hiển thị các kết nối TCP:
   ```bash
   netstat -t
   ```

3. Hiển thị các kết nối UDP:
   ```bash
   netstat -u
   ```

4. Hiển thị thông tin kết nối với địa chỉ IP và số cổng:
   ```bash
   netstat -n
   ```

5. Hiển thị các cổng đang lắng nghe:
   ```bash
   netstat -l
   ```

6. Hiển thị thông tin kết nối cùng với PID và tên chương trình:
   ```bash
   netstat -p
   ```

## Mẹo
- Sử dụng tùy chọn `-tuln` để nhanh chóng xem các kết nối TCP và UDP đang lắng nghe mà không cần tên miền.
- Kết hợp `netstat` với `grep` để lọc ra thông tin cụ thể. Ví dụ:
  ```bash
  netstat -tuln | grep 80
  ```
- Để có cái nhìn tổng quan hơn về tình trạng mạng, bạn có thể sử dụng `netstat` cùng với các lệnh khác như `top` hoặc `htop` để theo dõi hiệu suất hệ thống.