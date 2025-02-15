# [리눅스] Bash fdisk 사용법

## Tổng quan
`fdisk` là một công cụ dòng lệnh trong hệ điều hành Linux được sử dụng để quản lý các phân vùng trên ổ đĩa cứng. Nó cho phép người dùng tạo, xóa, thay đổi kích thước và quản lý các phân vùng, giúp tối ưu hóa việc sử dụng không gian lưu trữ trên hệ thống. `fdisk` thường được sử dụng cho các ổ đĩa có định dạng MBR (Master Boot Record).

## Cách sử dụng
Cú pháp cơ bản của lệnh `fdisk` như sau:

```
fdisk [tùy chọn] [thiết bị]
```

Trong đó:
- `[tùy chọn]`: Các tùy chọn có thể được sử dụng để điều chỉnh hành vi của lệnh.
- `[thiết bị]`: Đường dẫn đến thiết bị ổ đĩa mà bạn muốn quản lý, ví dụ: `/dev/sda`.

### Một số tùy chọn phổ biến:
- `-l`: Liệt kê tất cả các phân vùng trên các ổ đĩa.
- `-u`: Sử dụng đơn vị là sector thay vì cylinder.
- `-v`: Hiển thị thông tin phiên bản của `fdisk`.

## Ví dụ
### Ví dụ 1: Liệt kê các phân vùng
Để xem danh sách các phân vùng trên ổ đĩa `/dev/sda`, bạn có thể sử dụng lệnh sau:

```bash
sudo fdisk -l /dev/sda
```

### Ví dụ 2: Tạo một phân vùng mới
Để tạo một phân vùng mới trên ổ đĩa `/dev/sda`, bạn có thể chạy lệnh sau:

```bash
sudo fdisk /dev/sda
```
Sau đó, bạn sẽ vào chế độ tương tác của `fdisk`, nơi bạn có thể nhập các lệnh như `n` để tạo phân vùng mới, `d` để xóa phân vùng, và `w` để lưu thay đổi.

## Mẹo
- **Sao lưu dữ liệu**: Trước khi thực hiện bất kỳ thay đổi nào trên phân vùng, hãy chắc chắn sao lưu dữ liệu quan trọng để tránh mất mát dữ liệu.
- **Kiểm tra phân vùng**: Sau khi thay đổi phân vùng, hãy sử dụng lệnh `lsblk` để kiểm tra lại cấu trúc phân vùng và đảm bảo mọi thứ hoạt động như mong đợi.
- **Sử dụng với cẩn thận**: `fdisk` là một công cụ mạnh mẽ và có thể gây ra thiệt hại nghiêm trọng nếu không sử dụng đúng cách. Hãy chắc chắn hiểu rõ các lệnh trước khi thực hiện.