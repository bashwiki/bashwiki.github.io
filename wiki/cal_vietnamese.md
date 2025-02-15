# [리눅스] Bash cal 사용법

## Tổng quan
Lệnh `cal` trong Bash được sử dụng để hiển thị lịch tháng hoặc năm. Đây là một công cụ hữu ích cho các kỹ sư và nhà phát triển khi cần tra cứu ngày tháng hoặc lên kế hoạch cho các sự kiện. Lệnh này có thể hiển thị lịch theo nhiều định dạng khác nhau, giúp người dùng dễ dàng theo dõi các ngày trong tháng hoặc năm.

## Cách sử dụng
Cú pháp cơ bản của lệnh `cal` như sau:

```bash
cal [tháng] [năm]
```

- Nếu không chỉ định tháng và năm, `cal` sẽ hiển thị lịch của tháng hiện tại.
- Bạn có thể chỉ định tháng bằng số (1-12) và năm bằng số (ví dụ: 2023).
  
### Các tùy chọn phổ biến
- `-y`: Hiển thị lịch của cả năm hiện tại.
- `-3`: Hiển thị lịch của tháng trước, tháng hiện tại và tháng tiếp theo.
- `-m`: Hiển thị lịch với thứ Hai là ngày đầu tuần (mặc định là Chủ Nhật).

## Ví dụ
1. Hiển thị lịch của tháng hiện tại:
   ```bash
   cal
   ```

2. Hiển thị lịch của tháng 5 năm 2023:
   ```bash
   cal 5 2023
   ```

3. Hiển thị lịch của cả năm 2023:
   ```bash
   cal -y 2023
   ```

## Mẹo
- Sử dụng tùy chọn `-3` để có cái nhìn tổng quan về ba tháng liên tiếp, giúp bạn dễ dàng lập kế hoạch cho các sự kiện.
- Kết hợp lệnh `cal` với lệnh `grep` để tìm kiếm các ngày cụ thể trong lịch.
- Bạn có thể sử dụng lệnh `cal` trong các script để tự động tạo lịch cho các dự án hoặc sự kiện.

Lệnh `cal` là một công cụ đơn giản nhưng mạnh mẽ để quản lý thời gian và lên kế hoạch, rất hữu ích cho các kỹ sư và nhà phát triển trong công việc hàng ngày.