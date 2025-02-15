# [리눅스] Bash last 사용법

## Tổng quan
Lệnh `last` trong Bash được sử dụng để hiển thị danh sách các lần đăng nhập gần đây của người dùng trên hệ thống. Nó đọc thông tin từ tệp `/var/log/wtmp`, nơi lưu trữ các phiên đăng nhập và đăng xuất của người dùng. Lệnh này rất hữu ích cho việc theo dõi hoạt động của người dùng và phân tích các sự cố liên quan đến bảo mật.

## Cách sử dụng
Cú pháp cơ bản của lệnh `last` như sau:

```
last [tùy chọn] [tên người dùng]
```

### Các tùy chọn phổ biến:
- `-n [số]`: Hiển thị số lượng bản ghi đăng nhập gần đây. Ví dụ: `last -n 5` sẽ hiển thị 5 lần đăng nhập gần đây nhất.
- `-a`: Hiển thị địa chỉ IP hoặc tên máy chủ của người dùng khi họ đăng nhập từ xa.
- `-R`: Không hiển thị tên máy chủ.
- `-x`: Hiển thị thông tin về các phiên làm việc (session) và các lần khởi động lại hệ thống.

## Ví dụ
### Ví dụ 1: Hiển thị tất cả các lần đăng nhập
Để xem tất cả các lần đăng nhập gần đây, bạn chỉ cần gõ lệnh:

```bash
last
```

### Ví dụ 2: Hiển thị 3 lần đăng nhập gần đây nhất
Nếu bạn chỉ muốn xem 3 lần đăng nhập gần đây nhất, bạn có thể sử dụng tùy chọn `-n`:

```bash
last -n 3
```

## Mẹo
- Để theo dõi hoạt động của một người dùng cụ thể, bạn có thể chỉ định tên người dùng sau lệnh `last`. Ví dụ: `last username` sẽ hiển thị tất cả các lần đăng nhập của người dùng đó.
- Hãy thường xuyên kiểm tra các bản ghi đăng nhập để phát hiện các hoạt động đáng ngờ hoặc không mong muốn trên hệ thống của bạn.
- Kết hợp lệnh `last` với các lệnh khác như `grep` để lọc thông tin theo yêu cầu cụ thể của bạn. Ví dụ: `last | grep username` sẽ chỉ hiển thị các lần đăng nhập của người dùng cụ thể.