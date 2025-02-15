# [리눅스] Bash wait 사용법

## Tổng quan
Lệnh `wait` trong Bash được sử dụng để chờ một hoặc nhiều tiến trình con hoàn thành. Khi bạn chạy một lệnh trong nền (background), bạn có thể sử dụng `wait` để đợi cho lệnh đó hoàn tất trước khi tiếp tục thực hiện các lệnh khác trong script. Lệnh này rất hữu ích trong các kịch bản tự động hóa và quản lý tiến trình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `wait` như sau:

```bash
wait [PID]
```

- `PID`: Là ID của tiến trình mà bạn muốn chờ. Nếu không chỉ định PID, lệnh `wait` sẽ chờ tất cả các tiến trình con đang chạy trong shell hiện tại.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `wait`.

### Ví dụ 1: Chờ một tiến trình cụ thể
```bash
#!/bin/bash

sleep 5 &  # Chạy lệnh sleep trong nền
pid=$!     # Lưu PID của tiến trình vừa chạy
echo "Đang chờ tiến trình $pid hoàn tất..."
wait $pid # Chờ cho tiến trình hoàn tất
echo "Tiến trình $pid đã hoàn tất!"
```

### Ví dụ 2: Chờ tất cả các tiến trình con
```bash
#!/bin/bash

for i in {1..3}; do
    sleep $i &  # Chạy nhiều lệnh sleep trong nền
done

echo "Đang chờ tất cả các tiến trình hoàn tất..."
wait  # Chờ cho tất cả các tiến trình con hoàn tất
echo "Tất cả các tiến trình đã hoàn tất!"
```

## Mẹo
- Sử dụng `wait` mà không có tham số PID sẽ giúp bạn chờ tất cả các tiến trình con, điều này rất hữu ích khi bạn không muốn quản lý từng PID riêng lẻ.
- Khi sử dụng `wait`, hãy đảm bảo rằng bạn đã chạy các tiến trình con trong nền bằng cách sử dụng ký tự `&`, nếu không lệnh sẽ không trả về cho đến khi tiến trình hiện tại hoàn tất.
- Lệnh `wait` có thể trả về mã thoát của tiến trình mà bạn đang chờ, điều này có thể được sử dụng để kiểm tra xem tiến trình đã hoàn tất thành công hay không.

Hy vọng rằng bài viết này sẽ giúp bạn hiểu rõ hơn về cách sử dụng lệnh `wait` trong Bash!