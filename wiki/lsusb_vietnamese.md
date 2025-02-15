# [리눅스] Bash lsusb 사용법

## Tổng quan
Lệnh `lsusb` là một công cụ dòng lệnh trong hệ điều hành Linux, được sử dụng để hiển thị thông tin về các thiết bị USB được kết nối với hệ thống. Nó cung cấp một cái nhìn tổng quan về các thiết bị USB, bao gồm thông tin như ID nhà sản xuất, ID thiết bị và tên thiết bị. Lệnh này rất hữu ích cho các kỹ sư và nhà phát triển khi cần kiểm tra hoặc gỡ lỗi các thiết bị USB.

## Cách sử dụng
Cú pháp cơ bản của lệnh `lsusb` như sau:

```bash
lsusb [tùy chọn]
```

### Các tùy chọn phổ biến:
- `-v`: Hiển thị thông tin chi tiết về các thiết bị USB.
- `-t`: Hiển thị cấu trúc cây của các thiết bị USB.
- `-s [bus]:[device]`: Chỉ định bus và thiết bị cụ thể để hiển thị thông tin.
- `-D [tên thiết bị]`: Hiển thị thông tin chi tiết cho một thiết bị cụ thể được xác định bởi tên.

## Ví dụ
### Ví dụ 1: Hiển thị danh sách các thiết bị USB
Để hiển thị danh sách tất cả các thiết bị USB đang kết nối, bạn chỉ cần gõ lệnh sau:

```bash
lsusb
```

### Ví dụ 2: Hiển thị thông tin chi tiết về một thiết bị USB
Nếu bạn muốn xem thông tin chi tiết về một thiết bị USB cụ thể, bạn có thể sử dụng tùy chọn `-v`. Ví dụ:

```bash
lsusb -v -s 001:002
```

Trong đó `001:002` là bus và ID thiết bị mà bạn muốn kiểm tra.

## Mẹo
- Sử dụng lệnh `lsusb` thường xuyên để theo dõi các thiết bị USB được kết nối và đảm bảo rằng chúng hoạt động đúng cách.
- Kết hợp `lsusb` với các lệnh khác như `grep` để lọc thông tin bạn cần. Ví dụ, bạn có thể tìm kiếm một thiết bị cụ thể bằng cách sử dụng:

```bash
lsusb | grep "Tên thiết bị"
```

- Nếu bạn cần thông tin chi tiết về các thiết bị USB, hãy sử dụng tùy chọn `-v`, nhưng lưu ý rằng thông tin có thể rất dài và phức tạp.