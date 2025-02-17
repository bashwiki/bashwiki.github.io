# [Linux] Bash man lệnh: Truy cập tài liệu hướng dẫn

## Tổng quan
Lệnh `man` trong Bash được sử dụng để truy cập tài liệu hướng dẫn cho các lệnh và chương trình trong hệ thống. Nó cung cấp thông tin chi tiết về cách sử dụng, các tùy chọn và các ví dụ cho từng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `man` như sau:

```bash
man [tùy chọn] [lệnh]
```

## Các tùy chọn phổ biến
- `-k`: Tìm kiếm các mục trong cơ sở dữ liệu man dựa trên từ khóa.
- `-f`: Hiển thị một mô tả ngắn gọn về lệnh.
- `-a`: Xem tất cả các mục man liên quan đến lệnh, không chỉ mục đầu tiên.
- `-w`: Hiển thị đường dẫn đến tệp man mà không mở nó.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `man`:

1. Xem tài liệu hướng dẫn cho lệnh `ls`:
   ```bash
   man ls
   ```

2. Tìm kiếm các mục man liên quan đến từ khóa "copy":
   ```bash
   man -k copy
   ```

3. Hiển thị mô tả ngắn gọn về lệnh `cp`:
   ```bash
   man -f cp
   ```

4. Xem tất cả các mục man cho lệnh `mkdir`:
   ```bash
   man -a mkdir
   ```

5. Hiển thị đường dẫn đến tệp man cho lệnh `grep`:
   ```bash
   man -w grep
   ```

## Mẹo
- Sử dụng phím `q` để thoát khỏi tài liệu man khi bạn đã xem xong.
- Bạn có thể tìm kiếm trong tài liệu man bằng cách nhấn `/` và nhập từ khóa cần tìm.
- Để xem các mục man trong các phần khác nhau (như phần 1 cho lệnh, phần 5 cho định dạng tệp), bạn có thể chỉ định số phần, ví dụ: `man 5 passwd`.