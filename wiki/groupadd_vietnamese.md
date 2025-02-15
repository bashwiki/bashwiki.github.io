# [리눅스] Bash groupadd 사용법

## Tổng quan
Lệnh `groupadd` trong Bash được sử dụng để tạo một nhóm người dùng mới trên hệ thống Linux. Mục đích chính của lệnh này là quản lý quyền truy cập và phân quyền cho các người dùng trong một nhóm, giúp tổ chức và kiểm soát quyền truy cập vào tài nguyên hệ thống một cách hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `groupadd` như sau:

```bash
groupadd [tùy chọn] tên_nhóm
```

### Các tùy chọn phổ biến:
- `-g GID`: Chỉ định ID nhóm (GID) cho nhóm mới. Nếu không chỉ định, hệ thống sẽ tự động gán GID tiếp theo.
- `-r`: Tạo một nhóm hệ thống. Nhóm này thường được sử dụng cho các dịch vụ hệ thống và có GID nhỏ hơn 1000.
- `-f`: Nếu nhóm đã tồn tại, không tạo nhóm mới và không báo lỗi.

## Ví dụ
### Ví dụ 1: Tạo một nhóm mới
Để tạo một nhóm có tên là `developers`, bạn có thể sử dụng lệnh sau:

```bash
sudo groupadd developers
```

### Ví dụ 2: Tạo một nhóm hệ thống
Nếu bạn muốn tạo một nhóm hệ thống có tên là `sysadmins` với GID là 500, bạn có thể sử dụng lệnh sau:

```bash
sudo groupadd -g 500 sysadmins
```

## Mẹo
- Hãy chắc chắn rằng tên nhóm bạn muốn tạo chưa tồn tại trong hệ thống để tránh xung đột. Bạn có thể kiểm tra danh sách các nhóm hiện có bằng lệnh `getent group`.
- Sử dụng tùy chọn `-r` khi tạo nhóm cho các dịch vụ hệ thống để giữ cho GID của nhóm trong khoảng hợp lệ cho nhóm hệ thống.
- Để quản lý người dùng trong nhóm mới, bạn có thể sử dụng lệnh `usermod` để thêm người dùng vào nhóm đó sau khi nhóm đã được tạo.