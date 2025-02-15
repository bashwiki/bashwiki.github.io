# [리눅스] Bash htop 사용법

## Tổng quan
`htop` là một công cụ giám sát hệ thống tương tác, cho phép người dùng theo dõi các tiến trình đang chạy trên hệ thống Linux. Nó cung cấp một giao diện đồ họa dễ sử dụng, cho phép người dùng xem thông tin chi tiết về CPU, bộ nhớ, và các tiến trình đang hoạt động. Khác với lệnh `top`, `htop` cho phép người dùng tương tác với các tiến trình, như dừng hoặc thay đổi ưu tiên của chúng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `htop` rất đơn giản:

```bash
htop
```

Khi bạn chạy lệnh này, `htop` sẽ khởi động và hiển thị giao diện người dùng với thông tin về các tiến trình. Một số tùy chọn phổ biến của `htop` bao gồm:

- `-d <giây>`: Thiết lập khoảng thời gian làm mới (refresh) giữa các lần cập nhật thông tin.
- `-p <PID>`: Chỉ hiển thị tiến trình với ID tiến trình (PID) cụ thể.
- `--sort-key <key>`: Sắp xếp các tiến trình theo khóa cụ thể (ví dụ: `PID`, `MEM`, `CPU`).

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng lệnh `htop`:

1. Chạy `htop` với khoảng thời gian làm mới là 2 giây:

```bash
htop -d 2
```

2. Chỉ hiển thị một tiến trình cụ thể với PID là 1234:

```bash
htop -p 1234
```

## Mẹo
- Sử dụng phím mũi tên để điều hướng giữa các tiến trình và phím `F9` để gửi tín hiệu đến một tiến trình (như `SIGKILL` để dừng tiến trình).
- Bạn có thể sử dụng phím `F6` để thay đổi khóa sắp xếp và phím `F10` để thoát khỏi `htop`.
- Để tìm kiếm một tiến trình cụ thể, bạn có thể nhấn `F3` và nhập tên hoặc PID của tiến trình.

Hy vọng rằng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng lệnh `htop` trong Bash!