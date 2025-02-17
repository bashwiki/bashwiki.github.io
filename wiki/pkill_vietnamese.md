# [Linux] Bash pkill Cách sử dụng: Kết thúc tiến trình theo tên

## Tổng quan
Lệnh `pkill` trong Bash được sử dụng để kết thúc các tiến trình đang chạy dựa trên tên của chúng. Điều này rất hữu ích khi bạn muốn dừng một hoặc nhiều tiến trình mà không cần phải tìm kiếm ID tiến trình (PID).

## Cách sử dụng
Cú pháp cơ bản của lệnh `pkill` như sau:

```bash
pkill [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-f`: Tìm kiếm tên tiến trình trong toàn bộ dòng lệnh.
- `-n`: Kết thúc tiến trình mới nhất.
- `-o`: Kết thúc tiến trình cũ nhất.
- `-signal`: Gửi tín hiệu cụ thể đến tiến trình (mặc định là SIGTERM).

## Ví dụ phổ biến
- Kết thúc tất cả các tiến trình có tên "firefox":
  ```bash
  pkill firefox
  ```

- Kết thúc tất cả các tiến trình có tên "python":
  ```bash
  pkill python
  ```

- Kết thúc tiến trình mới nhất có tên "myapp":
  ```bash
  pkill -n myapp
  ```

- Kết thúc tiến trình cũ nhất có tên "myapp":
  ```bash
  pkill -o myapp
  ```

- Gửi tín hiệu SIGKILL đến tất cả các tiến trình có tên "myapp":
  ```bash
  pkill -9 myapp
  ```

## Mẹo
- Sử dụng tùy chọn `-f` nếu bạn cần tìm kiếm tiến trình dựa trên toàn bộ dòng lệnh, không chỉ tên.
- Hãy cẩn thận khi sử dụng `pkill`, vì nó có thể kết thúc nhiều tiến trình cùng lúc nếu chúng có cùng tên.
- Kiểm tra các tiến trình đang chạy trước khi sử dụng `pkill` bằng lệnh `ps` hoặc `top` để tránh việc dừng nhầm tiến trình quan trọng.