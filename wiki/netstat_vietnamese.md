# [리눅스] Bash netstat 사용법

## Tổng quan
Lệnh `netstat` (network statistics) là một công cụ dòng lệnh trong hệ điều hành Unix/Linux dùng để hiển thị thông tin về các kết nối mạng, bảng định tuyến, thống kê giao thức và các thông tin khác liên quan đến mạng. Lệnh này rất hữu ích cho các kỹ sư và lập trình viên để theo dõi trạng thái mạng và chẩn đoán sự cố kết nối.

## Cách sử dụng
Cú pháp cơ bản của lệnh `netstat` như sau:

```bash
netstat [tùy chọn]
```

Một số tùy chọn phổ biến của lệnh `netstat` bao gồm:

- `-a`: Hiển thị tất cả các kết nối và cổng đang lắng nghe.
- `-t`: Hiển thị các kết nối TCP.
- `-u`: Hiển thị các kết nối UDP.
- `-n`: Hiển thị địa chỉ và số cổng dưới dạng số, không chuyển đổi thành tên.
- `-l`: Hiển thị các cổng đang lắng nghe.
- `-p`: Hiển thị PID và tên của chương trình sử dụng kết nối.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `netstat`:

1. Hiển thị tất cả các kết nối và cổng đang lắng nghe:

```bash
netstat -a
```

2. Hiển thị các kết nối TCP đang hoạt động:

```bash
netstat -t
```

3. Hiển thị các cổng đang lắng nghe cùng với PID của chương trình:

```bash
netstat -l -p
```

## Mẹo
- Sử dụng tùy chọn `-n` để tăng tốc độ hiển thị thông tin, vì lệnh sẽ không cố gắng chuyển đổi địa chỉ IP thành tên miền.
- Kết hợp `netstat` với lệnh `grep` để lọc thông tin cụ thể. Ví dụ, để tìm kiếm các kết nối đến một địa chỉ IP cụ thể:

```bash
netstat -an | grep 192.168.1.1
```
- Thường xuyên kiểm tra các kết nối mạng để phát hiện các hoạt động bất thường hoặc không mong muốn, giúp bảo mật hệ thống tốt hơn.