# [리눅스] Bash mpstat 사용법

## Tổng quan
`mpstat` là một lệnh trong hệ thống Unix/Linux được sử dụng để hiển thị thông tin về hiệu suất CPU. Lệnh này cho phép người dùng theo dõi hoạt động của từng CPU hoặc tất cả các CPU trong hệ thống, giúp phát hiện các vấn đề về hiệu suất và tối ưu hóa tài nguyên.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mpstat` như sau:

```
mpstat [tùy chọn] [thời gian] [số lần]
```

### Các tùy chọn phổ biến:
- `-P ALL`: Hiển thị thông tin cho tất cả các CPU.
- `-u`: Hiển thị thông tin sử dụng CPU.
- `-h`: Hiển thị thông tin theo định dạng dễ đọc hơn.
- `-V`: Hiển thị phiên bản của `mpstat`.

## Ví dụ
### Ví dụ 1: Hiển thị thông tin sử dụng CPU cho tất cả các CPU
Để xem thông tin sử dụng CPU cho tất cả các CPU trong hệ thống, bạn có thể sử dụng lệnh sau:

```bash
mpstat -P ALL 1 5
```
Lệnh này sẽ hiển thị thông tin sử dụng CPU mỗi giây trong 5 lần.

### Ví dụ 2: Hiển thị thông tin sử dụng CPU với định dạng dễ đọc
Nếu bạn muốn hiển thị thông tin theo định dạng dễ đọc hơn, bạn có thể sử dụng tùy chọn `-h`:

```bash
mpstat -u -h 2 3
```
Lệnh này sẽ hiển thị thông tin sử dụng CPU mỗi 2 giây trong 3 lần.

## Mẹo
- Sử dụng `mpstat` cùng với các công cụ giám sát khác như `top` hoặc `htop` để có cái nhìn tổng quan hơn về hiệu suất hệ thống.
- Thường xuyên theo dõi thông tin CPU trong các môi trường sản xuất để phát hiện sớm các vấn đề tiềm ẩn.
- Lưu ý rằng việc sử dụng lệnh `mpstat` liên tục có thể tạo ra một lượng lớn dữ liệu, vì vậy hãy cân nhắc số lần và khoảng thời gian giữa các lần gọi lệnh.