# [Linux] Bash last lệnh: Hiển thị lịch sử đăng nhập của người dùng

## Tổng quan
Lệnh `last` trong Bash được sử dụng để hiển thị lịch sử đăng nhập của người dùng trên hệ thống. Nó cho phép bạn xem thông tin về các phiên đăng nhập, bao gồm tên người dùng, thời gian đăng nhập, và thời gian đăng xuất.

## Cú pháp
Cú pháp cơ bản của lệnh `last` như sau:

```bash
last [options] [arguments]
```

## Các tùy chọn phổ biến
- `-a`: Hiển thị địa chỉ IP hoặc tên máy của người dùng.
- `-n [số]`: Giới hạn số lượng bản ghi hiển thị.
- `-R`: Không hiển thị tên máy.
- `-x`: Hiển thị thông tin về các phiên đăng nhập và đăng xuất.

## Ví dụ thường gặp
Dưới đây là một số ví dụ về cách sử dụng lệnh `last`:

1. **Hiển thị tất cả lịch sử đăng nhập:**
   ```bash
   last
   ```

2. **Hiển thị 5 bản ghi gần nhất:**
   ```bash
   last -n 5
   ```

3. **Hiển thị địa chỉ IP của người dùng:**
   ```bash
   last -a
   ```

4. **Hiển thị thông tin về các phiên đăng nhập và đăng xuất:**
   ```bash
   last -x
   ```

## Mẹo
- Sử dụng tùy chọn `-n` để chỉ định số lượng bản ghi bạn muốn xem, giúp bạn dễ dàng quản lý thông tin.
- Kết hợp với lệnh `grep` để tìm kiếm thông tin về một người dùng cụ thể:
  ```bash
  last | grep username
  ```
- Thường xuyên kiểm tra lịch sử đăng nhập để phát hiện các hoạt động bất thường trên hệ thống của bạn.