# [Linux] Bash history cách sử dụng: Lưu trữ và truy xuất lệnh đã thực hiện

## Tổng quan
Lệnh `history` trong Bash cho phép người dùng xem lại danh sách các lệnh đã thực hiện trong phiên làm việc của họ. Điều này rất hữu ích để tìm kiếm lại các lệnh đã sử dụng mà không cần phải gõ lại từ đầu.

## Cách sử dụng
Cú pháp cơ bản của lệnh `history` như sau:

```bash
history [options] [arguments]
```

## Các tùy chọn phổ biến
- `-c`: Xóa toàn bộ lịch sử lệnh.
- `-d offset`: Xóa lệnh tại vị trí `offset` trong lịch sử.
- `n`: Chỉ hiển thị `n` lệnh gần nhất.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `history`:

1. **Hiển thị toàn bộ lịch sử lệnh:**
   ```bash
   history
   ```

2. **Hiển thị 10 lệnh gần nhất:**
   ```bash
   history 10
   ```

3. **Xóa lệnh tại vị trí thứ 5:**
   ```bash
   history -d 5
   ```

4. **Xóa toàn bộ lịch sử lệnh:**
   ```bash
   history -c
   ```

## Mẹo
- Sử dụng phím mũi tên lên/xuống để duyệt qua các lệnh đã thực hiện mà không cần gõ lại.
- Bạn có thể sử dụng `!n` để thực hiện lại lệnh tại vị trí `n` trong lịch sử.
- Để lưu lịch sử lệnh vào một tệp, bạn có thể sử dụng lệnh `history > filename.txt`.