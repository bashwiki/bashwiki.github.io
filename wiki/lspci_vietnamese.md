# [리눅스] Bash lspci 사용법

## Tổng quan
Lệnh `lspci` là một công cụ dòng lệnh trong Linux được sử dụng để liệt kê tất cả các thiết bị PCI (Peripheral Component Interconnect) được kết nối với hệ thống. Lệnh này rất hữu ích cho các kỹ sư và nhà phát triển khi cần kiểm tra thông tin phần cứng, giúp xác định các thiết bị như card đồ họa, card mạng, và các thiết bị khác được kết nối qua bus PCI.

## Cách sử dụng
Cú pháp cơ bản của lệnh `lspci` như sau:

```bash
lspci [tùy chọn]
```

Một số tùy chọn phổ biến của lệnh `lspci` bao gồm:

- `-v`: Hiển thị thông tin chi tiết về các thiết bị.
- `-vv`: Hiển thị thông tin chi tiết hơn nữa.
- `-k`: Hiển thị thông tin về trình điều khiển (driver) đang sử dụng cho các thiết bị.
- `-nn`: Hiển thị ID nhà sản xuất và ID thiết bị trong định dạng số.
- `-s <bus:device.function>`: Chỉ định một thiết bị cụ thể để hiển thị thông tin.

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng lệnh `lspci`:

1. Để liệt kê tất cả các thiết bị PCI trong hệ thống:

```bash
lspci
```

2. Để hiển thị thông tin chi tiết về tất cả các thiết bị PCI, bao gồm cả thông tin về trình điều khiển:

```bash
lspci -v -k
```

## Mẹo
- Khi bạn cần tìm hiểu sâu hơn về một thiết bị cụ thể, hãy sử dụng tùy chọn `-s` để chỉ định thiết bị đó. Điều này giúp giảm thiểu thông tin không cần thiết và tập trung vào thiết bị bạn quan tâm.
- Kết hợp `lspci` với các lệnh khác như `grep` để lọc kết quả. Ví dụ, để tìm card đồ họa, bạn có thể sử dụng:

```bash
lspci | grep VGA
```

- Nếu bạn muốn xuất thông tin ra file để phân tích sau, bạn có thể sử dụng dấu `>`:

```bash
lspci -vv > pci_devices.txt
```

Lệnh `lspci` là một công cụ mạnh mẽ giúp bạn quản lý và hiểu rõ hơn về phần cứng trong hệ thống Linux của mình.