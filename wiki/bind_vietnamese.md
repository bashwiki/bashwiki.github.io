# [Linux] Bash bind cách sử dụng: Gán phím tắt cho lệnh

## Tổng quan
Lệnh `bind` trong Bash cho phép người dùng gán các phím tắt cho các lệnh hoặc hành động cụ thể trong shell. Điều này giúp tăng tốc độ làm việc và cải thiện hiệu suất khi sử dụng dòng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `bind` như sau:
```bash
bind [options] [arguments]
```

## Các tùy chọn phổ biến
- `-p`: Hiển thị danh sách các phím tắt hiện tại.
- `-s`: Gán một chuỗi lệnh cho một phím tắt.
- `-f`: Nhập một tệp chứa các lệnh để gán cho phím tắt.
- `-q`: Kiểm tra xem một phím tắt có tồn tại hay không.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `bind`:

1. **Hiển thị danh sách các phím tắt hiện tại:**
   ```bash
   bind -p
   ```

2. **Gán phím tắt Ctrl + x cho lệnh `ls`:**
   ```bash
   bind '"\C-x": "ls\n"'
   ```

3. **Gán phím tắt Alt + h cho lệnh `history`:**
   ```bash
   bind '"\eh": "history\n"'
   ```

4. **Nhập từ tệp để gán phím tắt:**
   ```bash
   bind -f my_bindings.txt
   ```

## Mẹo
- Hãy thử nghiệm với các phím tắt khác nhau để tìm ra những gì phù hợp nhất với cách làm việc của bạn.
- Lưu lại các gán phím tắt trong tệp cấu hình `.bashrc` để tự động áp dụng mỗi khi mở terminal.
- Sử dụng lệnh `bind -p` để kiểm tra các phím tắt đã gán và tránh xung đột với các phím tắt khác.