# [Linux] Bash disown cách sử dụng: Giải phóng tiến trình khỏi terminal

## Tổng quan
Lệnh `disown` trong Bash được sử dụng để loại bỏ một hoặc nhiều tiến trình khỏi danh sách tiến trình của shell hiện tại. Khi một tiến trình bị disown, nó sẽ không còn nhận tín hiệu từ terminal, cho phép nó tiếp tục chạy ngay cả khi terminal bị đóng.

## Cú pháp
Cú pháp cơ bản của lệnh `disown` như sau:
```bash
disown [options] [arguments]
```

## Tùy chọn phổ biến
- `-h`: Giữ lại tiến trình khỏi việc nhận tín hiệu SIGHUP khi terminal bị đóng.
- `jobspec`: Chỉ định tiến trình cụ thể mà bạn muốn disown. Bạn có thể sử dụng số thứ tự của tiến trình hoặc tên của nó.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `disown`:

1. **Disown một tiến trình cụ thể**:
   ```bash
   sleep 100 &
   disown %1
   ```
   Trong ví dụ này, tiến trình `sleep 100` được chạy ở chế độ nền và sau đó bị disown.

2. **Disown tất cả tiến trình**:
   ```bash
   disown
   ```
   Lệnh này sẽ disown tất cả các tiến trình đang chạy trong background.

3. **Disown với tùy chọn -h**:
   ```bash
   long_running_process &
   disown -h %1
   ```
   Tiến trình `long_running_process` sẽ không nhận tín hiệu SIGHUP khi terminal bị đóng.

## Mẹo
- Hãy chắc chắn rằng bạn thực sự muốn disown một tiến trình trước khi thực hiện, vì bạn sẽ không thể điều khiển nó từ terminal sau khi disown.
- Sử dụng lệnh `jobs` để kiểm tra danh sách các tiến trình đang chạy trước khi disown.
- Nếu bạn muốn tiếp tục theo dõi tiến trình, hãy xem xét sử dụng `bg` hoặc `fg` thay vì disown.