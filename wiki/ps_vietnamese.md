# [리눅스] Bash ps 사용법

## Tổng quan
Lệnh `ps` (process status) trong Bash được sử dụng để hiển thị thông tin về các tiến trình đang chạy trên hệ thống. Lệnh này cung cấp cái nhìn tổng quan về các tiến trình, bao gồm ID tiến trình (PID), trạng thái, thời gian CPU sử dụng và nhiều thông tin khác. Đây là một công cụ hữu ích cho các kỹ sư và nhà phát triển để theo dõi và quản lý các tiến trình trong môi trường Unix/Linux.

## Cách sử dụng
Cú pháp cơ bản của lệnh `ps` như sau:

```bash
ps [options]
```

Một số tùy chọn phổ biến của lệnh `ps` bao gồm:

- `-e` hoặc `-A`: Hiển thị tất cả các tiến trình đang chạy trên hệ thống.
- `-f`: Hiển thị thông tin chi tiết về các tiến trình, bao gồm cả thông tin về cha mẹ (PPID).
- `-u [username]`: Hiển thị các tiến trình của một người dùng cụ thể.
- `-aux`: Hiển thị tất cả các tiến trình, bao gồm cả những tiến trình không thuộc về người dùng hiện tại, với thông tin chi tiết.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `ps`:

1. Hiển thị tất cả các tiến trình đang chạy trên hệ thống:

```bash
ps -e
```

2. Hiển thị thông tin chi tiết về các tiến trình của người dùng hiện tại:

```bash
ps aux
```

3. Hiển thị các tiến trình của một người dùng cụ thể, ví dụ như `john`:

```bash
ps -u john
```

## Mẹo
- Sử dụng lệnh `ps` kết hợp với các lệnh khác như `grep` để tìm kiếm các tiến trình cụ thể. Ví dụ:

```bash
ps aux | grep firefox
```

- Kết hợp `ps` với `watch` để theo dõi sự thay đổi của các tiến trình theo thời gian:

```bash
watch -n 2 'ps aux'
```

- Để có cái nhìn tổng quan hơn về các tiến trình và tài nguyên hệ thống, bạn có thể sử dụng lệnh `top` hoặc `htop` thay vì `ps`, nhưng `ps` vẫn là một công cụ cơ bản và hữu ích để kiểm tra trạng thái tiến trình.