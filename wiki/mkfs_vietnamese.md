# [리눅스] Bash mkfs 사용법

## Tổng quan
Lệnh `mkfs` (make filesystem) trong Bash được sử dụng để tạo hệ thống tệp trên một phân vùng hoặc thiết bị lưu trữ. Lệnh này thường được sử dụng khi bạn muốn định dạng một ổ đĩa hoặc phân vùng để có thể lưu trữ dữ liệu. `mkfs` hỗ trợ nhiều loại hệ thống tệp khác nhau như ext2, ext3, ext4, xfs, và nhiều loại khác.

## Cú pháp
Cú pháp cơ bản của lệnh `mkfs` như sau:

```bash
mkfs [tùy chọn] [thiết bị]
```

### Tùy chọn phổ biến
- `-t <loại>`: Chỉ định loại hệ thống tệp cần tạo (ví dụ: ext4, xfs).
- `-L <nhãn>`: Gán nhãn cho hệ thống tệp.
- `-n`: Chạy lệnh trong chế độ thử nghiệm, không thực hiện thay đổi nào.
- `-V`: Hiển thị thông tin chi tiết về quá trình tạo hệ thống tệp.

## Ví dụ
### Ví dụ 1: Tạo hệ thống tệp ext4
Để tạo một hệ thống tệp ext4 trên phân vùng `/dev/sdb1`, bạn có thể sử dụng lệnh sau:

```bash
sudo mkfs -t ext4 /dev/sdb1
```

### Ví dụ 2: Tạo hệ thống tệp xfs với nhãn
Để tạo một hệ thống tệp xfs và gán nhãn cho nó là "DataDisk", bạn có thể sử dụng lệnh sau:

```bash
sudo mkfs -t xfs -L DataDisk /dev/sdc1
```

## Mẹo
- Trước khi sử dụng lệnh `mkfs`, hãy chắc chắn rằng bạn đã sao lưu dữ liệu quan trọng, vì lệnh này sẽ xóa tất cả dữ liệu trên phân vùng hoặc thiết bị được chỉ định.
- Sử dụng tùy chọn `-n` để kiểm tra lệnh mà không thực hiện thay đổi thực tế. Điều này giúp bạn đảm bảo rằng bạn đang sử dụng đúng thiết bị và loại hệ thống tệp.
- Kiểm tra tài liệu của hệ thống tệp cụ thể mà bạn muốn tạo để biết thêm thông tin về các tùy chọn và tính năng hỗ trợ.