# [Linux] Bash wget Cách sử dụng: Tải tệp từ Internet

## Tổng quan
Lệnh `wget` là một công cụ dòng lệnh mạnh mẽ dùng để tải tệp từ Internet. Nó hỗ trợ nhiều giao thức như HTTP, HTTPS và FTP, cho phép người dùng tải xuống các tệp một cách dễ dàng và hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `wget` như sau:

```bash
wget [tùy chọn] [đối số]
```

## Các tùy chọn phổ biến
- `-O <tên_tệp>`: Chỉ định tên tệp đầu ra.
- `-c`: Tiếp tục tải xuống một tệp bị gián đoạn.
- `-q`: Chạy trong chế độ im lặng, không hiển thị thông tin tải xuống.
- `--limit-rate=<tốc độ>`: Giới hạn tốc độ tải xuống.
- `-r`: Tải xuống một trang web và tất cả các tệp liên quan.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `wget`:

1. Tải xuống một tệp đơn giản:
   ```bash
   wget https://example.com/file.zip
   ```

2. Tải xuống và chỉ định tên tệp đầu ra:
   ```bash
   wget -O myfile.zip https://example.com/file.zip
   ```

3. Tiếp tục tải xuống một tệp bị gián đoạn:
   ```bash
   wget -c https://example.com/largefile.zip
   ```

4. Tải xuống một trang web cùng với tất cả các tệp liên quan:
   ```bash
   wget -r https://example.com
   ```

5. Giới hạn tốc độ tải xuống:
   ```bash
   wget --limit-rate=200k https://example.com/file.zip
   ```

## Mẹo
- Sử dụng tùy chọn `-q` để tải xuống mà không làm phiền người dùng với quá nhiều thông tin.
- Nếu bạn cần tải xuống nhiều tệp, hãy sử dụng một tệp danh sách và lệnh `-i` để chỉ định tệp đó.
- Kiểm tra tài liệu chính thức của `wget` để tìm hiểu thêm về các tùy chọn nâng cao và cách sử dụng hiệu quả.