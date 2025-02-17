# [Linux] Bash mkfs Cách sử dụng: Tạo hệ thống tệp

## Tổng quan
Lệnh `mkfs` được sử dụng để tạo một hệ thống tệp trên một phân vùng hoặc thiết bị lưu trữ. Nó định dạng thiết bị để có thể lưu trữ dữ liệu theo một cấu trúc nhất định, cho phép hệ điều hành quản lý và truy cập dữ liệu hiệu quả hơn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mkfs` như sau:
```bash
mkfs [options] [arguments]
```

## Các tùy chọn phổ biến
- `-t` hoặc `--type`: Chỉ định loại hệ thống tệp (ví dụ: ext4, xfs).
- `-L` hoặc `--label`: Gán nhãn cho hệ thống tệp.
- `-n` hoặc `--no-mount`: Không tự động gắn kết sau khi tạo.
- `-V` hoặc `--verbose`: Hiển thị thông tin chi tiết trong quá trình thực hiện.

## Ví dụ thường gặp
1. Tạo hệ thống tệp ext4 trên phân vùng `/dev/sdb1`:
   ```bash
   mkfs -t ext4 /dev/sdb1
   ```

2. Tạo hệ thống tệp xfs trên phân vùng `/dev/sdc1` với nhãn "Data":
   ```bash
   mkfs -t xfs -L Data /dev/sdc1
   ```

3. Tạo hệ thống tệp vfat trên thiết bị USB `/dev/sdd1`:
   ```bash
   mkfs.vfat /dev/sdd1
   ```

4. Tạo hệ thống tệp ext3 trên phân vùng `/dev/sde1` mà không tự động gắn kết:
   ```bash
   mkfs -t ext3 -n /dev/sde1
   ```

## Mẹo
- Trước khi sử dụng `mkfs`, hãy chắc chắn rằng bạn đã sao lưu dữ liệu quan trọng, vì lệnh này sẽ xóa tất cả dữ liệu trên phân vùng.
- Kiểm tra phân vùng trước khi định dạng bằng lệnh `lsblk` để xác định đúng thiết bị.
- Sử dụng tùy chọn `-V` để theo dõi quá trình tạo hệ thống tệp, điều này có thể hữu ích trong trường hợp có lỗi xảy ra.