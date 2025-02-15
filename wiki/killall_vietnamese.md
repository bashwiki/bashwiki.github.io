# [리눅스] Bash killall 사용법

## Tổng quan
Lệnh `killall` trong Bash được sử dụng để gửi tín hiệu đến tất cả các tiến trình đang chạy có tên giống như tên mà người dùng chỉ định. Mục đích chính của lệnh này là để dừng hoặc quản lý các tiến trình một cách dễ dàng mà không cần phải biết ID tiến trình (PID) của chúng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `killall` như sau:

```bash
killall [tùy chọn] <tên_tiến_trình>
```

### Các tùy chọn phổ biến:
- `-s`, `--signal <tín hiệu>`: Chỉ định tín hiệu mà bạn muốn gửi đến tiến trình. Ví dụ: `-s SIGKILL` để buộc dừng tiến trình.
- `-u <tên_người_dùng>`: Chỉ dừng các tiến trình của một người dùng cụ thể.
- `-q`, `--quiet`: Không hiển thị thông báo lỗi cho các tiến trình không tồn tại.
- `-v`, `--verbose`: Hiển thị thông tin chi tiết về các tiến trình đã bị dừng.

## Ví dụ
### Ví dụ 1: Dừng tất cả các tiến trình của một ứng dụng
Giả sử bạn muốn dừng tất cả các tiến trình của ứng dụng `firefox`, bạn có thể sử dụng lệnh sau:

```bash
killall firefox
```

### Ví dụ 2: Gửi tín hiệu SIGKILL đến tất cả các tiến trình của một ứng dụng
Nếu bạn muốn buộc dừng tất cả các tiến trình của `chrome`, bạn có thể sử dụng tín hiệu SIGKILL như sau:

```bash
killall -s SIGKILL chrome
```

## Mẹo
- Hãy cẩn thận khi sử dụng `killall`, vì nó sẽ dừng tất cả các tiến trình có tên giống nhau. Đảm bảo rằng bạn không dừng nhầm các tiến trình quan trọng.
- Sử dụng tùy chọn `-q` để tránh hiển thị thông báo lỗi nếu bạn không chắc chắn về tên tiến trình.
- Kiểm tra các tiến trình đang chạy bằng lệnh `ps` trước khi sử dụng `killall` để đảm bảo rằng bạn đang dừng đúng tiến trình.