# [Linux] Bash chown Cách sử dụng: Thay đổi quyền sở hữu tệp

## Overview
Lệnh `chown` trong Bash được sử dụng để thay đổi quyền sở hữu của tệp hoặc thư mục. Bạn có thể chỉ định người dùng và nhóm mà tệp hoặc thư mục sẽ thuộc về.

## Usage
Cú pháp cơ bản của lệnh `chown` như sau:
```bash
chown [options] [user][:group] [file]
```

## Common Options
- `-R`: Thay đổi quyền sở hữu một cách đệ quy cho tất cả các tệp và thư mục bên trong.
- `-v`: Hiển thị thông tin chi tiết về các tệp đã được thay đổi quyền sở hữu.
- `-c`: Chỉ hiển thị các tệp mà quyền sở hữu đã được thay đổi.

## Common Examples
1. **Thay đổi quyền sở hữu của một tệp cho người dùng cụ thể:**
   ```bash
   chown username file.txt
   ```

2. **Thay đổi quyền sở hữu của một thư mục và tất cả các tệp bên trong:**
   ```bash
   chown -R username directory/
   ```

3. **Thay đổi quyền sở hữu cho cả người dùng và nhóm:**
   ```bash
   chown username:groupname file.txt
   ```

4. **Hiển thị thông tin chi tiết khi thay đổi quyền sở hữu:**
   ```bash
   chown -v username file.txt
   ```

## Tips
- Luôn kiểm tra quyền sở hữu hiện tại của tệp trước khi thay đổi bằng lệnh `ls -l`.
- Sử dụng tùy chọn `-R` cẩn thận, vì nó sẽ thay đổi quyền sở hữu cho tất cả các tệp và thư mục con.
- Đảm bảo rằng bạn có quyền thực hiện thay đổi quyền sở hữu, thường cần quyền root hoặc sudo.