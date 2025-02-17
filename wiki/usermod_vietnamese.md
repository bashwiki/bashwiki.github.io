# [Linux] Bash usermod cách sử dụng: Thay đổi thông tin người dùng

## Tổng quan
Lệnh `usermod` trong Bash được sử dụng để thay đổi thông tin của người dùng trên hệ thống Linux. Bạn có thể thay đổi tên đăng nhập, nhóm người dùng, và nhiều thuộc tính khác liên quan đến tài khoản người dùng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `usermod` như sau:
```
usermod [options] [arguments]
```

## Các tùy chọn phổ biến
- `-l, --login NEW_LOGIN`: Đổi tên đăng nhập của người dùng.
- `-d, --home NEW_HOME`: Thay đổi thư mục chính của người dùng.
- `-m, --move-home`: Di chuyển thư mục chính của người dùng đến vị trí mới.
- `-G, --groups GROUP1[,GROUP2,...]`: Thêm người dùng vào các nhóm mới.
- `-a, --append`: Thêm người dùng vào nhóm mà không xóa các nhóm hiện tại.
- `-s, --shell SHELL`: Thay đổi shell mặc định cho người dùng.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `usermod`:

1. **Đổi tên đăng nhập của người dùng**:
   ```bash
   usermod -l newusername oldusername
   ```

2. **Thay đổi thư mục chính của người dùng**:
   ```bash
   usermod -d /new/home/directory username
   ```

3. **Di chuyển thư mục chính của người dùng đến vị trí mới**:
   ```bash
   usermod -m -d /new/home/directory username
   ```

4. **Thêm người dùng vào nhóm mới**:
   ```bash
   usermod -G group1,group2 username
   ```

5. **Thay đổi shell mặc định cho người dùng**:
   ```bash
   usermod -s /bin/bash username
   ```

## Mẹo
- Luôn sao lưu dữ liệu quan trọng trước khi thực hiện thay đổi lớn trên tài khoản người dùng.
- Kiểm tra các nhóm hiện tại của người dùng bằng lệnh `groups username` trước khi thêm hoặc thay đổi.
- Sử dụng tùy chọn `-a` khi thêm người dùng vào nhóm để đảm bảo không xóa các nhóm hiện tại.
- Đảm bảo rằng bạn có quyền truy cập root hoặc sử dụng `sudo` để thực hiện lệnh `usermod`.