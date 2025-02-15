# [리눅스] Bash tail 사용법

## Tổng quan
Lệnh `tail` trong Bash được sử dụng để hiển thị các dòng cuối cùng của một tệp tin. Nó rất hữu ích trong việc theo dõi các tệp log hoặc bất kỳ tệp nào mà bạn muốn xem nội dung mới nhất mà không cần mở toàn bộ tệp. Mặc định, `tail` sẽ hiển thị 10 dòng cuối cùng của tệp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `tail` như sau:

```bash
tail [tùy chọn] [tệp]
```

Một số tùy chọn phổ biến của lệnh `tail` bao gồm:

- `-n [số]`: Hiển thị số dòng cuối cùng được chỉ định. Ví dụ: `tail -n 20 file.txt` sẽ hiển thị 20 dòng cuối cùng của `file.txt`.
- `-f`: Theo dõi tệp trong thời gian thực. Lệnh này sẽ tiếp tục hiển thị các dòng mới được thêm vào tệp. Ví dụ: `tail -f file.log` sẽ theo dõi `file.log` và hiển thị các dòng mới khi chúng được ghi vào tệp.
- `-c [số]`: Hiển thị số byte cuối cùng được chỉ định. Ví dụ: `tail -c 100 file.txt` sẽ hiển thị 100 byte cuối cùng của `file.txt`.

## Ví dụ
### Ví dụ 1: Hiển thị 10 dòng cuối cùng của một tệp
```bash
tail file.txt
```

### Ví dụ 2: Theo dõi tệp log trong thời gian thực
```bash
tail -f /var/log/syslog
```

## Mẹo
- Khi sử dụng `tail -f`, bạn có thể nhấn `Ctrl + C` để dừng theo dõi tệp.
- Kết hợp `tail` với `grep` để lọc các dòng cụ thể. Ví dụ: `tail -f file.log | grep "ERROR"` sẽ chỉ hiển thị các dòng chứa từ "ERROR" trong `file.log`.
- Sử dụng `-n` để điều chỉnh số lượng dòng hiển thị theo nhu cầu của bạn, giúp bạn dễ dàng quản lý thông tin từ các tệp lớn.