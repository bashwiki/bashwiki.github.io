# [Linux] Bash su: Thay đổi người dùng trong phiên làm việc

## Overview
Lệnh `su` (switch user) trong Bash cho phép người dùng thay đổi tài khoản người dùng trong một phiên làm việc hiện tại. Điều này rất hữu ích khi bạn cần thực hiện các tác vụ yêu cầu quyền truy cập của người dùng khác, thường là người dùng root.

## Usage
Cú pháp cơ bản của lệnh `su` như sau:
```bash
su [options] [username]
```

## Common Options
- `-l` hoặc `--login`: Đăng nhập như một người dùng mới và khởi động một shell mới.
- `-c`: Chạy một lệnh cụ thể với quyền của người dùng khác.
- `-s`: Chỉ định shell để sử dụng cho người dùng mới.

## Common Examples
- Để chuyển sang người dùng root:
```bash
su
```

- Để chuyển sang người dùng cụ thể (ví dụ: user1):
```bash
su user1
```

- Để chạy một lệnh với quyền của người dùng root:
```bash
su -c 'apt update'
```

- Để đăng nhập vào một shell mới với người dùng cụ thể:
```bash
su -l user1
```

## Tips
- Hãy chắc chắn rằng bạn có quyền truy cập để sử dụng lệnh `su`, thường là bạn cần biết mật khẩu của người dùng mà bạn muốn chuyển sang.
- Sử dụng `sudo` thay vì `su` nếu bạn chỉ cần thực hiện một lệnh với quyền root mà không cần chuyển đổi hoàn toàn sang tài khoản root.
- Luôn cẩn thận khi làm việc với quyền root, vì bạn có thể thay đổi hoặc xóa các tệp quan trọng trong hệ thống.