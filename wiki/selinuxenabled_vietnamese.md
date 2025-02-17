# [Linux] Bash selinuxenabled <Kiểm tra trạng thái SELinux>: Kiểm tra xem SELinux có được kích hoạt hay không

## Tổng quan
Lệnh `selinuxenabled` được sử dụng để kiểm tra xem SELinux (Security-Enhanced Linux) có được kích hoạt trên hệ thống hay không. Nếu SELinux đang hoạt động, lệnh sẽ trả về mã thoát 0, ngược lại, nó sẽ trả về mã thoát 1.

## Cú pháp
Cú pháp cơ bản của lệnh `selinuxenabled` như sau:

```bash
selinuxenabled [options]
```

## Các tùy chọn phổ biến
- Không có tùy chọn nào đặc biệt cho lệnh này. Nó chỉ đơn giản là kiểm tra trạng thái của SELinux.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế khi sử dụng lệnh `selinuxenabled`:

1. **Kiểm tra trạng thái SELinux**:
   ```bash
   selinuxenabled
   ```

2. **Kiểm tra trạng thái và sử dụng trong một câu lệnh điều kiện**:
   ```bash
   if selinuxenabled; then
       echo "SELinux is enabled."
   else
       echo "SELinux is not enabled."
   fi
   ```

3. **Sử dụng trong một script**:
   ```bash
   #!/bin/bash
   if selinuxenabled; then
       echo "SELinux is active."
   else
       echo "SELinux is inactive."
   fi
   ```

## Mẹo
- **Sử dụng trong các script**: Lệnh `selinuxenabled` rất hữu ích để kiểm tra trạng thái SELinux trong các script tự động hóa, giúp bạn thực hiện các hành động khác nhau dựa trên trạng thái của SELinux.
- **Kết hợp với các lệnh khác**: Bạn có thể kết hợp lệnh này với các lệnh khác để thực hiện các tác vụ bảo mật tùy thuộc vào trạng thái của SELinux.
- **Kiểm tra mã thoát**: Để kiểm tra mã thoát của lệnh, bạn có thể sử dụng biến `$?` ngay sau khi chạy lệnh `selinuxenabled`.