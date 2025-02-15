# [리눅스] Bash su 사용법

## Tổng quan
Lệnh `su` (viết tắt của "substitute user") trong Bash được sử dụng để chuyển đổi giữa các tài khoản người dùng trong hệ thống Linux. Lệnh này cho phép người dùng đăng nhập vào tài khoản khác mà không cần phải đăng xuất và đăng nhập lại. Thông thường, lệnh `su` được sử dụng để chuyển sang tài khoản người dùng root, cho phép thực hiện các tác vụ quản trị hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `su` như sau:

```bash
su [tùy chọn] [người_dùng]
```

### Các tùy chọn phổ biến:
- `-`: Chuyển sang môi trường shell của người dùng mục tiêu, bao gồm cả biến môi trường.
- `-c`: Chạy lệnh cụ thể với quyền của người dùng mục tiêu.
- `-l` hoặc `--login`: Tương tự như `-`, khởi động một shell đăng nhập cho người dùng mục tiêu.

## Ví dụ
### Ví dụ 1: Chuyển sang tài khoản root
Để chuyển sang tài khoản root, bạn có thể sử dụng lệnh sau:

```bash
su -
```
Sau khi nhập lệnh này, bạn sẽ được yêu cầu nhập mật khẩu của tài khoản root.

### Ví dụ 2: Chạy một lệnh với quyền của người dùng khác
Nếu bạn muốn chạy một lệnh cụ thể với quyền của người dùng khác, bạn có thể sử dụng tùy chọn `-c` như sau:

```bash
su -c "ls /root" username
```
Trong ví dụ này, lệnh `ls /root` sẽ được thực hiện với quyền của `username`.

## Mẹo
- Hãy cẩn thận khi sử dụng lệnh `su`, đặc biệt là khi chuyển sang tài khoản root, vì bạn có thể thực hiện các thay đổi quan trọng trong hệ thống.
- Sử dụng lệnh `sudo` thay vì `su` nếu bạn chỉ cần thực hiện một lệnh cụ thể với quyền quản trị, vì `sudo` cho phép bạn thực hiện lệnh mà không cần chuyển đổi hoàn toàn sang tài khoản root.
- Đảm bảo rằng bạn đã biết rõ mật khẩu của tài khoản mà bạn muốn chuyển sang trước khi sử dụng lệnh `su`.