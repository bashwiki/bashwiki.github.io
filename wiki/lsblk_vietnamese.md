# [Linux] Bash lsblk Cách sử dụng: Hiển thị thông tin về các thiết bị lưu trữ

## Tổng quan
Lệnh `lsblk` được sử dụng để hiển thị thông tin về các thiết bị lưu trữ trên hệ thống Linux, bao gồm các phân vùng và điểm gắn kết. Nó giúp người dùng dễ dàng nhận biết cấu trúc và trạng thái của các thiết bị lưu trữ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `lsblk` như sau:
```
lsblk [options] [arguments]
```

## Các tùy chọn phổ biến
- `-a`, `--all`: Hiển thị tất cả các thiết bị, bao gồm cả những thiết bị không có điểm gắn kết.
- `-f`, `--fs`: Hiển thị thông tin về hệ thống tệp của các thiết bị.
- `-l`, `--list`: Hiển thị thông tin theo dạng danh sách thay vì dạng cây.
- `-o`, `--output`: Chỉ định các cột thông tin cần hiển thị.
- `-p`, `--paths`: Hiển thị đường dẫn đầy đủ của thiết bị.

## Các ví dụ phổ biến
1. Hiển thị danh sách các thiết bị lưu trữ:
   ```bash
   lsblk
   ```

2. Hiển thị thông tin chi tiết về hệ thống tệp:
   ```bash
   lsblk -f
   ```

3. Hiển thị thông tin theo dạng danh sách:
   ```bash
   lsblk -l
   ```

4. Chỉ định các cột thông tin cần hiển thị:
   ```bash
   lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
   ```

5. Hiển thị tất cả các thiết bị, bao gồm cả những thiết bị không có điểm gắn kết:
   ```bash
   lsblk -a
   ```

## Mẹo
- Sử dụng tùy chọn `-f` để nhanh chóng kiểm tra hệ thống tệp của các phân vùng, điều này rất hữu ích khi bạn cần xác định loại hệ thống tệp.
- Kết hợp `lsblk` với `grep` để tìm kiếm thiết bị cụ thể, ví dụ:
  ```bash
  lsblk | grep sda
  ```
- Thường xuyên kiểm tra cấu trúc thiết bị lưu trữ của bạn để đảm bảo không có phân vùng nào bị thiếu hoặc không được gắn kết đúng cách.