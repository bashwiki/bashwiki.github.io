# [Linux] Bash g++ Cách sử dụng: Biên dịch mã nguồn C++

## Tổng quan
Lệnh `g++` là một trình biên dịch cho ngôn ngữ lập trình C++. Nó được sử dụng để biên dịch các tệp mã nguồn C++ thành tệp thực thi, cho phép bạn chạy chương trình trên hệ thống của mình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `g++` như sau:

```bash
g++ [options] [arguments]
```

## Các tùy chọn phổ biến
- `-o <filename>`: Chỉ định tên tệp đầu ra cho chương trình biên dịch.
- `-Wall`: Kích hoạt tất cả các cảnh báo để giúp phát hiện lỗi trong mã nguồn.
- `-g`: Thêm thông tin gỡ lỗi vào tệp biên dịch, hữu ích cho việc gỡ lỗi với gdb.
- `-std=<standard>`: Chỉ định tiêu chuẩn C++ mà bạn muốn sử dụng (ví dụ: `-std=c++11`).

## Ví dụ thường gặp
1. Biên dịch một tệp mã nguồn đơn giản:
   ```bash
   g++ main.cpp
   ```

2. Biên dịch và chỉ định tên tệp đầu ra:
   ```bash
   g++ main.cpp -o my_program
   ```

3. Biên dịch với cảnh báo:
   ```bash
   g++ -Wall main.cpp -o my_program
   ```

4. Biên dịch với thông tin gỡ lỗi:
   ```bash
   g++ -g main.cpp -o my_program
   ```

5. Biên dịch với tiêu chuẩn C++11:
   ```bash
   g++ -std=c++11 main.cpp -o my_program
   ```

## Mẹo
- Luôn sử dụng tùy chọn `-Wall` để phát hiện lỗi tiềm ẩn trong mã nguồn.
- Thêm tùy chọn `-g` khi bạn cần gỡ lỗi chương trình để dễ dàng theo dõi lỗi.
- Đặt tên tệp đầu ra rõ ràng để dễ dàng nhận diện chương trình sau khi biên dịch.
- Nếu bạn làm việc với nhiều tệp mã nguồn, hãy sử dụng `g++ file1.cpp file2.cpp -o my_program` để biên dịch tất cả trong một lệnh.