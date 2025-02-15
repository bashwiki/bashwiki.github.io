# [리눅스] Bash realpath 사용법

## Tổng quan
Lệnh `realpath` trong Bash được sử dụng để chuyển đổi đường dẫn tương đối hoặc đường dẫn không đầy đủ thành đường dẫn tuyệt đối. Mục đích chính của lệnh này là giúp người dùng xác định vị trí chính xác của tệp hoặc thư mục trong hệ thống tệp, điều này rất hữu ích trong các kịch bản tự động hóa và lập trình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `realpath` như sau:

```bash
realpath [tùy chọn] <đường_dẫn>
```

### Tùy chọn phổ biến
- `-m`, `--canonicalize-missing`: Chuyển đổi đường dẫn mà không cần kiểm tra sự tồn tại của tệp hoặc thư mục.
- `-q`, `--quiet`: Không in ra thông báo lỗi nếu đường dẫn không tồn tại.
- `-s`, `--strip`: Loại bỏ các phần tử `..` và `.` trong đường dẫn.

## Ví dụ
### Ví dụ 1: Chuyển đổi đường dẫn tương đối
Giả sử bạn có một thư mục con `docs` trong thư mục hiện tại và bạn muốn lấy đường dẫn tuyệt đối của nó:

```bash
realpath docs
```
Kết quả có thể là:
```
/home/user/project/docs
```

### Ví dụ 2: Sử dụng tùy chọn `-m`
Nếu bạn muốn chuyển đổi một đường dẫn mà không cần kiểm tra sự tồn tại của nó:

```bash
realpath -m ./nonexistent/path
```
Kết quả sẽ là đường dẫn tuyệt đối của đường dẫn đã cho, ngay cả khi nó không tồn tại.

## Mẹo
- Sử dụng `realpath` trong các script để đảm bảo rằng bạn luôn làm việc với đường dẫn tuyệt đối, giúp tránh các lỗi liên quan đến đường dẫn tương đối.
- Kết hợp `realpath` với các lệnh khác như `cd` hoặc `ln` để quản lý tệp và thư mục một cách hiệu quả hơn.
- Hãy cẩn thận khi sử dụng tùy chọn `-m`, vì nó có thể dẫn đến việc bạn làm việc với đường dẫn không tồn tại, điều này có thể gây ra lỗi trong các lệnh tiếp theo.