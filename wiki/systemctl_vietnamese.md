# [리눅스] Bash systemctl 사용법

## Tổng quan
`systemctl` là một công cụ dòng lệnh trong hệ thống Linux, được sử dụng để quản lý hệ thống và dịch vụ. Nó là một phần của systemd, một hệ thống khởi động và quản lý dịch vụ. Với `systemctl`, người dùng có thể khởi động, dừng, khởi động lại, kiểm tra trạng thái và quản lý các dịch vụ và đơn vị (units) trong hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `systemctl` như sau:

```
systemctl [tùy chọn] [hành động] [tên đơn vị]
```

### Các tùy chọn phổ biến:
- `start`: Khởi động một dịch vụ.
- `stop`: Dừng một dịch vụ.
- `restart`: Khởi động lại một dịch vụ.
- `status`: Kiểm tra trạng thái của một dịch vụ.
- `enable`: Bật tự động khởi động dịch vụ khi hệ thống khởi động.
- `disable`: Tắt tự động khởi động dịch vụ khi hệ thống khởi động.
- `list-units`: Liệt kê tất cả các đơn vị đang hoạt động.

## Ví dụ
### Ví dụ 1: Kiểm tra trạng thái của một dịch vụ
Để kiểm tra trạng thái của dịch vụ `nginx`, bạn có thể sử dụng lệnh sau:

```bash
systemctl status nginx
```

Lệnh này sẽ hiển thị thông tin chi tiết về trạng thái của dịch vụ `nginx`, bao gồm thông tin về việc nó đang chạy hay không, thời gian khởi động và bất kỳ thông báo lỗi nào.

### Ví dụ 2: Khởi động và bật tự động khởi động dịch vụ
Để khởi động dịch vụ `apache2` và bật tự động khởi động khi hệ thống khởi động, bạn có thể sử dụng các lệnh sau:

```bash
systemctl start apache2
systemctl enable apache2
```

Lệnh đầu tiên sẽ khởi động dịch vụ `apache2`, trong khi lệnh thứ hai sẽ đảm bảo rằng dịch vụ này sẽ tự động khởi động khi hệ thống khởi động lại.

## Mẹo
- Luôn kiểm tra trạng thái của dịch vụ sau khi thực hiện các hành động khởi động hoặc dừng để đảm bảo rằng dịch vụ hoạt động như mong đợi.
- Sử dụng `systemctl list-units` để xem tất cả các dịch vụ và trạng thái của chúng, giúp bạn dễ dàng quản lý hơn.
- Khi làm việc với các dịch vụ quan trọng, hãy đảm bảo rằng bạn có quyền truy cập root hoặc sử dụng `sudo` để thực hiện các lệnh `systemctl`.