# [리눅스] Bash who 사용법

## Tổng quan
Lệnh `who` trong Bash được sử dụng để hiển thị danh sách người dùng đang đăng nhập vào hệ thống. Nó cung cấp thông tin về tên người dùng, terminal mà họ đang sử dụng, thời gian đăng nhập và địa chỉ IP hoặc tên máy chủ (nếu có). Lệnh này rất hữu ích cho quản trị viên hệ thống và các nhà phát triển muốn theo dõi hoạt động của người dùng trên máy chủ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `who` như sau:

```bash
who [tùy chọn]
```

### Các tùy chọn phổ biến:
- `-a`: Hiển thị tất cả thông tin về người dùng, bao gồm cả thông tin về thời gian và trạng thái.
- `-b`: Hiển thị thời gian khởi động của hệ thống.
- `-q`: Chỉ hiển thị danh sách tên người dùng và số lượng người dùng đang đăng nhập.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `who`:

1. Hiển thị danh sách người dùng đang đăng nhập:
   ```bash
   who
   ```

2. Hiển thị thông tin chi tiết về người dùng và thời gian khởi động của hệ thống:
   ```bash
   who -a
   ```

## Mẹo
- Sử dụng lệnh `who` kết hợp với các lệnh khác như `grep` để tìm kiếm thông tin cụ thể về người dùng. Ví dụ:
  ```bash
  who | grep username
  ```
- Thường xuyên kiểm tra danh sách người dùng đang đăng nhập để phát hiện các hoạt động không bình thường trên hệ thống của bạn.
- Kết hợp lệnh `who` với `last` để theo dõi lịch sử đăng nhập của người dùng.