# [Linux] Bash dig Cách sử dụng: Truy vấn thông tin DNS

## Tổng quan
Lệnh `dig` (Domain Information Groper) là một công cụ dòng lệnh dùng để truy vấn thông tin DNS (Domain Name System). Nó cho phép người dùng kiểm tra và phân tích các bản ghi DNS, giúp xác định địa chỉ IP của tên miền hoặc ngược lại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dig` như sau:

```bash
dig [options] [arguments]
```

## Các tùy chọn phổ biến
- `@server`: Chỉ định máy chủ DNS để truy vấn.
- `-t type`: Chỉ định loại bản ghi DNS cần truy vấn (ví dụ: A, AAAA, MX, TXT).
- `+short`: Hiển thị kết quả ngắn gọn, chỉ cho ra thông tin cần thiết.
- `+trace`: Theo dõi quá trình truy vấn từ máy chủ gốc đến máy chủ DNS.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `dig`:

1. **Truy vấn địa chỉ IP của một tên miền:**
   ```bash
   dig example.com
   ```

2. **Truy vấn bản ghi MX (Mail Exchange) của một tên miền:**
   ```bash
   dig -t MX example.com
   ```

3. **Sử dụng máy chủ DNS cụ thể để truy vấn:**
   ```bash
   dig @8.8.8.8 example.com
   ```

4. **Hiển thị kết quả ngắn gọn:**
   ```bash
   dig +short example.com
   ```

5. **Theo dõi quá trình truy vấn:**
   ```bash
   dig +trace example.com
   ```

## Mẹo
- Sử dụng tùy chọn `+short` để nhận kết quả nhanh chóng và dễ hiểu.
- Thử nghiệm với các loại bản ghi khác nhau để hiểu rõ hơn về cấu trúc DNS.
- Kiểm tra nhiều máy chủ DNS khác nhau để so sánh kết quả và xác minh tính chính xác.