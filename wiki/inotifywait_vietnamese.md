# [리눅스] Bash inotifywait 사용법

## Tổng quan
`inotifywait` là một công cụ dòng lệnh trong Linux được sử dụng để theo dõi các thay đổi trong hệ thống tệp. Nó cho phép người dùng nhận thông báo khi có sự kiện xảy ra trên các tệp hoặc thư mục, chẳng hạn như tạo, xóa, hoặc thay đổi nội dung. Điều này rất hữu ích cho việc giám sát các thay đổi trong thời gian thực và tự động hóa các tác vụ dựa trên các sự kiện này.

## Cách sử dụng
Cú pháp cơ bản của `inotifywait` như sau:

```bash
inotifywait [tùy chọn] [tệp hoặc thư mục]
```

### Các tùy chọn phổ biến:
- `-m` hoặc `--monitor`: Giữ cho `inotifywait` chạy liên tục và theo dõi các sự kiện.
- `-r` hoặc `--recursive`: Theo dõi các thư mục và tất cả các thư mục con của chúng.
- `-e` hoặc `--event`: Chỉ định loại sự kiện cần theo dõi, ví dụ: `create`, `delete`, `modify`, v.v.
- `-q` hoặc `--quiet`: Giảm thiểu thông tin đầu ra, chỉ hiển thị các sự kiện.

## Ví dụ
### Ví dụ 1: Theo dõi một thư mục cụ thể
Để theo dõi một thư mục có tên `my_folder` và nhận thông báo khi có tệp mới được tạo:

```bash
inotifywait -m -e create my_folder
```

Khi có tệp mới được tạo trong `my_folder`, bạn sẽ thấy thông báo tương ứng trên màn hình.

### Ví dụ 2: Theo dõi nhiều sự kiện
Để theo dõi cả sự kiện tạo và xóa trong thư mục `my_folder`:

```bash
inotifywait -m -e create -e delete my_folder
```

Điều này sẽ cho phép bạn nhận thông báo khi có tệp được tạo hoặc xóa trong thư mục.

## Mẹo
- Sử dụng tùy chọn `-r` nếu bạn cần theo dõi các thư mục con, điều này rất hữu ích trong các dự án lớn với nhiều thư mục.
- Kết hợp `inotifywait` với các lệnh khác trong Bash để tự động hóa quy trình làm việc. Ví dụ, bạn có thể sử dụng nó để tự động biên dịch mã nguồn khi có thay đổi.
- Đảm bảo rằng bạn có quyền truy cập vào thư mục hoặc tệp mà bạn muốn theo dõi, nếu không, `inotifywait` sẽ không hoạt động đúng cách.

Hy vọng rằng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng `inotifywait` trong Bash!