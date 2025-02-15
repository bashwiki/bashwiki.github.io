# [리눅스] Bash iptables 사용법

## Tổng quan
`iptables` là một công cụ dòng lệnh được sử dụng để cấu hình, quản lý và kiểm soát các quy tắc tường lửa trên hệ điều hành Linux. Nó cho phép người dùng định nghĩa các quy tắc để cho phép hoặc từ chối lưu lượng mạng dựa trên các tiêu chí như địa chỉ IP, cổng, giao thức và nhiều yếu tố khác. Mục đích chính của `iptables` là bảo vệ hệ thống khỏi các mối đe dọa từ mạng và quản lý lưu lượng mạng hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `iptables` như sau:

```bash
iptables [OPTION] [CHAIN] [RULE]
```

### Các tùy chọn phổ biến:
- `-A` (append): Thêm một quy tắc vào cuối chuỗi.
- `-D` (delete): Xóa một quy tắc khỏi chuỗi.
- `-L` (list): Liệt kê các quy tắc hiện tại trong chuỗi.
- `-F` (flush): Xóa tất cả các quy tắc trong chuỗi.
- `-P` (policy): Đặt chính sách mặc định cho chuỗi (chấp nhận hoặc từ chối).
- `-I` (insert): Chèn một quy tắc vào đầu chuỗi.

## Ví dụ
### Ví dụ 1: Liệt kê các quy tắc hiện tại
Để xem các quy tắc tường lửa hiện tại, bạn có thể sử dụng lệnh sau:

```bash
iptables -L -n -v
```

Lệnh này sẽ liệt kê tất cả các quy tắc trong các chuỗi hiện có, hiển thị thông tin chi tiết và không chuyển đổi địa chỉ IP thành tên miền.

### Ví dụ 2: Thêm quy tắc cho phép lưu lượng SSH
Để cho phép lưu lượng SSH (cổng 22) từ bất kỳ địa chỉ IP nào, bạn có thể sử dụng lệnh sau:

```bash
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

Lệnh này sẽ thêm một quy tắc vào chuỗi INPUT, cho phép tất cả các kết nối TCP đến cổng 22.

## Mẹo
- **Sao lưu và khôi phục quy tắc**: Trước khi thực hiện bất kỳ thay đổi nào, hãy sao lưu các quy tắc hiện tại bằng lệnh `iptables-save > iptables-backup.txt`. Bạn có thể khôi phục quy tắc từ tệp sao lưu bằng lệnh `iptables-restore < iptables-backup.txt`.
- **Kiểm tra quy tắc**: Sau khi thêm hoặc sửa đổi quy tắc, hãy luôn kiểm tra lại bằng lệnh `iptables -L` để đảm bảo rằng các quy tắc đã được áp dụng đúng cách.
- **Sử dụng chính sách mặc định**: Đặt chính sách mặc định cho chuỗi INPUT và OUTPUT là `DROP` và chỉ thêm các quy tắc cho phép cụ thể. Điều này giúp tăng cường bảo mật cho hệ thống của bạn.