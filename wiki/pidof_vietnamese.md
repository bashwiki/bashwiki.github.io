# [리눅스] Bash pidof 사용법

## Tổng quan
Lệnh `pidof` trong Bash được sử dụng để tìm kiếm Process ID (PID) của một hoặc nhiều tiến trình đang chạy trên hệ thống. Mục đích chính của lệnh này là giúp người dùng xác định PID của các tiến trình dựa trên tên của chúng, điều này rất hữu ích trong việc quản lý và giám sát các tiến trình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `pidof` như sau:

```bash
pidof [tên_tiến_trình]
```

Trong đó:
- `tên_tiến_trình`: Là tên của tiến trình mà bạn muốn tìm PID. Bạn có thể chỉ định tên đầy đủ hoặc một phần của tên tiến trình.

### Tùy chọn phổ biến
- `-s`: Chỉ in ra PID đầu tiên của tiến trình.
- `-x`: Tìm PID của các tiến trình đang chạy từ các tập tin thực thi (không chỉ từ tên tiến trình).

## Ví dụ
### Ví dụ 1: Tìm PID của một tiến trình cụ thể
Giả sử bạn muốn tìm PID của tiến trình `bash`, bạn có thể sử dụng lệnh sau:

```bash
pidof bash
```

Kết quả sẽ là danh sách các PID của tất cả các tiến trình `bash` đang chạy.

### Ví dụ 2: Sử dụng tùy chọn -s
Nếu bạn chỉ muốn lấy PID đầu tiên của tiến trình `sshd`, bạn có thể sử dụng lệnh sau:

```bash
pidof -s sshd
```

Kết quả sẽ chỉ hiển thị PID đầu tiên của tiến trình `sshd`.

## Mẹo
- Khi sử dụng `pidof`, hãy chắc chắn rằng tên tiến trình bạn nhập chính xác để tránh nhận được kết quả không mong muốn.
- Kết hợp `pidof` với các lệnh khác như `kill` để dễ dàng quản lý tiến trình. Ví dụ, bạn có thể sử dụng:

```bash
kill $(pidof tiến_trình)
```

Điều này sẽ giúp bạn dừng một tiến trình cụ thể một cách nhanh chóng và hiệu quả.