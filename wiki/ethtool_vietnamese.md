# [리눅스] Bash ethtool 사용법

## Tổng quan
`ethtool` là một công cụ dòng lệnh trong Linux được sử dụng để quản lý và cấu hình các thiết bị mạng Ethernet. Nó cho phép người dùng xem và thay đổi các thông số của card mạng, bao gồm tốc độ kết nối, chế độ full-duplex, và nhiều thông tin khác liên quan đến hiệu suất và trạng thái của thiết bị mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ethtool` như sau:

```
ethtool [tùy chọn] [tên_giao_diện]
```

Trong đó:
- `tên_giao_diện` là tên của card mạng mà bạn muốn quản lý (ví dụ: `eth0`, `enp3s0`, v.v.).
- Các tùy chọn phổ biến bao gồm:
  - `-i`: Hiển thị thông tin về driver của card mạng.
  - `-s`: Cấu hình card mạng (ví dụ: thay đổi tốc độ, chế độ duplex).
  - `-p`: Nhấp nháy đèn LED trên card mạng để xác định vị trí.
  - `-a`: Hiển thị thông tin chi tiết về card mạng.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `ethtool`:

1. **Xem thông tin về card mạng**:
   ```bash
   ethtool eth0
   ```
   Lệnh này sẽ hiển thị thông tin chi tiết về card mạng `eth0`, bao gồm tốc độ kết nối, chế độ duplex, và trạng thái link.

2. **Thay đổi tốc độ và chế độ duplex**:
   ```bash
   ethtool -s eth0 speed 100 duplex full
   ```
   Lệnh này sẽ cấu hình card mạng `eth0` để hoạt động ở tốc độ 100 Mbps và chế độ full-duplex.

## Mẹo
- Khi sử dụng `ethtool`, hãy chắc chắn rằng bạn có quyền truy cập root hoặc sử dụng `sudo` để thực hiện các thay đổi cấu hình.
- Kiểm tra thường xuyên thông tin về card mạng có thể giúp bạn phát hiện sớm các vấn đề về kết nối.
- Sử dụng tùy chọn `-i` để kiểm tra phiên bản driver của card mạng, điều này có thể hữu ích khi bạn cần cập nhật hoặc khắc phục sự cố.