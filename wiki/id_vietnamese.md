# [Linux] Bash id cách sử dụng: Xem thông tin người dùng

## Overview
Lệnh `id` trong Bash được sử dụng để hiển thị thông tin về người dùng hiện tại, bao gồm UID (User ID), GID (Group ID) và các nhóm mà người dùng thuộc về. Đây là một công cụ hữu ích để kiểm tra quyền truy cập và thông tin người dùng trong hệ thống.

## Usage
Cú pháp cơ bản của lệnh `id` như sau:
```
id [options] [arguments]
```

## Common Options
- `-u`: Hiển thị UID của người dùng.
- `-g`: Hiển thị GID của nhóm chính.
- `-G`: Hiển thị tất cả các GID mà người dùng thuộc về.
- `-n`: Hiển thị tên thay vì số cho UID hoặc GID.
- `-r`: Hiển thị UID và GID thực tế.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `id`:

1. Hiển thị thông tin của người dùng hiện tại:
   ```bash
   id
   ```

2. Hiển thị UID của người dùng hiện tại:
   ```bash
   id -u
   ```

3. Hiển thị GID của nhóm chính của người dùng hiện tại:
   ```bash
   id -g
   ```

4. Hiển thị tất cả các GID mà người dùng thuộc về:
   ```bash
   id -G
   ```

5. Hiển thị thông tin của một người dùng cụ thể (ví dụ: user1):
   ```bash
   id user1
   ```

## Tips
- Sử dụng `id -n` để dễ dàng đọc tên người dùng và nhóm thay vì số ID.
- Kiểm tra thông tin người dùng trước khi thực hiện các thay đổi liên quan đến quyền truy cập.
- Kết hợp lệnh `id` với các lệnh khác trong Bash để kiểm tra quyền truy cập một cách hiệu quả hơn.