# [Linux] Bash rm Cách sử dụng: Xóa tệp và thư mục

## Tổng quan
Lệnh `rm` trong Bash được sử dụng để xóa các tệp và thư mục. Đây là một công cụ mạnh mẽ, nhưng cần được sử dụng cẩn thận vì các tệp bị xóa sẽ không thể phục hồi dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `rm` như sau:

```bash
rm [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-f`: Bỏ qua xác nhận và xóa tệp mà không thông báo lỗi.
- `-i`: Yêu cầu xác nhận trước khi xóa mỗi tệp.
- `-r`: Xóa thư mục và tất cả các tệp bên trong nó một cách đệ quy.
- `-v`: Hiển thị thông tin chi tiết về các tệp đang được xóa.

## Ví dụ phổ biến
- Xóa một tệp đơn giản:
  ```bash
  rm file.txt
  ```

- Xóa nhiều tệp cùng lúc:
  ```bash
  rm file1.txt file2.txt file3.txt
  ```

- Xóa một thư mục và tất cả các tệp bên trong:
  ```bash
  rm -r my_directory/
  ```

- Xóa tệp mà không yêu cầu xác nhận:
  ```bash
  rm -f file.txt
  ```

- Xóa tệp với xác nhận trước:
  ```bash
  rm -i file.txt
  ```

## Mẹo
- Luôn kiểm tra kỹ trước khi sử dụng lệnh `rm`, đặc biệt là với tùy chọn `-r` và `-f`.
- Sử dụng tùy chọn `-i` để tránh xóa nhầm các tệp quan trọng.
- Cân nhắc sử dụng lệnh `trash-cli` để di chuyển tệp vào thùng rác thay vì xóa vĩnh viễn, giúp dễ dàng phục hồi nếu cần.