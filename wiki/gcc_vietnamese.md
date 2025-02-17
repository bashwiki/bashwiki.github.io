# [Linux] Bash gcc Cách sử dụng: Biên dịch mã nguồn C

## Tổng quan
Lệnh `gcc` (GNU Compiler Collection) là một trình biên dịch mã nguồn C, C++, và nhiều ngôn ngữ lập trình khác. Nó cho phép người dùng biên dịch mã nguồn thành tệp thực thi, giúp chạy các chương trình viết bằng ngôn ngữ C.

## Cách sử dụng
Cú pháp cơ bản của lệnh `gcc` như sau:
```bash
gcc [options] [arguments]
```

## Các tùy chọn phổ biến
- `-o <file>`: Chỉ định tên tệp đầu ra cho chương trình biên dịch.
- `-Wall`: Bật tất cả các cảnh báo.
- `-g`: Tạo thông tin gỡ lỗi trong tệp thực thi.
- `-O`: Tối ưu hóa mã nguồn (có thể sử dụng `-O1`, `-O2`, hoặc `-O3`).
- `-I<directory>`: Thêm thư mục vào danh sách tìm kiếm tệp tiêu đề.

## Ví dụ phổ biến
1. Biên dịch một tệp mã nguồn đơn giản:
   ```bash
   gcc hello.c -o hello
   ```

2. Biên dịch với cảnh báo:
   ```bash
   gcc -Wall hello.c -o hello
   ```

3. Biên dịch với thông tin gỡ lỗi:
   ```bash
   gcc -g hello.c -o hello
   ```

4. Biên dịch với tối ưu hóa:
   ```bash
   gcc -O2 hello.c -o hello
   ```

5. Biên dịch nhiều tệp:
   ```bash
   gcc file1.c file2.c -o myprogram
   ```

## Mẹo
- Luôn sử dụng tùy chọn `-Wall` để phát hiện lỗi tiềm ẩn trong mã nguồn.
- Sử dụng tùy chọn `-g` khi phát triển để dễ dàng gỡ lỗi chương trình.
- Đặt tên tệp đầu ra bằng tùy chọn `-o` để dễ dàng quản lý các tệp thực thi.
- Thường xuyên kiểm tra tài liệu của gcc để nắm bắt các tùy chọn mới và tính năng cải tiến.