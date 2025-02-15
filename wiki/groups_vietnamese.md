# [리눅스] Bash groups 사용법

## Tổng quan
Lệnh `groups` trong Bash được sử dụng để hiển thị các nhóm mà một người dùng thuộc về. Nó giúp người dùng và quản trị viên hệ thống xác định quyền truy cập và quyền hạn của người dùng trong hệ thống Unix/Linux. Mỗi người dùng có thể thuộc về một hoặc nhiều nhóm, và lệnh này cung cấp thông tin đó một cách nhanh chóng và dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `groups` như sau:

```
groups [tên_người_dùng]
```

- Nếu không có tham số nào được cung cấp, lệnh sẽ hiển thị các nhóm của người dùng hiện tại.
- Nếu bạn chỉ định một tên người dùng, lệnh sẽ hiển thị các nhóm mà người dùng đó thuộc về.

### Các tùy chọn phổ biến
- `-n`: Chỉ hiển thị tên nhóm mà không hiển thị ID nhóm.
- `--help`: Hiển thị thông tin trợ giúp về lệnh.

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng lệnh `groups`.

### Ví dụ 1: Hiển thị nhóm của người dùng hiện tại
```bash
groups
```
Khi bạn chạy lệnh này, nó sẽ hiển thị danh sách các nhóm mà người dùng hiện tại thuộc về.

### Ví dụ 2: Hiển thị nhóm của một người dùng cụ thể
```bash
groups username
```
Thay thế `username` bằng tên người dùng mà bạn muốn kiểm tra. Lệnh này sẽ hiển thị các nhóm mà người dùng đó thuộc về.

## Mẹo
- Sử dụng lệnh `groups` để kiểm tra quyền truy cập của người dùng trước khi thực hiện các thay đổi quan trọng trong hệ thống.
- Kết hợp lệnh `groups` với các lệnh khác như `id` để có được thông tin chi tiết hơn về người dùng và nhóm của họ.
- Đảm bảo rằng bạn có quyền truy cập để xem thông tin nhóm của người dùng khác, vì một số hệ thống có thể hạn chế quyền này.