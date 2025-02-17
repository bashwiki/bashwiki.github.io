# [Linux] Bash zip cách sử dụng: Nén và lưu trữ tệp

## Tổng quan
Lệnh `zip` được sử dụng để nén các tệp và thư mục thành một tệp zip. Điều này giúp tiết kiệm không gian lưu trữ và dễ dàng chia sẻ nhiều tệp trong một tệp duy nhất.

## Cách sử dụng
Cú pháp cơ bản của lệnh zip như sau:
```bash
zip [tùy chọn] [tên_tệp_zip] [tệp_hoặc_thư_mục]
```

## Tùy chọn phổ biến
- `-r`: Nén thư mục và tất cả các tệp con.
- `-e`: Mã hóa tệp zip bằng mật khẩu.
- `-u`: Cập nhật tệp zip bằng cách thêm hoặc thay thế các tệp mới.
- `-d`: Xóa tệp khỏi tệp zip.

## Ví dụ phổ biến
1. Nén một tệp đơn:
   ```bash
   zip myfile.zip file.txt
   ```

2. Nén nhiều tệp:
   ```bash
   zip myfiles.zip file1.txt file2.txt file3.txt
   ```

3. Nén một thư mục và tất cả các tệp con:
   ```bash
   zip -r myfolder.zip myfolder/
   ```

4. Nén và mã hóa tệp zip:
   ```bash
   zip -e mysecure.zip secret.txt
   ```

5. Cập nhật tệp zip với tệp mới:
   ```bash
   zip -u myfiles.zip newfile.txt
   ```

## Mẹo
- Sử dụng tùy chọn `-r` khi bạn cần nén toàn bộ thư mục để đảm bảo tất cả các tệp con được bao gồm.
- Đặt mật khẩu cho tệp zip nếu bạn muốn bảo vệ thông tin nhạy cảm.
- Kiểm tra nội dung của tệp zip bằng lệnh `unzip -l [tên_tệp_zip]` trước khi giải nén để xem các tệp bên trong.