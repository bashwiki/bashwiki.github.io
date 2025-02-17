# [Linux] Bash watch cách sử dụng: Theo dõi lệnh trong thời gian thực

## Overview
Lệnh `watch` trong Bash cho phép bạn theo dõi và thực thi một lệnh cụ thể ở khoảng thời gian định trước. Điều này rất hữu ích khi bạn muốn giám sát sự thay đổi của đầu ra lệnh mà không cần phải nhập lại lệnh đó liên tục.

## Usage
Cú pháp cơ bản của lệnh `watch` như sau:

```bash
watch [options] [arguments]
```

## Common Options
- `-n <seconds>`: Đặt khoảng thời gian (tính bằng giây) giữa các lần thực thi lệnh.
- `-d`: Làm nổi bật sự khác biệt giữa các lần thực thi.
- `-t`: Tắt tiêu đề hiển thị, chỉ hiển thị đầu ra của lệnh.
- `-x`: Thực thi lệnh với các tham số được chỉ định.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `watch`:

1. Theo dõi sự thay đổi của thư mục hiện tại:
   ```bash
   watch -n 2 ls -l
   ```

2. Theo dõi trạng thái của một dịch vụ:
   ```bash
   watch systemctl status apache2
   ```

3. Theo dõi sự thay đổi của một tệp tin:
   ```bash
   watch -d cat /var/log/syslog
   ```

4. Theo dõi việc sử dụng bộ nhớ:
   ```bash
   watch -n 5 free -h
   ```

## Tips
- Sử dụng tùy chọn `-d` để dễ dàng nhận diện các thay đổi trong đầu ra.
- Điều chỉnh khoảng thời gian với `-n` để phù hợp với nhu cầu theo dõi của bạn.
- Nếu bạn chỉ muốn xem đầu ra mà không cần tiêu đề, hãy sử dụng tùy chọn `-t` để làm cho màn hình gọn gàng hơn.