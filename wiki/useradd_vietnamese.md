# [Linux] Bash useradd Cách sử dụng: Tạo người dùng mới trong hệ thống

## Tổng quan
Lệnh `useradd` được sử dụng để tạo một người dùng mới trong hệ thống Linux. Lệnh này cho phép quản trị viên thêm người dùng mới với các tùy chọn cấu hình khác nhau.

## Cách sử dụng
Cú pháp cơ bản của lệnh `useradd` như sau:

```bash
useradd [options] [arguments]
```

## Các tùy chọn phổ biến
- `-m`: Tạo thư mục chính cho người dùng mới.
- `-s`: Chỉ định shell mặc định cho người dùng.
- `-G`: Thêm người dùng vào nhóm bổ sung.
- `-c`: Thêm mô tả cho người dùng.
- `-e`: Đặt ngày hết hạn cho tài khoản người dùng.

## Ví dụ phổ biến
- Tạo một người dùng mới với tên là `john`:

```bash
useradd john
```

- Tạo người dùng mới và tạo thư mục chính:

```bash
useradd -m john
```

- Tạo người dùng mới với shell mặc định là `/bin/bash`:

```bash
useradd -s /bin/bash john
```

- Tạo người dùng mới và thêm vào nhóm `developers`:

```bash
useradd -G developers john
```

- Tạo người dùng mới với mô tả:

```bash
useradd -c "Người dùng John Doe" john
```

## Mẹo
- Luôn sử dụng tùy chọn `-m` để đảm bảo rằng thư mục chính được tạo cho người dùng mới.
- Kiểm tra các nhóm hiện có trước khi thêm người dùng vào nhóm bằng lệnh `getent group`.
- Sau khi tạo người dùng, hãy nhớ đặt mật khẩu bằng lệnh `passwd` để bảo mật tài khoản.