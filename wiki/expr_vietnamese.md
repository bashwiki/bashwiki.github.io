# [Linux] Bash expr cách sử dụng: Tính toán và so sánh

## Tổng quan
Lệnh `expr` trong Bash được sử dụng để thực hiện các phép toán số học và so sánh. Nó cho phép người dùng thực hiện các phép toán cơ bản như cộng, trừ, nhân, chia, cũng như so sánh các giá trị.

## Cú pháp
Cú pháp cơ bản của lệnh `expr` như sau:
```bash
expr [options] [arguments]
```

## Các tùy chọn phổ biến
- `+` : Phép cộng.
- `-` : Phép trừ.
- `*` : Phép nhân (cần phải sử dụng dấu escape `\*` hoặc đặt trong dấu nháy đơn).
- `/` : Phép chia.
- `%` : Phép chia lấy dư.
- `=` : So sánh bằng.
- `!=` : So sánh khác.
- `<` : So sánh nhỏ hơn.
- `>` : So sánh lớn hơn.

## Ví dụ phổ biến
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `expr`:

### Phép cộng
```bash
expr 5 + 3
```
Kết quả sẽ là `8`.

### Phép trừ
```bash
expr 10 - 4
```
Kết quả sẽ là `6`.

### Phép nhân
```bash
expr 7 \* 6
```
Kết quả sẽ là `42`.

### Phép chia
```bash
expr 20 / 4
```
Kết quả sẽ là `5`.

### So sánh
```bash
expr 5 = 5
```
Kết quả sẽ là `1` (đúng).

```bash
expr 5 != 3
```
Kết quả sẽ là `1` (đúng).

## Mẹo
- Khi sử dụng phép nhân, hãy nhớ sử dụng dấu escape `\*` hoặc đặt trong dấu nháy đơn để tránh lỗi cú pháp.
- Để tránh lỗi khi sử dụng các phép toán, hãy đảm bảo rằng các giá trị được truyền vào là số.
- Sử dụng lệnh `expr` trong các câu lệnh điều kiện để kiểm tra các giá trị trước khi thực hiện các hành động khác trong script.