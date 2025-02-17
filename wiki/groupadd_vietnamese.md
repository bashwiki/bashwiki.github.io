# [Linux] Bash groupadd Cách sử dụng: Tạo nhóm người dùng mới

## Overview
Lệnh `groupadd` trong Bash được sử dụng để tạo một nhóm người dùng mới trên hệ thống. Đây là một công cụ hữu ích cho việc quản lý người dùng và phân quyền truy cập trong môi trường đa người dùng.

## Usage
Cú pháp cơ bản của lệnh `groupadd` như sau:

```bash
groupadd [options] [arguments]
```

## Common Options
- `-g GID`: Chỉ định ID nhóm (GID) cho nhóm mới.
- `-r`: Tạo nhóm hệ thống, thường có GID nhỏ hơn 1000.
- `-f`: Nếu nhóm đã tồn tại, không tạo nhóm mới và không báo lỗi.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `groupadd`:

1. Tạo một nhóm người dùng mới có tên là `developers`:
   ```bash
   groupadd developers
   ```

2. Tạo một nhóm người dùng mới với GID là 1500:
   ```bash
   groupadd -g 1500 newgroup
   ```

3. Tạo một nhóm hệ thống có tên là `sysadmins`:
   ```bash
   groupadd -r sysadmins
   ```

4. Tạo một nhóm mới mà không báo lỗi nếu nhóm đã tồn tại:
   ```bash
   groupadd -f existinggroup
   ```

## Tips
- Luôn kiểm tra xem nhóm đã tồn tại hay chưa trước khi tạo nhóm mới để tránh lỗi không cần thiết.
- Sử dụng tùy chọn `-g` để quản lý GID một cách hiệu quả, đặc biệt trong các môi trường lớn.
- Kết hợp `groupadd` với các lệnh khác như `usermod` để thêm người dùng vào nhóm vừa tạo.