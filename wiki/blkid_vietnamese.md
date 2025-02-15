# [리눅스] Bash blkid 사용법

## Tổng quan
Lệnh `blkid` trong Bash được sử dụng để xác định và hiển thị thông tin về các thiết bị lưu trữ trên hệ thống. Nó cung cấp thông tin chi tiết về các phân vùng, bao gồm UUID (Universally Unique Identifier), loại hệ thống tệp, và nhãn của phân vùng. Lệnh này rất hữu ích cho các kỹ sư và nhà phát triển khi cần quản lý và cấu hình các thiết bị lưu trữ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `blkid` như sau:

```bash
blkid [tùy chọn] [tên thiết bị]
```

### Các tùy chọn phổ biến:
- `-o` hoặc `--output`: Chỉ định định dạng đầu ra (ví dụ: `value`, `full`, `udev`).
- `-s` hoặc `--match-tag`: Chỉ định một nhãn cụ thể để hiển thị.
- `-p` hoặc `--probe`: Thực hiện kiểm tra để xác định thông tin của thiết bị.
- `-c` hoặc `--cache`: Sử dụng hoặc không sử dụng bộ nhớ cache.

## Ví dụ
### Ví dụ 1: Hiển thị thông tin về tất cả các thiết bị lưu trữ
```bash
blkid
```
Lệnh này sẽ hiển thị danh sách tất cả các thiết bị lưu trữ trên hệ thống cùng với thông tin chi tiết như UUID và loại hệ thống tệp.

### Ví dụ 2: Hiển thị thông tin chỉ cho một thiết bị cụ thể
```bash
blkid /dev/sda1
```
Lệnh này sẽ chỉ hiển thị thông tin của phân vùng `/dev/sda1`, bao gồm UUID và loại hệ thống tệp.

## Mẹo
- Sử dụng lệnh `blkid` với quyền `sudo` nếu bạn không thấy thông tin đầy đủ về các thiết bị lưu trữ, vì một số thông tin có thể yêu cầu quyền truy cập cao hơn.
- Bạn có thể kết hợp lệnh `blkid` với các lệnh khác như `grep` để lọc thông tin theo nhu cầu, ví dụ: `blkid | grep ext4` để tìm các phân vùng có hệ thống tệp ext4.
- Để tự động hóa việc kiểm tra và quản lý các thiết bị lưu trữ, hãy xem xét việc sử dụng lệnh `blkid` trong các script Bash.