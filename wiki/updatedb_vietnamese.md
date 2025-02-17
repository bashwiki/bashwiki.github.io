# [Linux] Bash updatedb Cách sử dụng: Cập nhật cơ sở dữ liệu tìm kiếm

## Tổng quan
Lệnh `updatedb` được sử dụng để cập nhật cơ sở dữ liệu của hệ thống tìm kiếm tệp tin, thường là cơ sở dữ liệu của `locate`. Lệnh này giúp người dùng nhanh chóng tìm kiếm tệp tin trên hệ thống mà không cần quét toàn bộ hệ thống mỗi lần.

## Cách sử dụng
Cú pháp cơ bản của lệnh `updatedb` như sau:
```
updatedb [options] [arguments]
```

## Các tùy chọn phổ biến
- `--localpaths`: Chỉ định các đường dẫn cục bộ để cập nhật.
- `--netpaths`: Chỉ định các đường dẫn mạng để cập nhật.
- `--prunepaths`: Đường dẫn sẽ bị loại trừ khỏi việc cập nhật.
- `--prunefs`: Hệ thống tệp sẽ bị loại trừ khỏi việc cập nhật.

## Ví dụ thường gặp
1. Cập nhật cơ sở dữ liệu tìm kiếm với các đường dẫn mặc định:
   ```bash
   updatedb
   ```

2. Cập nhật cơ sở dữ liệu chỉ với các đường dẫn cục bộ:
   ```bash
   updatedb --localpaths '/home /usr'
   ```

3. Loại trừ một số đường dẫn khỏi việc cập nhật:
   ```bash
   updatedb --prunepaths '/tmp /var/tmp'
   ```

4. Cập nhật cơ sở dữ liệu và loại trừ một số hệ thống tệp:
   ```bash
   updatedb --prunefs 'nfs tmpfs'
   ```

## Mẹo
- Nên chạy `updatedb` với quyền quản trị để đảm bảo tất cả các tệp tin đều được cập nhật.
- Thiết lập một cron job để tự động cập nhật cơ sở dữ liệu vào thời gian định kỳ, giúp bạn luôn có thông tin mới nhất.
- Kiểm tra thường xuyên các tùy chọn để tối ưu hóa quá trình cập nhật, đặc biệt là khi làm việc với các hệ thống lớn.