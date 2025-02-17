# [Linux] Bash wait cách sử dụng: Chờ đợi tiến trình hoàn thành

## Overview
Lệnh `wait` trong Bash được sử dụng để chờ cho một hoặc nhiều tiến trình con hoàn thành. Khi tiến trình con kết thúc, lệnh `wait` sẽ trả về mã thoát của tiến trình đó. Điều này rất hữu ích khi bạn muốn đảm bảo rằng một tiến trình đã hoàn tất trước khi tiếp tục thực hiện các lệnh khác.

## Usage
Cú pháp cơ bản của lệnh `wait` như sau:
```bash
wait [options] [arguments]
```

## Common Options
- `-n`: Chờ cho bất kỳ tiến trình con nào hoàn thành.
- `-p`: Chờ cho tiến trình con có ID được chỉ định hoàn thành.

## Common Examples

### Ví dụ 1: Chờ một tiến trình cụ thể
```bash
sleep 5 &
pid=$!
wait $pid
echo "Tiến trình $pid đã hoàn thành."
```
Trong ví dụ này, lệnh `sleep 5` được chạy trong nền, và lệnh `wait` sẽ chờ cho tiến trình đó hoàn thành trước khi in ra thông báo.

### Ví dụ 2: Chờ tất cả các tiến trình con
```bash
for i in {1..3}; do
    sleep $i &
done
wait
echo "Tất cả các tiến trình đã hoàn thành."
```
Ở đây, ba tiến trình `sleep` được chạy song song, và lệnh `wait` sẽ chờ cho tất cả chúng hoàn tất.

### Ví dụ 3: Sử dụng tùy chọn -n
```bash
sleep 2 &
sleep 4 &
wait -n
echo "Một trong các tiến trình đã hoàn thành."
```
Lệnh `wait -n` sẽ chờ cho bất kỳ một tiến trình nào trong số các tiến trình con hoàn thành trước khi tiếp tục.

## Tips
- Sử dụng `wait` khi bạn cần đảm bảo rằng một tiến trình đã hoàn tất trước khi thực hiện các lệnh tiếp theo.
- Kết hợp `wait` với các lệnh chạy trong nền để tối ưu hóa thời gian thực thi của script.
- Kiểm tra mã thoát của tiến trình bằng cách sử dụng `wait` để xử lý lỗi một cách hiệu quả.