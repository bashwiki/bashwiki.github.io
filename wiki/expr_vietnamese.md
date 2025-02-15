# [리눅스] Bash expr 사용법

## Tổng quan
Lệnh `expr` trong Bash được sử dụng để thực hiện các phép toán số học, so sánh và chuỗi. Lệnh này cho phép người dùng thực hiện các phép toán cơ bản như cộng, trừ, nhân, chia, cũng như so sánh các giá trị và xử lý chuỗi. Mặc dù `expr` không còn phổ biến như trước đây do sự phát triển của các lệnh khác như `bc` và `awk`, nó vẫn hữu ích trong một số tình huống đơn giản.

## Cách sử dụng
Cú pháp cơ bản của lệnh `expr` như sau:

```bash
expr [toán_hạng1] [toán_tử] [toán_hạng2]
```

Trong đó:
- `toán_hạng1` và `toán_hạng2` có thể là số hoặc chuỗi.
- `toán_tử` có thể là một trong các toán tử sau:
  - `+` : Cộng
  - `-` : Trừ
  - `*` : Nhân
  - `/` : Chia
  - `%` : Chia lấy dư
  - `=` : So sánh bằng
  - `!=` : So sánh khác
  - `<` : So sánh nhỏ hơn
  - `>` : So sánh lớn hơn

Lưu ý rằng khi sử dụng toán tử nhân `*`, bạn cần phải thoát nó bằng dấu `\` hoặc đặt nó trong dấu nháy đơn.

## Ví dụ
Dưới đây là một số ví dụ về cách sử dụng lệnh `expr`:

### Ví dụ 1: Thực hiện phép toán số học
```bash
result=$(expr 5 + 3)
echo "Kết quả: $result"
```
Kết quả sẽ là:
```
Kết quả: 8
```

### Ví dụ 2: So sánh hai số
```bash
a=10
b=20
if expr $a \< $b; then
  echo "$a nhỏ hơn $b"
else
  echo "$a không nhỏ hơn $b"
fi
```
Kết quả sẽ là:
```
10 nhỏ hơn 20
```

## Mẹo
- Khi sử dụng `expr`, hãy nhớ rằng các phép toán số học chỉ hoạt động với số nguyên. Nếu bạn cần thực hiện phép toán với số thực, hãy xem xét sử dụng `bc`.
- Để tránh lỗi do khoảng trắng, hãy đảm bảo rằng bạn không có khoảng trắng không cần thiết giữa các toán hạng và toán tử.
- Sử dụng dấu nháy đơn cho các chuỗi chứa khoảng trắng để tránh lỗi cú pháp.

Hy vọng rằng bài viết này sẽ giúp bạn hiểu rõ hơn về lệnh `expr` trong Bash và cách sử dụng nó hiệu quả trong các kịch bản lập trình của bạn!