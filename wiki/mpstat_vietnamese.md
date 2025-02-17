# [Linux] Bash mpstat Cách sử dụng: Theo dõi hiệu suất CPU

## Tổng quan
Lệnh `mpstat` được sử dụng để hiển thị thông tin về hiệu suất CPU trên hệ thống. Nó cho phép người dùng theo dõi mức sử dụng CPU theo thời gian, giúp phân tích và tối ưu hóa hiệu suất hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mpstat` như sau:
```
mpstat [options] [arguments]
```

## Các tùy chọn phổ biến
- `-P ALL`: Hiển thị thông tin cho tất cả các CPU.
- `-u`: Hiển thị thông tin sử dụng CPU.
- `-r`: Hiển thị thông tin về bộ nhớ.
- `-h`: Hiển thị thông tin theo định dạng dễ đọc hơn.
- `interval`: Thời gian (tính bằng giây) giữa các lần cập nhật thông tin.

## Ví dụ thường gặp
1. Hiển thị thông tin sử dụng CPU cho tất cả các CPU:
   ```bash
   mpstat -P ALL
   ```

2. Theo dõi sử dụng CPU mỗi 5 giây:
   ```bash
   mpstat 5
   ```

3. Hiển thị thông tin sử dụng CPU với định dạng dễ đọc:
   ```bash
   mpstat -u -h
   ```

4. Hiển thị thông tin về bộ nhớ:
   ```bash
   mpstat -r
   ```

## Mẹo
- Sử dụng `mpstat` cùng với các công cụ khác như `grep` để lọc thông tin cần thiết.
- Theo dõi hiệu suất CPU trong thời gian dài để phát hiện các vấn đề tiềm ẩn.
- Kết hợp với các tùy chọn khác để có cái nhìn toàn diện hơn về hiệu suất hệ thống.