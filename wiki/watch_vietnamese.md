# [리눅스] Bash watch 사용법

## Tổng quan
Lệnh `watch` trong Bash được sử dụng để thực thi một lệnh liên tục và hiển thị kết quả của lệnh đó trên màn hình, giúp người dùng theo dõi sự thay đổi của đầu ra theo thời gian thực. Điều này rất hữu ích cho việc giám sát các thông tin như trạng thái hệ thống, tiến trình, hoặc bất kỳ lệnh nào mà bạn muốn theo dõi thường xuyên.

## Cách sử dụng
Cú pháp cơ bản của lệnh `watch` như sau:

```bash
watch [options] command
```

Trong đó:
- `command`: Lệnh mà bạn muốn thực thi và theo dõi.
- `options`: Các tùy chọn đi kèm để điều chỉnh cách thức hoạt động của lệnh `watch`.

Một số tùy chọn thông dụng của lệnh `watch` bao gồm:
- `-n seconds`: Thiết lập khoảng thời gian (tính bằng giây) giữa các lần thực thi lệnh. Mặc định là 2 giây.
- `-d`: Đánh dấu sự thay đổi trong đầu ra giữa các lần thực thi.
- `-t`: Tắt tiêu đề hiển thị trên đầu màn hình.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `watch`:

1. Theo dõi trạng thái của một thư mục:

```bash
watch -n 5 ls -l /path/to/directory
```
Lệnh này sẽ thực thi `ls -l /path/to/directory` mỗi 5 giây, cho phép bạn theo dõi các thay đổi trong thư mục.

2. Giám sát tài nguyên hệ thống:

```bash
watch -d free -h
```
Lệnh này sẽ hiển thị thông tin về bộ nhớ hệ thống và đánh dấu các thay đổi giữa các lần thực thi.

## Mẹo
- Sử dụng tùy chọn `-d` để dễ dàng nhận thấy các thay đổi trong đầu ra, điều này rất hữu ích khi bạn cần theo dõi các thông tin biến động nhanh.
- Nếu bạn muốn dừng lệnh `watch`, chỉ cần nhấn `Ctrl+C`.
- Hãy cân nhắc sử dụng khoảng thời gian ngắn hơn cho các lệnh có thể thay đổi thường xuyên và dài hơn cho các lệnh ít thay đổi hơn để giảm tải cho hệ thống.