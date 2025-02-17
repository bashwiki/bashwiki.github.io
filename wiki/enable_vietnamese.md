# [Linux] Bash enable lệnh: Kích hoạt hoặc vô hiệu hóa lệnh shell

## Tổng quan
Lệnh `enable` trong Bash được sử dụng để kích hoạt hoặc vô hiệu hóa các lệnh shell được xây dựng sẵn. Nó cho phép người dùng quản lý các lệnh mà họ muốn sử dụng trong phiên làm việc của mình.

## Cú pháp
Cú pháp cơ bản của lệnh `enable` như sau:
```
enable [options] [arguments]
```

## Các tùy chọn phổ biến
- `-n`: Vô hiệu hóa lệnh được chỉ định.
- `-a`: Kích hoạt tất cả các lệnh shell có sẵn.
- `-p`: Hiển thị trạng thái của các lệnh mà không thay đổi chúng.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `enable`:

1. **Kích hoạt một lệnh shell cụ thể**:
   ```bash
   enable command_name
   ```

2. **Vô hiệu hóa một lệnh shell cụ thể**:
   ```bash
   enable -n command_name
   ```

3. **Kích hoạt tất cả các lệnh shell**:
   ```bash
   enable -a
   ```

4. **Hiển thị trạng thái của các lệnh shell**:
   ```bash
   enable -p
   ```

## Mẹo
- Hãy kiểm tra trạng thái của các lệnh shell trước khi kích hoạt hoặc vô hiệu hóa chúng để tránh nhầm lẫn.
- Sử dụng `enable -p` để xem danh sách các lệnh đã được kích hoạt hoặc vô hiệu hóa trong phiên làm việc hiện tại.
- Lưu ý rằng việc vô hiệu hóa một lệnh có thể ảnh hưởng đến các script hoặc lệnh khác mà bạn đang chạy.