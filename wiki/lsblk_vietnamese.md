# [리눅스] Bash lsblk 사용법

## Tổng quan
Lệnh `lsblk` là một công cụ hữu ích trong Bash được sử dụng để liệt kê tất cả các thiết bị lưu trữ và phân vùng trên hệ thống Linux. Lệnh này cung cấp thông tin chi tiết về cấu trúc phân vùng, kích thước, loại hệ thống tập tin và trạng thái của các thiết bị lưu trữ, giúp người dùng dễ dàng quản lý và theo dõi các thiết bị lưu trữ của mình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `lsblk` như sau:

```bash
lsblk [OPTIONS]
```

Một số tùy chọn phổ biến của lệnh `lsblk` bao gồm:

- `-a`, `--all`: Hiển thị tất cả các thiết bị, bao gồm cả những thiết bị không có phân vùng.
- `-f`, `--fs`: Hiển thị thông tin về hệ thống tập tin của các thiết bị.
- `-l`, `--list`: Hiển thị thông tin theo dạng danh sách thay vì dạng cây.
- `-o`, `--output`: Chỉ định các cột thông tin cụ thể để hiển thị.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `lsblk`.

1. Liệt kê tất cả các thiết bị lưu trữ và phân vùng:

```bash
lsblk
```

Kết quả sẽ hiển thị danh sách các thiết bị lưu trữ, cùng với thông tin về kích thước và kiểu phân vùng.

2. Hiển thị thông tin về hệ thống tập tin của các thiết bị:

```bash
lsblk -f
```

Lệnh này sẽ cung cấp thêm thông tin về hệ thống tập tin, bao gồm tên hệ thống tập tin, nhãn và UUID.

## Mẹo
- Sử dụng tùy chọn `-o` để chỉ định các cột thông tin mà bạn muốn hiển thị, giúp bạn tùy chỉnh đầu ra theo nhu cầu cụ thể của mình.
- Kết hợp lệnh `lsblk` với các lệnh khác như `grep` để lọc thông tin theo yêu cầu, ví dụ:

```bash
lsblk | grep sda
```

Điều này sẽ giúp bạn tìm kiếm thông tin về thiết bị lưu trữ cụ thể một cách nhanh chóng.