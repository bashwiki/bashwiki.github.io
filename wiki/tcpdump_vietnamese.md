# [Linux] Bash tcpdump Cách sử dụng: Công cụ phân tích lưu lượng mạng

## Tổng quan
Lệnh `tcpdump` là một công cụ mạnh mẽ dùng để phân tích và ghi lại lưu lượng mạng trên các giao thức TCP/IP. Nó cho phép người dùng xem các gói dữ liệu đang đi qua một giao diện mạng cụ thể, giúp trong việc khắc phục sự cố và giám sát mạng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `tcpdump` như sau:

```bash
tcpdump [options] [arguments]
```

## Các tùy chọn phổ biến
- `-i <interface>`: Chỉ định giao diện mạng để theo dõi.
- `-n`: Không phân giải tên miền, hiển thị địa chỉ IP.
- `-v`: Hiển thị thông tin chi tiết hơn về các gói.
- `-c <count>`: Dừng sau khi đã ghi lại số lượng gói chỉ định.
- `-w <file>`: Ghi lại lưu lượng vào một tệp tin.
- `-r <file>`: Đọc lưu lượng từ một tệp tin đã ghi.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế khi sử dụng lệnh `tcpdump`:

1. Theo dõi lưu lượng trên giao diện mạng `eth0`:
   ```bash
   tcpdump -i eth0
   ```

2. Ghi lại 10 gói dữ liệu vào tệp tin `capture.pcap`:
   ```bash
   tcpdump -i eth0 -c 10 -w capture.pcap
   ```

3. Xem lưu lượng mà không phân giải tên miền:
   ```bash
   tcpdump -i eth0 -n
   ```

4. Đọc lưu lượng từ tệp tin đã ghi:
   ```bash
   tcpdump -r capture.pcap
   ```

5. Theo dõi lưu lượng HTTP (cổng 80):
   ```bash
   tcpdump -i eth0 port 80
   ```

## Mẹo
- Luôn sử dụng tùy chọn `-n` để tránh việc phân giải tên miền, giúp lệnh chạy nhanh hơn.
- Sử dụng tùy chọn `-v` hoặc `-vv` để có thêm thông tin chi tiết về các gói.
- Hãy chắc chắn rằng bạn có quyền truy cập vào giao diện mạng mà bạn muốn theo dõi, có thể cần quyền root.
- Lưu trữ các bản ghi vào tệp tin để phân tích sau này, sử dụng tùy chọn `-w` và `-r`.