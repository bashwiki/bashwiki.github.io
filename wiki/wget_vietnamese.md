# [리눅스] Bash wget 사용법

## Tổng quan
`wget` là một công cụ dòng lệnh mạnh mẽ được sử dụng để tải xuống các tệp từ Internet. Nó hỗ trợ nhiều giao thức như HTTP, HTTPS và FTP, cho phép người dùng tải xuống tệp một cách dễ dàng và hiệu quả. `wget` rất hữu ích cho các nhà phát triển và kỹ sư khi cần tải xuống dữ liệu hoặc tệp từ các máy chủ từ xa mà không cần phải mở trình duyệt web.

## Cách sử dụng
Cú pháp cơ bản của lệnh `wget` như sau:

```bash
wget [tùy chọn] [URL]
```

### Một số tùy chọn phổ biến:
- `-O [tên_tệp]`: Chỉ định tên tệp mà bạn muốn lưu khi tải xuống.
- `-c`: Tiếp tục tải xuống một tệp đã bị gián đoạn.
- `-r`: Tải xuống một trang web và tất cả các tài nguyên liên quan (recursive).
- `--limit-rate=[tốc độ]`: Giới hạn tốc độ tải xuống để tránh quá tải băng thông.

## Ví dụ
### Ví dụ 1: Tải xuống một tệp đơn giản
Để tải xuống một tệp từ một URL cụ thể, bạn có thể sử dụng lệnh sau:

```bash
wget https://example.com/file.zip
```

### Ví dụ 2: Tải xuống và đổi tên tệp
Nếu bạn muốn tải xuống tệp và lưu nó với một tên khác, bạn có thể sử dụng tùy chọn `-O`:

```bash
wget -O myfile.zip https://example.com/file.zip
```

## Mẹo
- Sử dụng tùy chọn `-c` để tiếp tục tải xuống nếu quá trình bị gián đoạn, điều này rất hữu ích khi tải xuống các tệp lớn.
- Nếu bạn đang tải xuống một trang web, hãy cẩn thận với tùy chọn `-r` vì nó có thể tải xuống rất nhiều tệp và tiêu tốn băng thông.
- Kiểm tra các tùy chọn khác bằng cách sử dụng `man wget` để tìm hiểu thêm về các tính năng nâng cao mà `wget` cung cấp.