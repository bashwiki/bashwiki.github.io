# [리눅스] Bash curl 사용법

## Tổng quan
`curl` là một công cụ dòng lệnh mạnh mẽ được sử dụng để truyền tải dữ liệu từ hoặc đến một máy chủ thông qua các giao thức khác nhau như HTTP, HTTPS, FTP và nhiều hơn nữa. Mục đích chính của `curl` là giúp người dùng thực hiện các yêu cầu mạng một cách dễ dàng và linh hoạt, cho phép kiểm tra và tương tác với các API, tải xuống tệp tin, và nhiều tác vụ khác liên quan đến mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `curl` như sau:

```bash
curl [options] [URL]
```

Trong đó:
- `[options]`: Các tùy chọn để điều chỉnh hành vi của `curl`.
- `[URL]`: Địa chỉ của tài nguyên mà bạn muốn truy cập.

Một số tùy chọn phổ biến của `curl` bao gồm:
- `-X`: Chỉ định phương thức HTTP (GET, POST, PUT, DELETE, v.v.).
- `-d`: Gửi dữ liệu trong yêu cầu POST.
- `-H`: Thêm tiêu đề HTTP vào yêu cầu.
- `-o`: Lưu kết quả vào tệp tin thay vì hiển thị trên màn hình.
- `-I`: Chỉ lấy tiêu đề của phản hồi.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng `curl`:

1. **Gửi yêu cầu GET đến một URL**:
   ```bash
   curl https://api.example.com/data
   ```
   Lệnh này sẽ gửi một yêu cầu GET đến URL và hiển thị phản hồi trên màn hình.

2. **Gửi yêu cầu POST với dữ liệu**:
   ```bash
   curl -X POST -d "name=John&age=30" https://api.example.com/users
   ```
   Lệnh này sẽ gửi một yêu cầu POST đến URL với dữ liệu tên và tuổi, thường được sử dụng để tạo một người dùng mới trong API.

## Mẹo
- Sử dụng tùy chọn `-o` để lưu phản hồi vào tệp tin, giúp bạn dễ dàng quản lý dữ liệu:
  ```bash
  curl -o response.json https://api.example.com/data
  ```
- Khi làm việc với API, hãy sử dụng tùy chọn `-H` để thêm các tiêu đề cần thiết như token xác thực:
  ```bash
  curl -H "Authorization: Bearer YOUR_TOKEN" https://api.example.com/protected
  ```
- Để theo dõi quá trình tải xuống, bạn có thể thêm tùy chọn `-#` để hiển thị thanh tiến trình:
  ```bash
  curl -# -O https://example.com/largefile.zip
  ```

Với những thông tin trên, bạn đã có cái nhìn tổng quan và cách sử dụng cơ bản của lệnh `curl` trong Bash.