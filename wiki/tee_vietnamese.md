# [리눅스] Bash tee 사용법

## Tổng quan
Lệnh `tee` trong Bash là một công cụ hữu ích cho phép bạn đọc dữ liệu từ đầu vào chuẩn (stdin) và ghi nó vào một hoặc nhiều tệp, đồng thời cũng gửi dữ liệu đó đến đầu ra chuẩn (stdout). Điều này rất hữu ích khi bạn muốn theo dõi đầu ra của một lệnh trong khi vẫn lưu trữ nó vào tệp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `tee` như sau:

```bash
tee [tùy chọn] [tệp...]
```

### Các tùy chọn phổ biến:
- `-a` hoặc `--append`: Ghi dữ liệu vào cuối tệp thay vì ghi đè lên tệp.
- `-i` hoặc `--ignore-interrupts`: Bỏ qua các tín hiệu ngắt khi đang ghi dữ liệu.
- `-p` hoặc `--output-error`: Chỉ định cách xử lý lỗi khi ghi vào tệp.

## Ví dụ
### Ví dụ 1: Ghi đầu ra vào tệp
Giả sử bạn muốn ghi đầu ra của lệnh `echo` vào tệp `output.txt`:

```bash
echo "Hello, World!" | tee output.txt
```

Lệnh này sẽ ghi "Hello, World!" vào tệp `output.txt` và cũng hiển thị nó trên màn hình.

### Ví dụ 2: Ghi đầu ra vào nhiều tệp
Bạn có thể ghi đầu ra vào nhiều tệp bằng cách chỉ định nhiều tệp trong lệnh:

```bash
echo "Logging data" | tee file1.txt file2.txt
```

Lệnh này sẽ ghi "Logging data" vào cả `file1.txt` và `file2.txt`, đồng thời hiển thị nó trên màn hình.

## Mẹo
- Sử dụng tùy chọn `-a` nếu bạn muốn thêm dữ liệu vào cuối tệp mà không ghi đè lên nội dung hiện có.
- Kết hợp `tee` với các lệnh khác trong chuỗi lệnh để theo dõi và lưu trữ đầu ra mà không làm mất thông tin.
- Khi làm việc với các tệp lớn, hãy cẩn thận với việc ghi đè, vì bạn có thể mất dữ liệu quan trọng nếu không sử dụng tùy chọn `-a`.