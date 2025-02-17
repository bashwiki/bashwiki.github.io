# [Linux] Bash realpath cách sử dụng: Lấy đường dẫn tuyệt đối của tệp tin

## Tổng quan
Lệnh `realpath` trong Bash được sử dụng để chuyển đổi đường dẫn tương đối của tệp tin hoặc thư mục thành đường dẫn tuyệt đối. Điều này rất hữu ích khi bạn cần biết chính xác vị trí của một tệp tin trong hệ thống tệp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `realpath` như sau:

```bash
realpath [options] [arguments]
```

## Các tùy chọn phổ biến
- `-m`, `--canonicalize-missing`: Chuyển đổi đường dẫn mà không cần kiểm tra sự tồn tại của tệp tin.
- `-q`, `--quiet`: Không hiển thị thông báo lỗi nếu đường dẫn không tồn tại.
- `-s`, `--strip`: Loại bỏ các phần tử không cần thiết trong đường dẫn.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `realpath`:

1. **Lấy đường dẫn tuyệt đối của một tệp tin:**
   ```bash
   realpath myfile.txt
   ```

2. **Chuyển đổi đường dẫn tương đối thành đường dẫn tuyệt đối:**
   ```bash
   realpath ./documents/report.pdf
   ```

3. **Sử dụng tùy chọn `-m` để lấy đường dẫn của tệp tin không tồn tại:**
   ```bash
   realpath -m /nonexistent/path/to/file.txt
   ```

4. **Lấy đường dẫn tuyệt đối của một thư mục:**
   ```bash
   realpath /home/user/projects/
   ```

## Mẹo
- Sử dụng `realpath` trong các script để đảm bảo rằng bạn luôn làm việc với đường dẫn tuyệt đối, giúp tránh nhầm lẫn.
- Kết hợp `realpath` với các lệnh khác như `cd` để dễ dàng điều hướng trong hệ thống tệp.
- Kiểm tra đường dẫn của các tệp tin trước khi thực hiện các thao tác khác để đảm bảo rằng bạn đang làm việc với đúng tệp tin.