# [리눅스] Bash g++ 사용법

## Tổng quan
`g++` là một trình biên dịch C++ thuộc bộ công cụ GNU Compiler Collection (GCC). Nó được sử dụng để biên dịch mã nguồn C++ thành mã máy, cho phép người lập trình phát triển và chạy các ứng dụng C++. `g++` hỗ trợ nhiều tính năng của ngôn ngữ C++ hiện đại và cung cấp các tùy chọn để tối ưu hóa mã, kiểm tra lỗi và quản lý các thư viện.

## Cách sử dụng
Cú pháp cơ bản của lệnh `g++` như sau:

```bash
g++ [tùy chọn] [tệp nguồn] -o [tên tệp thực thi]
```

### Các tùy chọn phổ biến:
- `-o [tên tệp thực thi]`: Xác định tên tệp đầu ra cho chương trình biên dịch.
- `-Wall`: Kích hoạt tất cả các cảnh báo, giúp phát hiện lỗi tiềm ẩn trong mã nguồn.
- `-g`: Thêm thông tin gỡ lỗi vào tệp thực thi, hữu ích cho việc sử dụng gdb (GNU Debugger).
- `-O2`: Kích hoạt tối ưu hóa mức độ 2, giúp cải thiện hiệu suất của chương trình.

## Ví dụ
### Ví dụ 1: Biên dịch một tệp nguồn đơn giản
Giả sử bạn có một tệp nguồn C++ tên là `hello.cpp` với nội dung sau:

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello, World!" << endl;
    return 0;
}
```

Bạn có thể biên dịch tệp này bằng lệnh sau:

```bash
g++ hello.cpp -o hello
```

Sau khi biên dịch, bạn có thể chạy chương trình bằng lệnh:

```bash
./hello
```

### Ví dụ 2: Biên dịch với cảnh báo và thông tin gỡ lỗi
Nếu bạn muốn biên dịch tệp `hello.cpp` với các cảnh báo và thông tin gỡ lỗi, bạn có thể sử dụng lệnh sau:

```bash
g++ -Wall -g hello.cpp -o hello_debug
```

Điều này sẽ tạo ra tệp thực thi `hello_debug` với các cảnh báo được kích hoạt.

## Mẹo
- Luôn sử dụng tùy chọn `-Wall` để phát hiện các vấn đề trong mã nguồn của bạn.
- Nếu bạn làm việc với nhiều tệp nguồn, hãy xem xét việc sử dụng Makefile để quản lý quá trình biên dịch một cách hiệu quả hơn.
- Thường xuyên kiểm tra tài liệu chính thức của GCC để cập nhật các tính năng và tùy chọn mới nhất của `g++`.