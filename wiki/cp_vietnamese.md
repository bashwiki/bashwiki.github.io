# [Linux] Bash cp Cách sử dụng: Sao chép tệp và thư mục

## Tổng quan
Lệnh `cp` trong Bash được sử dụng để sao chép tệp và thư mục từ vị trí này sang vị trí khác. Đây là một trong những lệnh cơ bản và quan trọng trong quản lý tệp trên hệ thống Unix và Linux.

## Cách sử dụng
Cú pháp cơ bản của lệnh `cp` như sau:

```bash
cp [tùy chọn] [đối số]
```

## Tùy chọn phổ biến
- `-r`: Sao chép thư mục và tất cả các tệp con bên trong.
- `-i`: Yêu cầu xác nhận trước khi ghi đè lên tệp đã tồn tại.
- `-u`: Chỉ sao chép tệp nếu tệp nguồn mới hơn tệp đích hoặc nếu tệp đích không tồn tại.
- `-v`: Hiển thị thông tin chi tiết về quá trình sao chép.

## Ví dụ phổ biến
- Sao chép một tệp đơn giản:

```bash
cp file1.txt file2.txt
```

- Sao chép một thư mục và tất cả các tệp bên trong:

```bash
cp -r folder1 folder2
```

- Sao chép tệp và yêu cầu xác nhận nếu tệp đích đã tồn tại:

```bash
cp -i file1.txt file2.txt
```

- Sao chép tệp chỉ khi tệp nguồn mới hơn tệp đích:

```bash
cp -u file1.txt file2.txt
```

- Sao chép tệp và hiển thị thông tin chi tiết:

```bash
cp -v file1.txt file2.txt
```

## Mẹo
- Luôn kiểm tra tệp đích trước khi sao chép để tránh ghi đè lên dữ liệu quan trọng.
- Sử dụng tùy chọn `-i` để bảo vệ dữ liệu của bạn khỏi việc ghi đè không mong muốn.
- Khi sao chép thư mục, hãy luôn sử dụng tùy chọn `-r` để đảm bảo tất cả các tệp con được sao chép.