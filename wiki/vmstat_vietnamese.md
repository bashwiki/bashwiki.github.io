# [리눅스] Bash vmstat 사용법

## Tổng quan
Lệnh `vmstat` (Virtual Memory Statistics) là một công cụ hữu ích trong Bash để theo dõi và báo cáo về tình trạng bộ nhớ ảo, CPU, và các hoạt động I/O trên hệ thống. Lệnh này giúp các kỹ sư và nhà phát triển nắm bắt được hiệu suất của hệ thống, từ đó có thể tối ưu hóa và khắc phục sự cố khi cần thiết.

## Cách sử dụng
Cú pháp cơ bản của lệnh `vmstat` như sau:

```bash
vmstat [options] [delay] [count]
```

### Các tùy chọn phổ biến:
- `-a`: Hiển thị thông tin về bộ nhớ đang sử dụng và bộ nhớ có thể sử dụng.
- `-m`: Hiển thị thông tin về bộ nhớ vật lý và bộ nhớ ảo.
- `-s`: Hiển thị thống kê bộ nhớ chi tiết.
- `delay`: Thời gian (tính bằng giây) giữa các lần cập nhật thông tin.
- `count`: Số lần cập nhật thông tin sẽ được thực hiện.

## Ví dụ
### Ví dụ 1: Theo dõi tình trạng bộ nhớ và CPU
Để theo dõi tình trạng bộ nhớ và CPU mỗi 2 giây trong 5 lần, bạn có thể sử dụng lệnh sau:

```bash
vmstat 2 5
```

### Ví dụ 2: Hiển thị thông tin chi tiết về bộ nhớ
Để xem thông tin chi tiết về bộ nhớ, bạn có thể sử dụng tùy chọn `-s`:

```bash
vmstat -s
```

## Mẹo
- Sử dụng `vmstat` cùng với các công cụ khác như `grep` hoặc `awk` để lọc và phân tích dữ liệu dễ dàng hơn.
- Theo dõi thường xuyên tình trạng hệ thống bằng cách thiết lập một cron job để ghi lại thông tin từ `vmstat` vào một tệp log.
- Kết hợp `vmstat` với các lệnh khác như `iostat` và `mpstat` để có cái nhìn tổng quát hơn về hiệu suất hệ thống.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `vmstat` trong Bash!