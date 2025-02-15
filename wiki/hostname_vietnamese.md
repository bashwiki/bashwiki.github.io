# [리눅스] Bash hostname 사용법

## Tổng quan
Lệnh `hostname` trong Bash được sử dụng để hiển thị hoặc thiết lập tên máy chủ của hệ thống. Tên máy chủ là một phần quan trọng trong việc xác định một thiết bị trong mạng, giúp người dùng và các ứng dụng nhận diện và giao tiếp với nhau. Lệnh này rất hữu ích cho các kỹ sư và nhà phát triển khi cần kiểm tra hoặc thay đổi tên máy chủ của hệ thống.

## Cách sử dụng
Cú pháp cơ bản của lệnh `hostname` như sau:

```bash
hostname [OPTION] [NAME]
```

### Các tùy chọn phổ biến:
- `-f`, `--fqdn`: Hiển thị tên miền đầy đủ (Fully Qualified Domain Name) của máy chủ.
- `-i`, `--ip-address`: Hiển thị địa chỉ IP của máy chủ.
- `-s`, `--short`: Hiển thị tên ngắn của máy chủ.
- `--help`: Hiển thị thông tin trợ giúp về lệnh.
- `--version`: Hiển thị phiên bản của lệnh.

## Ví dụ
### Ví dụ 1: Hiển thị tên máy chủ hiện tại
Để hiển thị tên máy chủ hiện tại, bạn có thể sử dụng lệnh đơn giản sau:

```bash
hostname
```

Kết quả sẽ là tên máy chủ của hệ thống bạn đang sử dụng.

### Ví dụ 2: Thiết lập tên máy chủ mới
Để thay đổi tên máy chủ, bạn có thể sử dụng lệnh sau (cần quyền quản trị):

```bash
sudo hostname new-hostname
```

Thay thế `new-hostname` bằng tên máy chủ mà bạn muốn thiết lập.

## Mẹo
- Khi thay đổi tên máy chủ, hãy chắc chắn rằng tên mới không trùng với bất kỳ tên nào khác trong mạng để tránh xung đột.
- Sau khi thay đổi tên máy chủ, bạn nên khởi động lại dịch vụ mạng hoặc khởi động lại hệ thống để đảm bảo rằng các thay đổi có hiệu lực.
- Sử dụng tùy chọn `-f` để kiểm tra tên miền đầy đủ của máy chủ, điều này rất hữu ích khi bạn làm việc trong môi trường mạng phức tạp.