# [리눅스] Bash usermod 사용법

## Tổng quan
Lệnh `usermod` trong Bash được sử dụng để thay đổi các thuộc tính của người dùng đã tồn tại trên hệ thống. Lệnh này cho phép quản trị viên hệ thống điều chỉnh quyền hạn, nhóm, và các thông tin khác liên quan đến tài khoản người dùng, giúp quản lý người dùng một cách hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `usermod` như sau:

```bash
usermod [tùy chọn] tên_người_dùng
```

### Các tùy chọn phổ biến:
- `-aG nhóm`: Thêm người dùng vào một nhóm mà không xóa các nhóm hiện tại.
- `-d thư_mục`: Thay đổi thư mục chính của người dùng.
- `-l tên_mới`: Đổi tên người dùng.
- `-s shell`: Thay đổi shell mặc định cho người dùng.
- `-u ID_mới`: Thay đổi ID người dùng.

## Ví dụ
### Ví dụ 1: Thêm người dùng vào nhóm
Để thêm người dùng `john` vào nhóm `developers`, bạn có thể sử dụng lệnh sau:

```bash
usermod -aG developers john
```

### Ví dụ 2: Đổi tên người dùng
Nếu bạn muốn đổi tên người dùng từ `john` thành `johnny`, bạn có thể sử dụng lệnh sau:

```bash
usermod -l johnny john
```

## Mẹo
- Trước khi thực hiện các thay đổi lớn với lệnh `usermod`, hãy sao lưu thông tin người dùng để tránh mất mát dữ liệu.
- Sử dụng tùy chọn `-d` để thay đổi thư mục chính của người dùng, nhưng hãy chắc chắn rằng thư mục mới đã tồn tại và có quyền truy cập thích hợp.
- Luôn kiểm tra các nhóm mà người dùng thuộc về sau khi thêm vào nhóm mới để đảm bảo rằng quyền hạn được thiết lập đúng cách.