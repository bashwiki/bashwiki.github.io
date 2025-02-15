# [리눅스] Bash trap 사용법

## Tổng quan
Lệnh `trap` trong Bash được sử dụng để xử lý các tín hiệu và sự kiện trong quá trình thực thi của một script. Mục đích chính của lệnh này là cho phép người dùng xác định các hành động cụ thể mà script sẽ thực hiện khi nhận được một tín hiệu nhất định, chẳng hạn như khi người dùng nhấn Ctrl+C (tín hiệu SIGINT) hoặc khi script kết thúc một cách bất ngờ.

## Cách sử dụng
Cú pháp cơ bản của lệnh `trap` như sau:

```bash
trap 'command' SIGNAL
```

Trong đó:
- `command`: là lệnh hoặc tập hợp các lệnh mà bạn muốn thực hiện khi nhận được tín hiệu.
- `SIGNAL`: là tín hiệu mà bạn muốn theo dõi. Một số tín hiệu phổ biến bao gồm:
  - `SIGINT`: Tín hiệu ngắt (Ctrl+C).
  - `SIGTERM`: Tín hiệu yêu cầu dừng.
  - `EXIT`: Tín hiệu khi script kết thúc.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `trap`.

### Ví dụ 1: Xử lý tín hiệu SIGINT
```bash
#!/bin/bash

trap 'echo "Script đã bị ngắt"; exit' SIGINT

while true; do
    echo "Đang chạy... Nhấn Ctrl+C để ngắt."
    sleep 1
done
```
Trong ví dụ này, khi người dùng nhấn Ctrl+C, thông báo "Script đã bị ngắt" sẽ được in ra và script sẽ kết thúc.

### Ví dụ 2: Dọn dẹp tài nguyên khi kết thúc script
```bash
#!/bin/bash

trap 'echo "Đang dọn dẹp..."; rm -f temp_file.txt; exit' EXIT

echo "Đang thực hiện một số công việc..."
touch temp_file.txt
sleep 5
echo "Công việc hoàn tất."
```
Trong ví dụ này, khi script kết thúc (dù là do tín hiệu hay do hoàn thành), lệnh dọn dẹp sẽ được thực hiện để xóa tệp tạm thời.

## Mẹo
- Hãy sử dụng `trap` để đảm bảo rằng các tài nguyên được dọn dẹp đúng cách khi script kết thúc, đặc biệt là khi làm việc với tệp hoặc kết nối mạng.
- Kiểm tra các tín hiệu mà script của bạn có thể nhận được và quyết định hành động phù hợp cho từng tín hiệu.
- Đặt lệnh `trap` ở đầu script để đảm bảo rằng nó luôn sẵn sàng xử lý các tín hiệu ngay từ khi bắt đầu thực thi.