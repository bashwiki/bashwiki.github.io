# [리눅스] Bash cp 사용법

## Tổng quan
Lệnh `cp` trong Bash được sử dụng để sao chép các tệp và thư mục từ vị trí này sang vị trí khác. Đây là một trong những lệnh cơ bản và thường xuyên được sử dụng trong quản lý tệp trên hệ điều hành Unix và Linux. Mục đích chính của lệnh này là giúp người dùng dễ dàng tạo bản sao của các tệp mà không làm thay đổi tệp gốc.

## Cách sử dụng
Cú pháp cơ bản của lệnh `cp` như sau:

```bash
cp [tùy chọn] nguồn đích
```

Trong đó:
- `nguồn`: Đường dẫn đến tệp hoặc thư mục mà bạn muốn sao chép.
- `đích`: Đường dẫn đến nơi bạn muốn lưu bản sao.

Một số tùy chọn phổ biến của lệnh `cp` bao gồm:
- `-r`: Sao chép thư mục và nội dung của nó một cách đệ quy.
- `-i`: Yêu cầu xác nhận trước khi ghi đè lên tệp đích nếu nó đã tồn tại.
- `-u`: Chỉ sao chép tệp nếu tệp nguồn mới hơn tệp đích hoặc nếu tệp đích không tồn tại.
- `-v`: Hiển thị thông tin chi tiết về quá trình sao chép.

## Ví dụ
### Ví dụ 1: Sao chép tệp
Để sao chép một tệp có tên `file.txt` vào thư mục `backup`, bạn có thể sử dụng lệnh sau:

```bash
cp file.txt backup/
```

### Ví dụ 2: Sao chép thư mục
Để sao chép một thư mục có tên `myfolder` cùng với tất cả nội dung bên trong, bạn sử dụng tùy chọn `-r`:

```bash
cp -r myfolder/ backup/
```

## Mẹo
- Luôn sử dụng tùy chọn `-i` khi bạn không chắc chắn về việc ghi đè lên tệp đích để tránh mất dữ liệu.
- Kiểm tra kỹ đường dẫn của tệp nguồn và tệp đích để đảm bảo bạn đang sao chép vào đúng vị trí.
- Sử dụng tùy chọn `-v` để theo dõi quá trình sao chép, đặc biệt khi sao chép nhiều tệp hoặc thư mục lớn.