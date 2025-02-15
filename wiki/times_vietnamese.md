# [리눅스] Bash times 사용법

## Tổng quan
Lệnh `times` trong Bash được sử dụng để hiển thị thời gian CPU mà shell hiện tại đã sử dụng cho các lệnh con. Nó cung cấp thông tin về thời gian thực hiện của các lệnh, bao gồm thời gian người dùng (user time) và thời gian hệ thống (system time). Mục đích chính của lệnh này là giúp người dùng theo dõi hiệu suất của các lệnh đã thực thi trong phiên làm việc hiện tại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `times` rất đơn giản:

```bash
times
```

Không có tùy chọn nào đi kèm với lệnh này, vì vậy bạn chỉ cần gõ `times` và nhấn Enter để nhận thông tin về thời gian CPU đã sử dụng.

## Ví dụ
### Ví dụ 1: Hiển thị thời gian CPU
Để sử dụng lệnh `times`, bạn chỉ cần gõ lệnh sau trong terminal:

```bash
times
```

Kết quả sẽ hiển thị thời gian CPU đã sử dụng cho các lệnh đã thực thi trong phiên làm việc hiện tại, ví dụ:

```
user     0m0.123s
system   0m0.045s
```

### Ví dụ 2: Sử dụng với một số lệnh khác
Bạn có thể chạy một số lệnh khác trước khi gọi `times` để xem thời gian CPU đã sử dụng cho các lệnh đó. Ví dụ:

```bash
sleep 1
ls -l
times
```

Khi bạn chạy lệnh `times` sau khi thực hiện các lệnh trên, bạn sẽ thấy thời gian CPU đã sử dụng cho các lệnh `sleep` và `ls`.

## Mẹo
- Lệnh `times` rất hữu ích để theo dõi hiệu suất của các lệnh trong phiên làm việc, đặc biệt khi bạn đang làm việc với các lệnh tốn nhiều thời gian.
- Bạn có thể sử dụng `times` sau khi chạy một loạt lệnh để có cái nhìn tổng quan về thời gian mà các lệnh đó đã tiêu tốn, giúp bạn tối ưu hóa quy trình làm việc của mình.
- Lưu ý rằng `times` chỉ hiển thị thời gian cho các lệnh đã chạy trong phiên hiện tại, vì vậy nếu bạn mở một terminal mới, thông tin sẽ không được hiển thị.