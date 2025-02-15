# [리눅스] Bash jobs 사용법

## Tổng quan
Lệnh `jobs` trong Bash được sử dụng để hiển thị danh sách các tiến trình (jobs) đang chạy trong phiên làm việc hiện tại của người dùng. Nó cho phép bạn theo dõi các tiến trình nền và tiến trình đang chạy, giúp bạn quản lý chúng một cách hiệu quả hơn. Lệnh này rất hữu ích khi bạn muốn xem trạng thái của các tiến trình mà bạn đã khởi động từ dòng lệnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `jobs` như sau:

```bash
jobs [options]
```

### Các tùy chọn phổ biến:
- `-l`: Hiển thị PID (Process ID) của mỗi tiến trình.
- `-n`: Chỉ hiển thị các tiến trình đã thay đổi trạng thái kể từ lần gọi lệnh trước đó.
- `-p`: Chỉ hiển thị PID của các tiến trình.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `jobs`.

### Ví dụ 1: Hiển thị danh sách các tiến trình
Khi bạn chạy một số lệnh trong nền, bạn có thể sử dụng lệnh `jobs` để xem chúng:

```bash
sleep 100 &
sleep 200 &
jobs
```

Kết quả sẽ hiển thị danh sách các tiến trình đang chạy trong nền.

### Ví dụ 2: Hiển thị PID của các tiến trình
Nếu bạn muốn biết PID của các tiến trình, bạn có thể sử dụng tùy chọn `-l`:

```bash
sleep 100 &
sleep 200 &
jobs -l
```

Kết quả sẽ hiển thị danh sách các tiến trình cùng với PID của chúng.

## Mẹo
- Sử dụng lệnh `bg` và `fg` để chuyển đổi giữa các tiến trình nền và tiến trình foreground. Bạn có thể sử dụng số thứ tự của tiến trình hiển thị từ lệnh `jobs` để xác định tiến trình nào bạn muốn chuyển đổi.
- Thường xuyên kiểm tra các tiến trình đang chạy bằng lệnh `jobs` để đảm bảo rằng bạn không bỏ lỡ bất kỳ tiến trình nào có thể cần được quản lý hoặc dừng lại.
- Kết hợp lệnh `jobs` với các lệnh khác như `kill` để dừng các tiến trình không còn cần thiết.

Lệnh `jobs` là một công cụ mạnh mẽ giúp bạn quản lý các tiến trình trong Bash một cách hiệu quả và dễ dàng.