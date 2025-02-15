# [리눅스] Bash bash 사용법

## Tổng quan
Lệnh `bash` là một trình thông dịch lệnh (shell) phổ biến trong hệ điều hành Unix và Linux. Nó cho phép người dùng thực thi các lệnh, chạy các tập lệnh shell, và tương tác với hệ thống thông qua dòng lệnh. `bash` (Bourne Again SHell) là một phiên bản nâng cao của Bourne Shell (sh), cung cấp nhiều tính năng hơn như lịch sử lệnh, tự động hoàn thành, và khả năng xử lý các tập lệnh phức tạp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `bash` như sau:

```bash
bash [options] [file]
```

### Các tùy chọn phổ biến:
- `-c`: Chạy lệnh được chỉ định trong chuỗi.
- `-i`: Bắt đầu một phiên tương tác.
- `-l`: Khởi động một shell đăng nhập.
- `-s`: Đọc lệnh từ stdin (đầu vào chuẩn).

## Ví dụ
### Ví dụ 1: Chạy một tập lệnh shell
Giả sử bạn có một tập lệnh shell tên là `script.sh`, bạn có thể chạy nó bằng lệnh:

```bash
bash script.sh
```

### Ví dụ 2: Chạy một lệnh trực tiếp
Bạn có thể sử dụng tùy chọn `-c` để chạy một lệnh đơn giản:

```bash
bash -c 'echo "Hello, World!"'
```

Lệnh này sẽ in ra "Hello, World!" trên màn hình.

## Mẹo
- Sử dụng `bash` trong các tập lệnh shell để tận dụng các tính năng nâng cao như kiểm soát luồng và xử lý lỗi.
- Khi viết các tập lệnh, hãy thêm `#!/bin/bash` ở đầu tập lệnh để chỉ định rằng nó nên được thực thi bằng `bash`.
- Tận dụng tính năng tự động hoàn thành của `bash` bằng cách nhấn phím Tab để tiết kiệm thời gian khi nhập lệnh. 

Hy vọng bài viết này giúp bạn hiểu rõ hơn về lệnh `bash` và cách sử dụng nó trong công việc hàng ngày của mình!