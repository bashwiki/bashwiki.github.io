# [리눅스] Bash passwd 사용법

## Tổng quan
Lệnh `passwd` trong Bash được sử dụng để thay đổi mật khẩu của người dùng trong hệ thống Linux. Lệnh này cho phép người dùng cập nhật mật khẩu của chính mình hoặc của người dùng khác (nếu có quyền thích hợp). Mục đích chính của lệnh này là để bảo mật tài khoản người dùng bằng cách đảm bảo rằng mật khẩu được cập nhật thường xuyên và mạnh mẽ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `passwd` như sau:

```bash
passwd [tùy chọn] [tên người dùng]
```

### Tùy chọn phổ biến:
- `tên người dùng`: Chỉ định tên người dùng mà bạn muốn thay đổi mật khẩu. Nếu không chỉ định tên người dùng, lệnh sẽ thay đổi mật khẩu của người dùng hiện tại.
- `-d`: Xóa mật khẩu của người dùng, cho phép đăng nhập mà không cần mật khẩu.
- `-e`: Đặt mật khẩu của người dùng hết hạn ngay lập tức, yêu cầu người dùng phải thay đổi mật khẩu khi đăng nhập lần tiếp theo.
- `-l`: Khóa tài khoản người dùng, ngăn không cho đăng nhập.
- `-u`: Mở khóa tài khoản người dùng đã bị khóa.

## Ví dụ
### Ví dụ 1: Thay đổi mật khẩu của người dùng hiện tại
Để thay đổi mật khẩu của người dùng hiện tại, bạn chỉ cần gõ lệnh sau:

```bash
passwd
```

Hệ thống sẽ yêu cầu bạn nhập mật khẩu hiện tại và sau đó là mật khẩu mới.

### Ví dụ 2: Thay đổi mật khẩu cho một người dùng khác
Nếu bạn có quyền quản trị (root), bạn có thể thay đổi mật khẩu cho một người dùng khác bằng cách chỉ định tên người dùng:

```bash
sudo passwd ten_nguoi_dung
```

Hệ thống sẽ yêu cầu bạn nhập mật khẩu mới cho người dùng đó.

## Mẹo
- **Sử dụng mật khẩu mạnh**: Đảm bảo rằng mật khẩu mới của bạn đủ mạnh, bao gồm chữ hoa, chữ thường, số và ký tự đặc biệt.
- **Thường xuyên thay đổi mật khẩu**: Để bảo mật tốt hơn, hãy thay đổi mật khẩu của bạn định kỳ.
- **Ghi nhớ mật khẩu**: Sử dụng trình quản lý mật khẩu nếu bạn gặp khó khăn trong việc ghi nhớ nhiều mật khẩu khác nhau.

Lệnh `passwd` là một công cụ quan trọng trong việc quản lý bảo mật tài khoản người dùng trên hệ thống Linux. Hãy sử dụng nó một cách cẩn thận và có trách nhiệm!