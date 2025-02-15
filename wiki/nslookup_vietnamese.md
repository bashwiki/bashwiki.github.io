# [리눅스] Bash nslookup 사용법

## Tổng quan
`nslookup` là một công cụ dòng lệnh được sử dụng để truy vấn các máy chủ DNS (Domain Name System) nhằm lấy thông tin về tên miền và địa chỉ IP. Lệnh này rất hữu ích cho các kỹ sư và nhà phát triển trong việc kiểm tra cấu hình DNS, xác định địa chỉ IP của tên miền hoặc ngược lại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `nslookup` như sau:

```
nslookup [tùy chọn] [tên miền | địa chỉ IP]
```

### Các tùy chọn phổ biến:
- `-type=TYPE`: Chỉ định loại bản ghi DNS mà bạn muốn truy vấn (ví dụ: A, AAAA, MX, CNAME).
- `-debug`: Hiển thị thông tin chi tiết về quá trình truy vấn.
- `-timeout=SECONDS`: Thiết lập thời gian chờ cho mỗi truy vấn.
- `-port=PORT`: Chỉ định cổng mà máy chủ DNS sẽ sử dụng.

## Ví dụ
### Ví dụ 1: Truy vấn địa chỉ IP của một tên miền
```bash
nslookup www.example.com
```
Kết quả sẽ hiển thị địa chỉ IP tương ứng với tên miền `www.example.com`.

### Ví dụ 2: Truy vấn bản ghi MX của một tên miền
```bash
nslookup -type=MX example.com
```
Kết quả sẽ hiển thị các bản ghi MX (Mail Exchange) cho tên miền `example.com`, cho phép bạn biết máy chủ nào xử lý email cho tên miền đó.

## Mẹo
- Sử dụng tùy chọn `-debug` để theo dõi quá trình truy vấn và tìm hiểu thêm về cách mà `nslookup` hoạt động.
- Kiểm tra nhiều máy chủ DNS khác nhau bằng cách chỉ định máy chủ DNS trong lệnh, ví dụ: `nslookup www.example.com 8.8.8.8` (sử dụng máy chủ DNS của Google).
- Hãy chắc chắn rằng bạn có quyền truy cập vào mạng để thực hiện các truy vấn DNS, vì một số mạng có thể hạn chế truy cập đến các máy chủ DNS bên ngoài.