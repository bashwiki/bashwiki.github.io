# [리눅스] Bash iostat 사용법

## Tổng quan
Lệnh `iostat` là một công cụ trong hệ điều hành Unix/Linux được sử dụng để theo dõi và báo cáo hoạt động của các thiết bị lưu trữ và CPU. Nó giúp người dùng phân tích hiệu suất hệ thống bằng cách cung cấp thông tin về thời gian sử dụng CPU và mức độ hoạt động của các thiết bị lưu trữ, từ đó hỗ trợ việc tối ưu hóa và khắc phục sự cố.

## Cú pháp
Cú pháp cơ bản của lệnh `iostat` như sau:

```bash
iostat [tùy chọn] [thời gian] [số lần]
```

### Các tùy chọn phổ biến:
- `-c`: Hiển thị thông tin về CPU.
- `-d`: Hiển thị thông tin về thiết bị lưu trữ.
- `-x`: Hiển thị thông tin mở rộng về thiết bị lưu trữ.
- `-h`: Hiển thị kết quả theo định dạng dễ đọc (kilo, mega).
- `-p [tên thiết bị]`: Hiển thị thông tin cho một thiết bị cụ thể.

## Ví dụ
### Ví dụ 1: Hiển thị thông tin CPU và thiết bị lưu trữ
Để xem thông tin về CPU và thiết bị lưu trữ, bạn có thể sử dụng lệnh sau:

```bash
iostat -c -d 2 5
```
Lệnh này sẽ báo cáo thông tin về CPU và thiết bị lưu trữ mỗi 2 giây, tổng cộng 5 lần.

### Ví dụ 2: Hiển thị thông tin mở rộng về thiết bị lưu trữ
Để xem thông tin mở rộng cho tất cả các thiết bị lưu trữ, bạn có thể chạy:

```bash
iostat -x 1 3
```
Lệnh này sẽ cung cấp thông tin mở rộng về các thiết bị lưu trữ mỗi giây, tổng cộng 3 lần.

## Mẹo
- Sử dụng tùy chọn `-h` để có được kết quả dễ đọc hơn, đặc biệt khi làm việc với các số liệu lớn.
- Kết hợp `iostat` với các công cụ khác như `vmstat` hoặc `mpstat` để có cái nhìn tổng thể hơn về hiệu suất hệ thống.
- Theo dõi thường xuyên hiệu suất hệ thống của bạn để phát hiện sớm các vấn đề tiềm ẩn và tối ưu hóa tài nguyên.