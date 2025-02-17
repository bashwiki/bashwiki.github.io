# [Linux] Bash killall cách sử dụng: Kết thúc tất cả các tiến trình theo tên

## Tổng quan
Lệnh `killall` trong Bash được sử dụng để kết thúc tất cả các tiến trình đang chạy với tên cụ thể. Điều này rất hữu ích khi bạn muốn dừng nhiều phiên bản của một ứng dụng mà không cần phải tìm kiếm từng tiến trình một.

## Cách sử dụng
Cú pháp cơ bản của lệnh `killall` như sau:
```bash
killall [tùy chọn] [tên_tiến_trình]
```

## Tùy chọn phổ biến
- `-u, --user`: Chỉ định người dùng sở hữu tiến trình.
- `-s, --signal`: Gửi tín hiệu cụ thể đến tiến trình (mặc định là SIGTERM).
- `-I, --ignore-case`: Bỏ qua phân biệt chữ hoa chữ thường khi tìm kiếm tên tiến trình.
- `-q, --quiet`: Không hiển thị thông báo lỗi nếu không tìm thấy tiến trình.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `killall`:

1. Kết thúc tất cả các tiến trình có tên `firefox`:
   ```bash
   killall firefox
   ```

2. Kết thúc tất cả các tiến trình `python` với tín hiệu SIGKILL:
   ```bash
   killall -s SIGKILL python
   ```

3. Kết thúc tất cả các tiến trình `gedit` mà không phân biệt chữ hoa chữ thường:
   ```bash
   killall -I gedit
   ```

4. Kết thúc tất cả các tiến trình của người dùng `username`:
   ```bash
   killall -u username
   ```

## Mẹo
- Hãy cẩn thận khi sử dụng `killall`, vì nó sẽ kết thúc tất cả các tiến trình có tên giống nhau, có thể gây mất dữ liệu nếu tiến trình đó đang làm việc.
- Sử dụng tùy chọn `-q` để tránh thông báo lỗi không cần thiết khi không tìm thấy tiến trình.
- Kiểm tra các tiến trình đang chạy trước khi sử dụng `killall` bằng lệnh `ps` hoặc `pgrep` để đảm bảo bạn không vô tình kết thúc tiến trình quan trọng.