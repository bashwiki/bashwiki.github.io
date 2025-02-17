# [Linux] Bash curl cách sử dụng: Gửi và nhận dữ liệu qua giao thức HTTP

## Tổng quan
Lệnh `curl` là một công cụ dòng lệnh mạnh mẽ được sử dụng để gửi và nhận dữ liệu qua các giao thức mạng như HTTP, HTTPS, FTP, và nhiều giao thức khác. Nó cho phép người dùng tương tác với các API và tải xuống hoặc tải lên tệp tin một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `curl` như sau:
```
curl [options] [arguments]
```

## Các tùy chọn phổ biến
- `-X, --request <method>`: Chỉ định phương thức HTTP (GET, POST, PUT, DELETE, v.v.).
- `-d, --data <data>`: Gửi dữ liệu trong yêu cầu POST.
- `-H, --header <header>`: Thêm tiêu đề HTTP vào yêu cầu.
- `-o, --output <file>`: Ghi dữ liệu nhận được vào tệp tin.
- `-I, --head`: Chỉ lấy tiêu đề HTTP mà không tải nội dung.

## Ví dụ phổ biến
- **Gửi yêu cầu GET đơn giản**:
```bash
curl http://example.com
```

- **Gửi yêu cầu POST với dữ liệu**:
```bash
curl -X POST -d "name=John&age=30" http://example.com/api
```

- **Thêm tiêu đề vào yêu cầu**:
```bash
curl -H "Authorization: Bearer token" http://example.com/protected
```

- **Tải xuống tệp tin**:
```bash
curl -o myfile.txt http://example.com/file.txt
```

- **Lấy chỉ tiêu đề HTTP**:
```bash
curl -I http://example.com
```

## Mẹo
- Sử dụng `-v` để xem thông tin chi tiết về yêu cầu và phản hồi, hữu ích cho việc gỡ lỗi.
- Nếu bạn cần gửi dữ liệu JSON, hãy sử dụng `-H "Content-Type: application/json"` cùng với `-d`.
- Để lưu lại lịch sử yêu cầu, bạn có thể sử dụng `-o` để ghi vào tệp tin và kiểm tra sau này.