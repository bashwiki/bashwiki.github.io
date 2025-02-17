# [Linux] Bash blkid Cách sử dụng: Lấy thông tin về thiết bị lưu trữ

## Tổng quan
Lệnh `blkid` được sử dụng để tìm kiếm và hiển thị thông tin về các thiết bị lưu trữ trong hệ thống, bao gồm UUID, loại hệ thống tập tin và nhãn của các phân vùng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `blkid` như sau:
```
blkid [options] [arguments]
```

## Các tùy chọn phổ biến
- `-o, --output`: Chỉ định định dạng đầu ra (ví dụ: `value`, `full`, `list`).
- `-s, --match-tag`: Chỉ định một thẻ cụ thể để tìm kiếm (ví dụ: `UUID`, `TYPE`).
- `-p, --probe`: Thực hiện kiểm tra để lấy thông tin chi tiết hơn về thiết bị.
- `-c, --cache`: Sử dụng bộ nhớ cache để tăng tốc độ truy xuất thông tin.

## Ví dụ phổ biến
1. Hiển thị thông tin về tất cả các thiết bị lưu trữ:
   ```bash
   blkid
   ```

2. Hiển thị thông tin chỉ cho một thiết bị cụ thể (ví dụ: `/dev/sda1`):
   ```bash
   blkid /dev/sda1
   ```

3. Lấy UUID của tất cả các phân vùng:
   ```bash
   blkid -s UUID
   ```

4. Xuất thông tin dưới dạng giá trị:
   ```bash
   blkid -o value -s UUID /dev/sda1
   ```

## Mẹo
- Sử dụng tùy chọn `-c` để tăng tốc độ truy xuất thông tin nếu bạn thường xuyên cần kiểm tra các thiết bị lưu trữ.
- Kiểm tra định dạng đầu ra với tùy chọn `-o` để dễ dàng tích hợp vào các tập lệnh tự động.
- Đảm bảo rằng bạn có quyền truy cập cần thiết để sử dụng lệnh `blkid`, vì một số thông tin có thể yêu cầu quyền root.