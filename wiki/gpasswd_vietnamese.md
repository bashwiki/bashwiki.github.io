# [Linux] Bash gpasswd <Sử dụng tương đương>: Quản lý nhóm người dùng

## Tổng quan
Lệnh `gpasswd` được sử dụng để quản lý các nhóm người dùng trong hệ thống Linux. Nó cho phép bạn thêm hoặc xóa người dùng khỏi nhóm, cũng như thay đổi mật khẩu cho nhóm.

## Cách sử dụng
Cú pháp cơ bản của lệnh `gpasswd` như sau:
```
gpasswd [tùy chọn] [tham số]
```

## Các tùy chọn phổ biến
- `-a, --add`: Thêm người dùng vào nhóm.
- `-d, --delete`: Xóa người dùng khỏi nhóm.
- `-r, --remove`: Xóa nhóm (cần quyền quản trị).
- `-P, --password`: Đặt mật khẩu cho nhóm.

## Ví dụ phổ biến
1. **Thêm người dùng vào nhóm**
   ```bash
   gpasswd -a username groupname
   ```
   Ví dụ: Thêm người dùng `alice` vào nhóm `developers`.
   ```bash
   gpasswd -a alice developers
   ```

2. **Xóa người dùng khỏi nhóm**
   ```bash
   gpasswd -d username groupname
   ```
   Ví dụ: Xóa người dùng `bob` khỏi nhóm `admins`.
   ```bash
   gpasswd -d bob admins
   ```

3. **Đặt mật khẩu cho nhóm**
   ```bash
   gpasswd groupname
   ```
   Ví dụ: Đặt mật khẩu cho nhóm `managers`.
   ```bash
   gpasswd managers
   ```

## Mẹo
- Hãy chắc chắn rằng bạn có quyền quản trị khi sử dụng `gpasswd` để thêm hoặc xóa người dùng khỏi nhóm.
- Kiểm tra các nhóm hiện có và người dùng trong nhóm bằng lệnh `getent group`.
- Sử dụng `gpasswd` cẩn thận, vì việc xóa người dùng khỏi nhóm có thể ảnh hưởng đến quyền truy cập của họ.