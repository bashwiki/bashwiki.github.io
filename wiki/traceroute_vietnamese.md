# [Linux] Bash traceroute cách sử dụng: Xác định đường đi của gói tin mạng

## Overview
Lệnh `traceroute` được sử dụng để xác định đường đi của các gói tin từ máy tính của bạn đến một máy chủ hoặc địa chỉ IP cụ thể. Nó giúp người dùng theo dõi các bước mà gói tin đi qua trên mạng, từ đó có thể phát hiện ra các vấn đề về kết nối.

## Usage
Cú pháp cơ bản của lệnh `traceroute` như sau:

```bash
traceroute [options] [arguments]
```

## Common Options
- `-m <hops>`: Xác định số lượng bước nhảy tối đa mà gói tin có thể đi qua.
- `-n`: Hiển thị địa chỉ IP thay vì tên miền.
- `-w <seconds>`: Thay đổi thời gian chờ cho mỗi gói tin.
- `-p <port>`: Chỉ định cổng mà gói tin sẽ được gửi đến.

## Common Examples
Dưới đây là một số ví dụ thực tế khi sử dụng lệnh `traceroute`:

1. **Traceroute đến một địa chỉ IP:**
   ```bash
   traceroute 8.8.8.8
   ```

2. **Traceroute đến một tên miền:**
   ```bash
   traceroute www.google.com
   ```

3. **Sử dụng tùy chọn -n để hiển thị địa chỉ IP:**
   ```bash
   traceroute -n www.google.com
   ```

4. **Thay đổi số lượng bước nhảy tối đa:**
   ```bash
   traceroute -m 15 www.google.com
   ```

5. **Thay đổi thời gian chờ cho mỗi gói tin:**
   ```bash
   traceroute -w 2 www.google.com
   ```

## Tips
- Sử dụng tùy chọn `-n` nếu bạn muốn tăng tốc độ thực hiện lệnh bằng cách bỏ qua việc phân giải tên miền.
- Nếu bạn gặp phải vấn đề về kết nối, hãy kiểm tra từng bước nhảy để xác định vị trí gặp sự cố.
- Thử nghiệm với các tùy chọn khác nhau để có được thông tin chi tiết hơn về mạng của bạn.