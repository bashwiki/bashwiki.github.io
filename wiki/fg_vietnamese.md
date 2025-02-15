# [리눅스] Bash fg 사용법

## Tổng quan
Lệnh `fg` trong Bash được sử dụng để đưa một tiến trình đang chạy ở chế độ nền (background) trở lại chế độ nền (foreground). Điều này cho phép người dùng tương tác với tiến trình đó, ví dụ như nhập dữ liệu hoặc nhận đầu ra trực tiếp từ tiến trình. Lệnh `fg` rất hữu ích khi bạn cần quay lại làm việc với một tiến trình mà bạn đã tạm dừng hoặc đã chạy ở chế độ nền.

## Cú pháp
Cú pháp cơ bản của lệnh `fg` như sau:
```
fg [job_spec]
```
Trong đó:
- `job_spec` là tham số tùy chọn, cho phép bạn chỉ định một tiến trình cụ thể mà bạn muốn đưa về chế độ foreground. Nếu không chỉ định, `fg` sẽ đưa tiến trình gần nhất về foreground.

## Ví dụ
### Ví dụ 1: Đưa tiến trình gần nhất về foreground
Giả sử bạn đã chạy một lệnh tốn thời gian như `sleep 100 &` trong chế độ nền. Bạn có thể sử dụng lệnh sau để đưa nó về foreground:
```bash
fg
```

### Ví dụ 2: Đưa một tiến trình cụ thể về foreground
Nếu bạn đã chạy nhiều tiến trình và muốn đưa một tiến trình cụ thể về foreground, bạn có thể sử dụng cú pháp sau. Giả sử bạn đã có một danh sách các tiến trình với số thứ tự là 1:
```bash
fg %1
```
Điều này sẽ đưa tiến trình có số thứ tự 1 về foreground.

## Mẹo
- Bạn có thể xem danh sách các tiến trình đang chạy ở chế độ nền bằng cách sử dụng lệnh `jobs`. Điều này sẽ giúp bạn xác định số thứ tự của tiến trình mà bạn muốn đưa về foreground.
- Nếu bạn muốn tạm dừng một tiến trình đang chạy ở foreground, bạn có thể sử dụng tổ hợp phím `Ctrl + Z`. Sau đó, bạn có thể sử dụng `fg` để đưa nó trở lại foreground.
- Hãy nhớ rằng khi một tiến trình đang chạy ở foreground, bạn không thể thực hiện các lệnh khác cho đến khi tiến trình đó kết thúc hoặc được tạm dừng.