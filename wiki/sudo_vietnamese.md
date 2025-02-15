# [리눅스] Bash sudo 사용법

## Tổng quan
Lệnh `sudo` (viết tắt của "superuser do") cho phép người dùng thực thi các lệnh với quyền của người dùng khác, thường là quyền của người quản trị (root). Mục đích chính của `sudo` là cung cấp một phương pháp an toàn để thực hiện các tác vụ yêu cầu quyền truy cập cao hơn mà không cần phải đăng nhập vào tài khoản root.

## Cách sử dụng
Cú pháp cơ bản của lệnh `sudo` như sau:

```bash
sudo [tùy chọn] lệnh [tham số]
```

### Tùy chọn thông dụng:
- `-u <người_dùng>`: Chạy lệnh với quyền của người dùng chỉ định. Mặc định, `sudo` sẽ chạy lệnh với quyền của người dùng root.
- `-k`: Làm mới thời gian hết hạn của phiên làm việc `sudo`, yêu cầu nhập mật khẩu cho lần sử dụng tiếp theo.
- `-l`: Liệt kê các quyền mà người dùng hiện tại có thể sử dụng với `sudo`.

## Ví dụ
### Ví dụ 1: Cài đặt một gói phần mềm
Để cài đặt một gói phần mềm (ví dụ: `curl`), bạn có thể sử dụng lệnh sau:

```bash
sudo apt-get install curl
```

### Ví dụ 2: Chạy một lệnh với quyền của người dùng khác
Nếu bạn muốn chạy một lệnh với quyền của người dùng `john`, bạn có thể sử dụng:

```bash
sudo -u john whoami
```
Lệnh này sẽ trả về tên người dùng `john`.

## Mẹo
- **Sử dụng một cách cẩn thận**: Chỉ sử dụng `sudo` khi cần thiết, vì việc thực thi các lệnh với quyền cao có thể gây ra rủi ro cho hệ thống.
- **Kiểm tra quyền**: Sử dụng `sudo -l` để kiểm tra các quyền mà bạn có thể sử dụng, giúp bạn hiểu rõ hơn về khả năng của mình.
- **Thời gian hết hạn**: Mặc định, `sudo` sẽ yêu cầu bạn nhập mật khẩu mỗi 15 phút. Nếu bạn thực hiện nhiều lệnh liên tiếp, hãy cân nhắc sử dụng `sudo -k` để làm mới thời gian này khi cần thiết.