# [Linux] Bash lspci Cách sử dụng: Liệt kê thiết bị PCI

## Tổng quan
Lệnh `lspci` được sử dụng để liệt kê tất cả các thiết bị PCI (Peripheral Component Interconnect) được kết nối với hệ thống của bạn. Nó cung cấp thông tin chi tiết về các thiết bị phần cứng như card đồ họa, card âm thanh và các bộ điều khiển mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `lspci` như sau:
```
lspci [options] [arguments]
```

## Tùy chọn phổ biến
- `-v`: Hiển thị thông tin chi tiết hơn về các thiết bị.
- `-vv`: Hiển thị thông tin rất chi tiết.
- `-k`: Hiển thị thông tin về driver đang sử dụng cho các thiết bị.
- `-nn`: Hiển thị ID của nhà sản xuất và ID thiết bị.
- `-s <slot>`: Chỉ định một thiết bị cụ thể để hiển thị thông tin.

## Ví dụ phổ biến
- Liệt kê tất cả các thiết bị PCI:
  ```bash
  lspci
  ```

- Hiển thị thông tin chi tiết về tất cả các thiết bị:
  ```bash
  lspci -v
  ```

- Hiển thị thông tin về driver cho các thiết bị:
  ```bash
  lspci -k
  ```

- Liệt kê thiết bị với ID nhà sản xuất và ID thiết bị:
  ```bash
  lspci -nn
  ```

- Hiển thị thông tin cho một thiết bị cụ thể (ví dụ: slot 00:1f.2):
  ```bash
  lspci -s 00:1f.2 -v
  ```

## Mẹo
- Sử dụng tùy chọn `-v` hoặc `-vv` để có thêm thông tin chi tiết khi cần thiết.
- Kết hợp `lspci` với `grep` để tìm kiếm thiết bị cụ thể:
  ```bash
  lspci | grep -i network
  ```
- Để xuất thông tin ra file, bạn có thể sử dụng chuyển hướng đầu ra:
  ```bash
  lspci > devices.txt
  ```