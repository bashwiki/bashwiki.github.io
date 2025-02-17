# [Linux] Bash sudo cách sử dụng: Thực thi lệnh với quyền quản trị

## Tổng quan
Lệnh `sudo` cho phép người dùng thực thi các lệnh với quyền của người dùng khác, thường là quyền của người quản trị (root). Điều này rất hữu ích khi bạn cần thực hiện các tác vụ yêu cầu quyền cao hơn mà tài khoản người dùng hiện tại không có.

## Cách sử dụng
Cú pháp cơ bản của lệnh `sudo` như sau:
```
sudo [options] [arguments]
```

## Các tùy chọn phổ biến
- `-u [user]`: Chạy lệnh với quyền của người dùng chỉ định.
- `-k`: Xóa thông tin xác thực đã lưu, yêu cầu nhập mật khẩu lần sau.
- `-l`: Liệt kê các lệnh mà người dùng hiện tại có quyền thực thi với `sudo`.
- `-i`: Chạy lệnh trong một shell tương tự như shell của người dùng chỉ định.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế khi sử dụng lệnh `sudo`:

1. Cập nhật danh sách gói trên hệ thống:
   ```bash
   sudo apt update
   ```

2. Cài đặt một gói phần mềm:
   ```bash
   sudo apt install [tên-gói]
   ```

3. Khởi động lại dịch vụ:
   ```bash
   sudo systemctl restart [tên-dịch-vụ]
   ```

4. Chạy một lệnh với quyền của người dùng khác:
   ```bash
   sudo -u [tên-người-dùng] [lệnh]
   ```

## Mẹo
- Hãy cẩn thận khi sử dụng `sudo`, vì việc thực thi lệnh với quyền quản trị có thể gây ra các thay đổi lớn cho hệ thống.
- Sử dụng tùy chọn `-l` để kiểm tra quyền của bạn trước khi thực hiện lệnh.
- Nếu bạn thường xuyên cần quyền quản trị, hãy xem xét việc cấu hình tệp `/etc/sudoers` để giảm thiểu việc nhập mật khẩu, nhưng hãy làm điều này một cách cẩn thận để tránh lỗ hổng bảo mật.