# [Linux] Bash nohup cách sử dụng: Chạy lệnh không bị ngắt kết nối

## Tổng quan
Lệnh `nohup` (no hang up) cho phép bạn chạy một lệnh mà không bị ngắt kết nối khi bạn đăng xuất khỏi phiên làm việc. Điều này rất hữu ích cho các tác vụ dài hạn hoặc khi bạn muốn đảm bảo rằng một lệnh vẫn tiếp tục chạy ngay cả khi bạn không còn kết nối với máy chủ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `nohup` như sau:

```bash
nohup [tùy chọn] [tham số] &
```

## Các tùy chọn phổ biến
- `&`: Chạy lệnh ở chế độ nền.
- `-h`: Hiển thị trợ giúp về lệnh `nohup`.
- `-v`: Hiển thị thông tin chi tiết về lệnh đang chạy.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `nohup`:

1. Chạy một script Python trong nền:
   ```bash
   nohup python my_script.py &
   ```

2. Chạy một lệnh `ping` liên tục và ghi lại đầu ra vào một tệp:
   ```bash
   nohup ping google.com > ping_output.txt &
   ```

3. Chạy một lệnh `sleep` trong 1 giờ:
   ```bash
   nohup sleep 3600 &
   ```

4. Chạy một lệnh `rsync` để sao lưu dữ liệu:
   ```bash
   nohup rsync -av /source/directory /destination/directory &
   ```

## Mẹo
- Sử dụng `nohup` cùng với `&` để đảm bảo lệnh chạy ở chế độ nền và không bị ngắt kết nối.
- Kiểm tra tệp `nohup.out` để xem đầu ra của lệnh nếu không chỉ định tệp đầu ra khác.
- Đảm bảo rằng bạn đã kiểm tra các quyền truy cập cần thiết cho các tệp hoặc thư mục mà bạn đang làm việc để tránh lỗi khi chạy lệnh.