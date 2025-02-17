# [Linux] Bash export cách sử dụng: Thiết lập biến môi trường

## Tổng quan
Lệnh `export` trong Bash được sử dụng để thiết lập và xuất các biến môi trường, cho phép các biến này có thể được truy cập bởi các tiến trình con. Khi một biến được xuất, nó trở thành một phần của môi trường của shell và có thể được sử dụng bởi các chương trình khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `export` như sau:

```bash
export [options] [arguments]
```

## Các tùy chọn phổ biến
- `-p`: Hiển thị tất cả các biến môi trường đã được xuất.
- `-n`: Hủy xuất một biến môi trường.
- `VAR=value`: Thiết lập giá trị cho biến môi trường `VAR` và xuất nó.

## Ví dụ thường gặp
1. Xuất một biến môi trường:
   ```bash
   export MY_VAR="Hello, World!"
   ```

2. Kiểm tra biến môi trường đã xuất:
   ```bash
   echo $MY_VAR
   ```

3. Xuất nhiều biến cùng lúc:
   ```bash
   export VAR1="Value1" VAR2="Value2"
   ```

4. Hủy xuất một biến môi trường:
   ```bash
   export -n MY_VAR
   ```

5. Hiển thị tất cả các biến môi trường đã xuất:
   ```bash
   export -p
   ```

## Mẹo
- Hãy nhớ rằng các biến môi trường chỉ có thể được truy cập bởi các tiến trình con, vì vậy nếu bạn cần sử dụng biến trong một shell khác, bạn phải xuất nó trong shell đó.
- Sử dụng `export` trong tệp cấu hình như `.bashrc` hoặc `.bash_profile` để tự động xuất các biến khi bạn mở một phiên làm việc mới.
- Tránh sử dụng tên biến trùng với các lệnh hệ thống để tránh nhầm lẫn.