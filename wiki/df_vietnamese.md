# [리눅스] Bash df 사용법

## Tổng quan
Lệnh `df` (disk free) trong Bash được sử dụng để hiển thị thông tin về dung lượng ổ đĩa và không gian trống trên các hệ thống tệp. Lệnh này giúp người dùng theo dõi tình trạng sử dụng dung lượng ổ đĩa, từ đó có thể quản lý tài nguyên lưu trữ một cách hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `df` như sau:

```bash
df [tùy chọn] [tệp hoặc thư mục]
```

### Các tùy chọn phổ biến:
- `-h`: Hiển thị dung lượng ổ đĩa theo định dạng dễ đọc (human-readable), sử dụng các đơn vị như KB, MB, GB.
- `-T`: Hiển thị loại hệ thống tệp cho mỗi hệ thống tệp được liệt kê.
- `-a`: Hiển thị tất cả các hệ thống tệp, bao gồm cả các hệ thống tệp có dung lượng 0.
- `-i`: Hiển thị thông tin về số lượng inode thay vì dung lượng ổ đĩa.

## Ví dụ
### Ví dụ 1: Kiểm tra dung lượng ổ đĩa
Để kiểm tra dung lượng ổ đĩa và không gian trống trên hệ thống của bạn, bạn có thể sử dụng lệnh sau:

```bash
df -h
```

Kết quả sẽ hiển thị thông tin về tất cả các hệ thống tệp, bao gồm tổng dung lượng, dung lượng đã sử dụng, dung lượng còn trống và điểm gắn kết.

### Ví dụ 2: Kiểm tra loại hệ thống tệp
Nếu bạn muốn xem loại hệ thống tệp cho mỗi ổ đĩa, bạn có thể sử dụng lệnh:

```bash
df -T
```

Lệnh này sẽ cung cấp thông tin về loại hệ thống tệp bên cạnh dung lượng ổ đĩa.

## Mẹo
- Sử dụng tùy chọn `-h` để dễ dàng đọc thông tin về dung lượng ổ đĩa, đặc biệt khi làm việc với các ổ đĩa lớn.
- Kết hợp lệnh `df` với lệnh `grep` để lọc thông tin cho một hệ thống tệp cụ thể. Ví dụ:

```bash
df -h | grep /dev/sda1
```

Điều này sẽ giúp bạn nhanh chóng tìm thấy thông tin về ổ đĩa mà bạn quan tâm.