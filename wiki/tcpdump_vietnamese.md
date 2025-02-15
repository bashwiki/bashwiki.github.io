# [리눅스] Bash tcpdump 사용법

## Tổng quan
`tcpdump` là một công cụ dòng lệnh mạnh mẽ được sử dụng để phân tích và ghi lại lưu lượng mạng trên các giao diện mạng. Nó cho phép người dùng xem các gói dữ liệu đang được truyền qua mạng, giúp trong việc chẩn đoán sự cố mạng, kiểm tra bảo mật và phân tích hiệu suất. `tcpdump` hỗ trợ nhiều giao thức và có thể lọc các gói dựa trên nhiều tiêu chí khác nhau.

## Cách sử dụng
Cú pháp cơ bản của lệnh `tcpdump` như sau:

```bash
tcpdump [tùy chọn] [biểu thức lọc]
```

### Các tùy chọn phổ biến:
- `-i <giao_diện>`: Chỉ định giao diện mạng mà bạn muốn theo dõi (ví dụ: `eth0`, `wlan0`).
- `-c <số_lượng>`: Giới hạn số lượng gói được ghi lại.
- `-w <tệp>`: Ghi lại các gói vào một tệp để phân tích sau.
- `-r <tệp>`: Đọc các gói từ một tệp đã ghi.
- `-n`: Không phân giải địa chỉ IP thành tên miền, giúp tăng tốc độ.
- `-v`, `-vv`, `-vvv`: Tăng cường mức độ chi tiết của thông tin được hiển thị.

## Ví dụ
### Ví dụ 1: Theo dõi lưu lượng mạng trên giao diện `eth0`
```bash
tcpdump -i eth0
```
Lệnh này sẽ hiển thị tất cả các gói dữ liệu đang đi qua giao diện `eth0`.

### Ví dụ 2: Ghi lại 10 gói dữ liệu vào tệp `capture.pcap`
```bash
tcpdump -i eth0 -c 10 -w capture.pcap
```
Lệnh này sẽ ghi lại 10 gói dữ liệu đầu tiên từ giao diện `eth0` vào tệp `capture.pcap`.

## Mẹo
- Sử dụng tùy chọn `-n` để tránh việc phân giải tên miền, điều này có thể giúp tăng tốc độ ghi lại gói.
- Kết hợp `tcpdump` với các công cụ phân tích khác như Wireshark để có cái nhìn sâu hơn về lưu lượng mạng.
- Thực hiện kiểm tra với quyền root hoặc sử dụng `sudo` để đảm bảo bạn có quyền truy cập vào các giao diện mạng.
- Lưu ý rằng việc ghi lại lưu lượng mạng có thể tạo ra một lượng lớn dữ liệu, vì vậy hãy cân nhắc sử dụng các biểu thức lọc để chỉ ghi lại những gì bạn cần.