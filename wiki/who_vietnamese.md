# [Linux] Bash who cách sử dụng: Xem danh sách người dùng đang đăng nhập

## Tổng quan
Lệnh `who` trong Bash được sử dụng để hiển thị danh sách người dùng đang đăng nhập vào hệ thống. Nó cung cấp thông tin về tên người dùng, thời gian đăng nhập và địa chỉ IP hoặc tên máy của người dùng.

## Cú pháp
Cú pháp cơ bản của lệnh `who` như sau:
```
who [options] [arguments]
```

## Tùy chọn phổ biến
- `-a`: Hiển thị tất cả thông tin liên quan đến người dùng đang đăng nhập.
- `-b`: Hiển thị thời gian khởi động của hệ thống.
- `-q`: Chỉ hiển thị danh sách tên người dùng và số lượng người dùng đang đăng nhập.
- `--help`: Hiển thị thông tin trợ giúp về lệnh `who`.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `who`:

1. Hiển thị danh sách người dùng đang đăng nhập:
   ```bash
   who
   ```

2. Hiển thị thông tin chi tiết về người dùng và thời gian khởi động hệ thống:
   ```bash
   who -a
   ```

3. Hiển thị thời gian khởi động của hệ thống:
   ```bash
   who -b
   ```

4. Chỉ hiển thị danh sách tên người dùng và số lượng người dùng đang đăng nhập:
   ```bash
   who -q
   ```

## Mẹo
- Sử dụng lệnh `who` thường xuyên để theo dõi ai đang sử dụng hệ thống của bạn.
- Kết hợp lệnh `who` với các lệnh khác như `grep` để tìm kiếm thông tin cụ thể về người dùng.
- Nếu bạn cần thông tin chi tiết hơn, hãy xem xét sử dụng lệnh `w`, lệnh này cung cấp thêm thông tin về hoạt động của người dùng.