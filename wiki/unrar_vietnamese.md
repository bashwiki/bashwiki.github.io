# [Linux] Bash unrar cách sử dụng: Giải nén tệp RAR

## Tổng quan
Lệnh `unrar` được sử dụng để giải nén các tệp tin nén định dạng RAR. Đây là công cụ hữu ích cho việc truy cập và quản lý nội dung bên trong các tệp RAR.

## Cách sử dụng
Cú pháp cơ bản của lệnh `unrar` như sau:

```bash
unrar [options] [arguments]
```

## Các tùy chọn phổ biến
- `x`: Giải nén tệp vào thư mục hiện tại.
- `e`: Giải nén tệp mà không giữ lại cấu trúc thư mục.
- `l`: Liệt kê nội dung của tệp RAR mà không giải nén.
- `t`: Kiểm tra tính toàn vẹn của tệp RAR.
- `v`: Hiển thị thông tin chi tiết về tệp RAR.

## Ví dụ thường gặp
- Giải nén tệp RAR vào thư mục hiện tại:

```bash
unrar x file.rar
```

- Giải nén tệp RAR vào một thư mục cụ thể:

```bash
unrar x file.rar /path/to/directory/
```

- Liệt kê nội dung của tệp RAR:

```bash
unrar l file.rar
```

- Kiểm tra tính toàn vẹn của tệp RAR:

```bash
unrar t file.rar
```

## Mẹo
- Đảm bảo rằng bạn đã cài đặt `unrar` trên hệ thống của mình. Bạn có thể cài đặt nó bằng cách sử dụng trình quản lý gói của hệ điều hành.
- Sử dụng tùy chọn `-y` để tự động trả lời "yes" cho tất cả các câu hỏi trong quá trình giải nén.
- Nếu bạn không muốn giữ lại cấu trúc thư mục, hãy sử dụng tùy chọn `e` để giải nén tất cả tệp vào thư mục hiện tại mà không tạo thư mục con.