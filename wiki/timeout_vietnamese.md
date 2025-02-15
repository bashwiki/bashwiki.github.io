# [리눅스] Bash timeout 사용법

## Tổng quan
Lệnh `timeout` trong Bash được sử dụng để giới hạn thời gian thực thi của một lệnh hoặc một tập lệnh. Mục đích chính của lệnh này là ngăn chặn các lệnh chạy quá lâu, giúp quản lý tài nguyên hệ thống hiệu quả hơn và tránh tình trạng treo hoặc không phản hồi.

## Cách sử dụng
Cú pháp cơ bản của lệnh `timeout` như sau:

```bash
timeout [OPTION] DURATION COMMAND [ARGUMENTS...]
```

Trong đó:
- `DURATION`: Thời gian tối đa cho phép lệnh chạy, có thể được chỉ định bằng các đơn vị như giây (s), phút (m), giờ (h), hoặc ngày (d).
- `COMMAND`: Lệnh hoặc tập lệnh mà bạn muốn thực thi.
- `ARGUMENTS`: Các tham số tùy chọn cho lệnh.

### Các tùy chọn phổ biến
- `-k, --kill-after=DURATION`: Thời gian chờ trước khi gửi tín hiệu kill đến lệnh sau khi thời gian timeout đã hết.
- `-s, --signal=SIGNAL`: Tín hiệu mà bạn muốn gửi đến lệnh khi hết thời gian (mặc định là `TERM`).

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `timeout`.

### Ví dụ 1: Giới hạn thời gian thực thi của một lệnh
```bash
timeout 5s sleep 10
```
Trong ví dụ này, lệnh `sleep 10` sẽ bị dừng sau 5 giây, vì thời gian tối đa được chỉ định là 5 giây.

### Ví dụ 2: Gửi tín hiệu kill sau khi hết thời gian
```bash
timeout -k 2s 5s sleep 10
```
Ở ví dụ này, lệnh `sleep 10` sẽ bị dừng sau 5 giây, và nếu nó vẫn còn chạy, lệnh sẽ nhận tín hiệu kill sau 2 giây nữa.

## Mẹo
- Khi sử dụng `timeout`, hãy luôn kiểm tra xem lệnh bạn đang chạy có thể xử lý tín hiệu mà bạn gửi hay không. Một số lệnh có thể không phản hồi đúng cách với tín hiệu `TERM`.
- Sử dụng tùy chọn `-k` để đảm bảo rằng các lệnh không bị treo sẽ được dừng lại một cách an toàn.
- Hãy thử nghiệm với các khoảng thời gian khác nhau để tìm ra thời gian tối ưu cho các lệnh cụ thể trong môi trường của bạn.

Lệnh `timeout` là một công cụ mạnh mẽ giúp bạn quản lý thời gian thực thi của các lệnh trong Bash, đảm bảo rằng bạn có thể kiểm soát tốt hơn các tác vụ trong hệ thống của mình.