# [Linux] Bash lsusb Cách sử dụng: Hiển thị thông tin về thiết bị USB

## Tổng quan
Lệnh `lsusb` được sử dụng để liệt kê các thiết bị USB được kết nối với hệ thống. Nó cung cấp thông tin chi tiết về các thiết bị, bao gồm ID nhà sản xuất, ID sản phẩm và các thông tin khác liên quan đến thiết bị USB.

## Cách sử dụng
Cú pháp cơ bản của lệnh `lsusb` như sau:
```
lsusb [options] [arguments]
```

## Các tùy chọn phổ biến
- `-v`: Hiển thị thông tin chi tiết về các thiết bị USB.
- `-t`: Hiển thị cấu trúc cây của các thiết bị USB.
- `-s [bus]:[device]`: Hiển thị thông tin cho một thiết bị USB cụ thể dựa trên bus và device ID.
- `-d [vendor]:[product]`: Hiển thị thông tin cho thiết bị USB có ID nhà sản xuất và ID sản phẩm cụ thể.

## Ví dụ phổ biến
- Để liệt kê tất cả các thiết bị USB:
  ```bash
  lsusb
  ```

- Để hiển thị thông tin chi tiết về tất cả các thiết bị USB:
  ```bash
  lsusb -v
  ```

- Để hiển thị cấu trúc cây của các thiết bị USB:
  ```bash
  lsusb -t
  ```

- Để xem thông tin cho một thiết bị USB cụ thể (ví dụ: bus 001, device 002):
  ```bash
  lsusb -s 001:002
  ```

- Để hiển thị thông tin cho một thiết bị USB cụ thể theo ID nhà sản xuất và ID sản phẩm (ví dụ: 1234:5678):
  ```bash
  lsusb -d 1234:5678
  ```

## Mẹo
- Sử dụng tùy chọn `-v` để có cái nhìn sâu hơn về các thông số kỹ thuật của thiết bị USB, điều này rất hữu ích khi bạn cần khắc phục sự cố.
- Kết hợp `lsusb` với các lệnh khác như `grep` để lọc thông tin cụ thể, ví dụ:
  ```bash
  lsusb | grep "Logitech"
  ```
- Nếu bạn thường xuyên làm việc với các thiết bị USB, hãy tạo một alias cho lệnh `lsusb` với các tùy chọn bạn sử dụng thường xuyên để tiết kiệm thời gian.