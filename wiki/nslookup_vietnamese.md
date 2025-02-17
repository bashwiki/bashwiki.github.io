# [Linux] Bash nslookup Cách sử dụng: Tra cứu thông tin DNS

## Overview
Lệnh `nslookup` được sử dụng để truy vấn thông tin về tên miền và địa chỉ IP từ hệ thống DNS. Nó giúp người dùng xác định địa chỉ IP tương ứng với tên miền hoặc ngược lại.

## Usage
Cú pháp cơ bản của lệnh `nslookup` như sau:
```
nslookup [options] [arguments]
```

## Common Options
- `-type=TYPE`: Chỉ định loại bản ghi DNS cần truy vấn (ví dụ: A, AAAA, MX, CNAME).
- `-timeout=SECONDS`: Thay đổi thời gian chờ cho mỗi truy vấn.
- `-retry=COUNT`: Đặt số lần thử lại khi không nhận được phản hồi.

## Common Examples
- Tra cứu địa chỉ IP của một tên miền:
  ```bash
  nslookup example.com
  ```

- Tra cứu tên miền từ một địa chỉ IP:
  ```bash
  nslookup 93.184.216.34
  ```

- Tra cứu bản ghi MX của một tên miền:
  ```bash
  nslookup -type=MX example.com
  ```

- Thay đổi máy chủ DNS để thực hiện truy vấn:
  ```bash
  nslookup example.com 8.8.8.8
  ```

## Tips
- Sử dụng `nslookup` để kiểm tra xem một tên miền có tồn tại hay không trước khi thực hiện các thao tác khác.
- Kiểm tra các bản ghi DNS khác nhau để đảm bảo cấu hình DNS chính xác cho tên miền của bạn.
- Nếu bạn gặp vấn đề với DNS, hãy thử sử dụng một máy chủ DNS khác như Google DNS (8.8.8.8) để xem có sự khác biệt nào không.