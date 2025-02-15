# [리눅스] Bash shutdown 사용법

## Tổng quan
Lệnh `shutdown` trong Bash được sử dụng để tắt hoặc khởi động lại hệ thống một cách an toàn. Lệnh này cho phép người dùng thông báo cho tất cả người dùng khác trên hệ thống rằng máy chủ sẽ tắt hoặc khởi động lại, đồng thời cung cấp thời gian để họ lưu lại công việc của mình. Đây là một công cụ quan trọng cho quản trị viên hệ thống để đảm bảo rằng quá trình tắt máy diễn ra một cách trơn tru và không gây mất dữ liệu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `shutdown` như sau:

```bash
shutdown [OPTION] [TIME] [MESSAGE]
```

### Các tùy chọn phổ biến:
- `-h`: Tắt máy.
- `-r`: Khởi động lại máy.
- `-c`: Hủy lệnh tắt máy đã lên lịch.
- `TIME`: Thời gian để tắt máy, có thể là một khoảng thời gian cụ thể (ví dụ: `+5` để tắt sau 5 phút) hoặc một thời điểm cụ thể (ví dụ: `12:00` để tắt lúc 12 giờ trưa).
- `MESSAGE`: Thông điệp sẽ được gửi đến tất cả người dùng đang đăng nhập.

## Ví dụ
### Ví dụ 1: Tắt máy ngay lập tức
Để tắt máy ngay lập tức, bạn có thể sử dụng lệnh sau:

```bash
shutdown -h now
```

### Ví dụ 2: Khởi động lại máy sau 10 phút
Nếu bạn muốn khởi động lại máy sau 10 phút, bạn có thể sử dụng lệnh sau:

```bash
shutdown -r +10 "Máy sẽ khởi động lại sau 10 phút. Vui lòng lưu công việc của bạn."
```

## Mẹo
- **Thông báo cho người dùng**: Luôn sử dụng tùy chọn `MESSAGE` để thông báo cho người dùng khác về thời gian tắt máy. Điều này giúp họ có thời gian để lưu lại công việc và tránh mất dữ liệu.
- **Kiểm tra lệnh**: Trước khi thực hiện lệnh `shutdown`, bạn có thể sử dụng tùy chọn `-c` để hủy lệnh tắt máy nếu cần thiết.
- **Quyền truy cập**: Đảm bảo rằng bạn có quyền truy cập thích hợp (thường là quyền root) để thực hiện lệnh `shutdown`.

Lệnh `shutdown` là một công cụ mạnh mẽ và cần thiết cho việc quản lý hệ thống, giúp đảm bảo rằng quá trình tắt máy hoặc khởi động lại diễn ra một cách an toàn và hiệu quả.