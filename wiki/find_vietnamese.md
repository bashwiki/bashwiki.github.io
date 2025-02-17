# [Linux] Bash find cách sử dụng: Tìm kiếm tên tệp

## Tổng quan
Lệnh `find` trong Bash được sử dụng để tìm kiếm các tệp và thư mục trong hệ thống tệp dựa trên các tiêu chí mà người dùng chỉ định. Nó rất mạnh mẽ và linh hoạt, cho phép người dùng tìm kiếm theo tên, kích thước, thời gian sửa đổi và nhiều thuộc tính khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `find` như sau:

```
find [tùy chọn] [đối số]
```

## Các tùy chọn phổ biến
- `-name`: Tìm kiếm tệp theo tên.
- `-type`: Chỉ định loại tệp (vd: `f` cho tệp thường, `d` cho thư mục).
- `-size`: Tìm kiếm tệp theo kích thước.
- `-mtime`: Tìm kiếm tệp theo thời gian sửa đổi.
- `-exec`: Thực thi một lệnh trên các tệp được tìm thấy.

## Ví dụ phổ biến
1. Tìm tất cả các tệp có đuôi `.txt` trong thư mục hiện tại:
   ```bash
   find . -name "*.txt"
   ```

2. Tìm tất cả các thư mục trong `/home/user`:
   ```bash
   find /home/user -type d
   ```

3. Tìm các tệp lớn hơn 100MB:
   ```bash
   find . -size +100M
   ```

4. Tìm các tệp đã được sửa đổi trong vòng 7 ngày qua:
   ```bash
   find . -mtime -7
   ```

5. Xóa tất cả các tệp `.tmp` trong thư mục hiện tại:
   ```bash
   find . -name "*.tmp" -exec rm {} \;
   ```

## Mẹo
- Sử dụng `-iname` thay vì `-name` để tìm kiếm không phân biệt chữ hoa chữ thường.
- Kết hợp nhiều tùy chọn để thu hẹp kết quả tìm kiếm.
- Luôn kiểm tra kết quả tìm kiếm trước khi thực hiện các lệnh như `rm` để tránh xóa nhầm tệp.