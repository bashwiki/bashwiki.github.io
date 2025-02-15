# [리눅스] Bash true 사용법

## Tổng quan
Lệnh `true` trong Bash là một lệnh rất đơn giản nhưng có ích. Nó không thực hiện bất kỳ hành động nào ngoại trừ việc trả về mã thoát 0, điều này cho biết rằng lệnh đã hoàn thành thành công. Lệnh này thường được sử dụng trong các kịch bản shell để tạo ra một điều kiện luôn đúng, hoặc để duy trì một vòng lặp vô hạn mà không làm gì cả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `true` rất đơn giản:

```bash
true
```

Lệnh này không có tùy chọn nào đặc biệt. Khi được gọi, nó sẽ chỉ trả về mã thoát 0 mà không có bất kỳ đầu ra nào.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `true`:

### Ví dụ 1: Sử dụng trong vòng lặp
Bạn có thể sử dụng `true` để tạo một vòng lặp vô hạn:

```bash
while true; do
    echo "Vòng lặp đang chạy..."
    sleep 1
done
```
Trong ví dụ này, vòng lặp sẽ tiếp tục chạy và in ra "Vòng lặp đang chạy..." mỗi giây cho đến khi bạn dừng nó bằng cách nhấn `Ctrl+C`.

### Ví dụ 2: Sử dụng trong điều kiện
Lệnh `true` có thể được sử dụng trong các điều kiện để đảm bảo rằng một khối mã luôn được thực thi:

```bash
if true; then
    echo "Điều kiện luôn đúng!"
fi
```
Khi chạy đoạn mã này, bạn sẽ thấy thông báo "Điều kiện luôn đúng!" được in ra.

## Mẹo
- Lệnh `true` rất hữu ích trong các kịch bản shell để kiểm tra các điều kiện mà không cần thực hiện bất kỳ hành động nào khác.
- Bạn có thể kết hợp `true` với các lệnh khác trong các kịch bản phức tạp hơn để tạo ra các điều kiện hoặc vòng lặp mà không cần phải viết mã phức tạp.
- Hãy cẩn thận khi sử dụng vòng lặp vô hạn với `true`, vì chúng có thể làm cho hệ thống của bạn không phản hồi nếu không có cách dừng thích hợp.