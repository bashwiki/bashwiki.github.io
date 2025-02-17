# [Linux] Bash iostat Cách sử dụng: Theo dõi hiệu suất I/O

## Tổng quan
Lệnh `iostat` được sử dụng để theo dõi và báo cáo hiệu suất của hệ thống đầu vào/đầu ra (I/O) của máy tính. Nó cung cấp thông tin về hoạt động của các thiết bị lưu trữ và phân vùng, giúp người dùng hiểu rõ hơn về hiệu suất của hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `iostat` như sau:
```bash
iostat [options] [arguments]
```

## Tùy chọn phổ biến
- `-c`: Hiển thị thông tin về CPU.
- `-d`: Hiển thị thông tin về thiết bị I/O.
- `-x`: Hiển thị thông tin chi tiết về thiết bị I/O, bao gồm cả các chỉ số mở rộng.
- `-h`: Hiển thị kích thước đơn vị theo định dạng dễ đọc (ví dụ: KB, MB).
- `interval`: Thời gian giữa các lần báo cáo (tính bằng giây).
- `count`: Số lần báo cáo sẽ được thực hiện.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `iostat`:

1. Hiển thị thông tin cơ bản về CPU và I/O:
   ```bash
   iostat
   ```

2. Hiển thị thông tin về CPU và thiết bị I/O mỗi 5 giây:
   ```bash
   iostat -c -d 5
   ```

3. Hiển thị thông tin chi tiết về thiết bị I/O:
   ```bash
   iostat -x
   ```

4. Hiển thị thông tin I/O với kích thước dễ đọc:
   ```bash
   iostat -h
   ```

5. Theo dõi hiệu suất I/O mỗi 10 giây và thực hiện 3 lần:
   ```bash
   iostat 10 3
   ```

## Mẹo
- Sử dụng tùy chọn `-x` để có cái nhìn sâu hơn về hiệu suất của từng thiết bị, giúp bạn phát hiện các vấn đề tiềm ẩn.
- Kết hợp `iostat` với các lệnh khác như `grep` để lọc thông tin cần thiết.
- Theo dõi thường xuyên hiệu suất I/O để phát hiện sớm các vấn đề và tối ưu hóa hiệu suất hệ thống.