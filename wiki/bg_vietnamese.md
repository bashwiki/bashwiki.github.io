# [리눅스] Bash bg 사용법

## Tổng Quan
Lệnh `bg` trong Bash được sử dụng để tiếp tục thực thi một tiến trình đang bị tạm dừng (suspended process) trong chế độ nền (background). Khi một tiến trình được đưa vào chế độ nền, nó sẽ không chiếm dụng terminal, cho phép người dùng tiếp tục làm việc với các lệnh khác trong cùng một phiên làm việc.

## Cách Sử Dụng
Cú pháp cơ bản của lệnh `bg` như sau:

```bash
bg [job_spec]
```

- `job_spec`: Đây là tham số tùy chọn, cho phép bạn chỉ định một tiến trình cụ thể mà bạn muốn tiếp tục trong chế độ nền. Nếu không chỉ định, lệnh sẽ áp dụng cho tiến trình bị tạm dừng gần nhất.

## Ví Dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `bg`.

### Ví dụ 1: Tiếp tục một tiến trình tạm dừng
Giả sử bạn đã chạy một lệnh nặng và tạm dừng nó bằng cách nhấn `Ctrl + Z`. Bạn có thể tiếp tục nó trong chế độ nền bằng cách sử dụng lệnh `bg`:

```bash
$ sleep 1000
^Z
[1]+  Stopped                 sleep 1000
$ bg
[1]+ sleep 1000 &
```

### Ví dụ 2: Tiếp tục một tiến trình cụ thể
Nếu bạn có nhiều tiến trình tạm dừng và muốn tiếp tục một tiến trình cụ thể, bạn có thể chỉ định nó bằng cách sử dụng số công việc:

```bash
$ sleep 1000
^Z
[1]+  Stopped                 sleep 1000
$ sleep 500
^Z
[2]+  Stopped                 sleep 500
$ bg %1
[1]+ sleep 1000 &
```

Trong ví dụ này, tiến trình `sleep 1000` được tiếp tục trong chế độ nền trong khi `sleep 500` vẫn bị tạm dừng.

## Mẹo
- Sử dụng lệnh `jobs` để xem danh sách các tiến trình đang chạy và tạm dừng trong phiên làm việc hiện tại. Điều này giúp bạn dễ dàng xác định số công việc mà bạn muốn tiếp tục.
- Hãy nhớ rằng khi một tiến trình chạy trong chế độ nền, bạn có thể không thấy đầu ra của nó trên terminal. Nếu bạn cần theo dõi đầu ra, hãy sử dụng lệnh `nohup` hoặc chuyển hướng đầu ra đến một tệp.
- Để dừng một tiến trình đang chạy trong nền, bạn có thể sử dụng lệnh `kill` với ID tiến trình hoặc số công việc.

Lệnh `bg` là một công cụ hữu ích cho phép bạn quản lý các tiến trình trong Bash một cách hiệu quả, giúp tối ưu hóa quy trình làm việc của bạn.