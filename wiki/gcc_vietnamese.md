# [리눅스] Bash gcc 사용법

## Tổng quan
`gcc` (GNU Compiler Collection) là một trình biên dịch mạnh mẽ được sử dụng để biên dịch mã nguồn viết bằng ngôn ngữ lập trình C, C++, và nhiều ngôn ngữ khác. Mục đích chính của `gcc` là chuyển đổi mã nguồn thành mã máy có thể thực thi trên hệ thống, giúp các lập trình viên phát triển và kiểm tra ứng dụng của họ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `gcc` như sau:

```bash
gcc [tùy chọn] [tệp nguồn] -o [tên tệp đầu ra]
```

### Các tùy chọn phổ biến:
- `-o [tên tệp đầu ra]`: Chỉ định tên tệp đầu ra cho chương trình biên dịch. Nếu không có tùy chọn này, tệp đầu ra sẽ có tên mặc định là `a.out`.
- `-Wall`: Kích hoạt tất cả các cảnh báo. Đây là một tùy chọn tốt để phát hiện lỗi tiềm ẩn trong mã nguồn.
- `-g`: Thêm thông tin gỡ lỗi vào tệp đầu ra, hữu ích cho việc sử dụng các công cụ gỡ lỗi như `gdb`.
- `-O`: Tối ưu hóa mã nguồn. Có thể sử dụng `-O1`, `-O2`, hoặc `-O3` để chỉ định mức độ tối ưu hóa.

## Ví dụ
### Ví dụ 1: Biên dịch một tệp nguồn đơn giản
Giả sử bạn có một tệp nguồn C tên là `hello.c` với nội dung sau:

```c
#include <stdio.h>

int main() {
    printf("Hello, World!\n");
    return 0;
}
```

Bạn có thể biên dịch tệp này bằng lệnh sau:

```bash
gcc hello.c -o hello
```

Sau khi biên dịch, bạn có thể chạy chương trình bằng lệnh:

```bash
./hello
```

### Ví dụ 2: Biên dịch với cảnh báo và thông tin gỡ lỗi
Nếu bạn muốn biên dịch tệp `hello.c` với cảnh báo và thông tin gỡ lỗi, bạn có thể sử dụng lệnh sau:

```bash
gcc -Wall -g hello.c -o hello_debug
```

Điều này sẽ tạo ra tệp thực thi `hello_debug` với các cảnh báo và thông tin gỡ lỗi.

## Mẹo
- Luôn sử dụng tùy chọn `-Wall` để nhận được các cảnh báo hữu ích trong quá trình biên dịch, giúp bạn phát hiện lỗi sớm hơn.
- Nếu bạn đang làm việc với nhiều tệp nguồn, hãy xem xét việc sử dụng Makefile để quản lý quá trình biên dịch một cách hiệu quả.
- Thường xuyên kiểm tra mã nguồn của bạn bằng cách biên dịch với tùy chọn `-g` để dễ dàng gỡ lỗi khi cần thiết.
- Đọc tài liệu chính thức của `gcc` bằng cách chạy `man gcc` trong terminal để tìm hiểu thêm về các tùy chọn và tính năng nâng cao.