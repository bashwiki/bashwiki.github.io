# [리눅스] Bash history 사용법

## Tổng quan
Lệnh `history` trong Bash được sử dụng để hiển thị danh sách các lệnh mà người dùng đã thực hiện trong phiên làm việc hiện tại. Mục đích chính của lệnh này là giúp người dùng dễ dàng theo dõi và truy cập lại các lệnh đã sử dụng trước đó, từ đó tiết kiệm thời gian và tăng hiệu quả làm việc.

## Cách sử dụng
Cú pháp cơ bản của lệnh `history` như sau:

```bash
history [n]
```

Trong đó:
- `n` là số lượng lệnh mà bạn muốn hiển thị. Nếu không chỉ định `n`, lệnh sẽ hiển thị toàn bộ lịch sử lệnh.

Một số tùy chọn phổ biến của lệnh `history` bao gồm:
- `-c`: Xóa toàn bộ lịch sử lệnh.
- `-d offset`: Xóa lệnh tại vị trí `offset` trong lịch sử.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `history`:

1. Hiển thị toàn bộ lịch sử lệnh:
   ```bash
   history
   ```

2. Hiển thị 5 lệnh gần đây nhất:
   ```bash
   history 5
   ```

3. Xóa toàn bộ lịch sử lệnh:
   ```bash
   history -c
   ```

## Mẹo
- Sử dụng phím mũi tên lên và xuống trên bàn phím để duyệt qua các lệnh đã sử dụng mà không cần phải gõ lại lệnh `history`.
- Bạn có thể sử dụng `!n` để thực thi lại lệnh thứ `n` trong lịch sử. Ví dụ, `!100` sẽ thực thi lại lệnh thứ 100.
- Để tìm kiếm lệnh trong lịch sử, bạn có thể sử dụng `Ctrl + r` và bắt đầu gõ một phần của lệnh mà bạn muốn tìm kiếm.