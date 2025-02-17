# [Linux] Bash times: [đếm thời gian thực thi lệnh]

## Overview
Lệnh `times` trong Bash được sử dụng để hiển thị thời gian thực thi của các lệnh trong shell. Nó cung cấp thông tin về thời gian CPU đã được sử dụng cho các lệnh trong phiên làm việc hiện tại, bao gồm thời gian người dùng và thời gian hệ thống.

## Usage
Cú pháp cơ bản của lệnh `times` như sau:

```bash
times [options]
```

## Common Options
Lệnh `times` không có nhiều tùy chọn, nhưng dưới đây là một số thông tin hữu ích:

- Không có tùy chọn: Khi bạn chỉ chạy `times`, nó sẽ hiển thị thời gian CPU đã sử dụng cho phiên làm việc hiện tại.

## Common Examples

### Ví dụ 1: Hiển thị thời gian thực thi
Chỉ cần gõ lệnh `times` để xem thời gian CPU đã sử dụng:

```bash
times
```

### Ví dụ 2: Sử dụng trong một phiên làm việc
Bạn có thể chạy một số lệnh và sau đó sử dụng `times` để xem tổng thời gian CPU đã sử dụng cho các lệnh đó. Ví dụ:

```bash
sleep 2
ls
echo "Hello, World!"
times
```

Khi bạn chạy lệnh trên, `times` sẽ hiển thị thời gian CPU đã sử dụng cho các lệnh `sleep`, `ls`, và `echo`.

## Tips
- Sử dụng lệnh `times` sau khi thực hiện một loạt các lệnh để có cái nhìn tổng quan về hiệu suất của chúng.
- Lưu ý rằng `times` chỉ hiển thị thời gian cho phiên làm việc hiện tại, vì vậy nếu bạn mở một shell mới, bạn sẽ cần chạy lại các lệnh để có kết quả chính xác.