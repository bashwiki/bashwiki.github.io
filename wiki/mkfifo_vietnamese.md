# [리눅스] Bash mkfifo 사용법

## Tổng quan
Lệnh `mkfifo` trong Bash được sử dụng để tạo ra một FIFO (First In, First Out) đặc biệt, còn được gọi là "named pipe". FIFO cho phép các tiến trình giao tiếp với nhau thông qua việc đọc và ghi dữ liệu. Khi một tiến trình ghi vào FIFO, dữ liệu sẽ được lưu trữ cho đến khi một tiến trình khác đọc nó. Điều này rất hữu ích trong các ứng dụng đa tiến trình, nơi mà việc truyền dữ liệu giữa các tiến trình là cần thiết.

## Cách sử dụng
Cú pháp cơ bản của lệnh `mkfifo` như sau:

```bash
mkfifo [tùy chọn] tên_fifo
```

### Tùy chọn phổ biến
- `-m, --mode=MODE`: Chỉ định quyền truy cập cho FIFO được tạo ra. Quyền truy cập có thể được chỉ định bằng cách sử dụng các ký hiệu như `u=rwx`, `g=rx`, `o=r`, hoặc bằng cách sử dụng số (ví dụ: `0777`).
- `-Z, --context=CONTEXT`: Thiết lập ngữ cảnh SELinux cho FIFO.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `mkfifo`:

### Ví dụ 1: Tạo một FIFO đơn giản
```bash
mkfifo my_fifo
```
Lệnh này sẽ tạo ra một FIFO có tên là `my_fifo` trong thư mục hiện tại.

### Ví dụ 2: Tạo FIFO với quyền truy cập cụ thể
```bash
mkfifo -m 0666 my_fifo
```
Lệnh này sẽ tạo ra một FIFO có tên là `my_fifo` với quyền truy cập cho phép tất cả người dùng đọc và ghi vào FIFO.

## Mẹo
- Hãy nhớ rằng FIFO sẽ không hoạt động nếu không có ít nhất một tiến trình đang đọc hoặc ghi vào nó. Nếu không, tiến trình ghi sẽ bị chặn cho đến khi có một tiến trình đọc.
- Để kiểm tra xem FIFO đã được tạo thành công hay chưa, bạn có thể sử dụng lệnh `ls -l` để xem thông tin về FIFO.
- Sử dụng FIFO có thể giúp giảm độ phức tạp trong việc giao tiếp giữa các tiến trình, nhưng hãy cẩn thận với việc quản lý lỗi và tình trạng chờ đợi trong các ứng dụng lớn hơn.