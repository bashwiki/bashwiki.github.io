# [Linux] Bash umask: [quản lý quyền truy cập tệp]

## Overview
Lệnh `umask` trong Bash được sử dụng để thiết lập quyền truy cập mặc định cho các tệp và thư mục mới được tạo ra. Nó xác định các quyền nào sẽ bị từ chối khi một tệp hoặc thư mục mới được tạo, giúp quản lý bảo mật cho hệ thống.

## Usage
Cú pháp cơ bản của lệnh `umask` như sau:

```bash
umask [options] [arguments]
```

## Common Options
- `-S`: Hiển thị umask dưới dạng ký hiệu.
- `-p`: Hiển thị umask hiện tại của shell hiện tại.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `umask`:

1. **Xem umask hiện tại**:
   ```bash
   umask
   ```

2. **Thiết lập umask mới**:
   ```bash
   umask 027
   ```
   Lệnh này sẽ thiết lập umask để các tệp mới sẽ có quyền 640 và thư mục mới sẽ có quyền 750.

3. **Hiển thị umask dưới dạng ký hiệu**:
   ```bash
   umask -S
   ```

4. **Thiết lập umask cho phiên làm việc hiện tại**:
   ```bash
   umask 002
   ```
   Điều này cho phép nhóm có quyền ghi vào các tệp mới.

## Tips
- Hãy chắc chắn kiểm tra umask hiện tại trước khi tạo tệp hoặc thư mục quan trọng.
- Sử dụng umask 007 để cho phép quyền truy cập đầy đủ cho người dùng và nhóm, nhưng không cho phép quyền truy cập cho người khác.
- Đặt umask trong tệp cấu hình shell của bạn (như `.bashrc` hoặc `.bash_profile`) để đảm bảo các thiết lập umask được áp dụng mỗi khi bạn đăng nhập.