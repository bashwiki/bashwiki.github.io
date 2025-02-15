# [리눅스] Bash continue 사용법

## Tổng Quan
Lệnh `continue` trong Bash được sử dụng trong các vòng lặp như `for`, `while`, hoặc `until`. Mục đích chính của lệnh này là bỏ qua phần còn lại của vòng lặp hiện tại và tiếp tục với lần lặp tiếp theo. Điều này hữu ích khi bạn muốn bỏ qua một số điều kiện nhất định mà không cần phải thoát khỏi vòng lặp hoàn toàn.

## Cách Sử Dụng
Cú pháp cơ bản của lệnh `continue` là:

```bash
continue [n]
```

Trong đó:
- `n` (tùy chọn): Là số nguyên tùy chọn chỉ định vòng lặp nào sẽ tiếp tục. Nếu không có tham số `n`, lệnh `continue` sẽ tiếp tục vòng lặp gần nhất.

## Ví Dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `continue` trong Bash:

### Ví dụ 1: Sử dụng trong vòng lặp `for`
```bash
for i in {1..5}; do
    if [ $i -eq 3 ]; then
        continue
    fi
    echo "Số: $i"
done
```
**Giải thích**: Trong ví dụ này, khi `i` bằng 3, lệnh `continue` sẽ được thực thi, và câu lệnh `echo` sẽ không được thực hiện cho giá trị này. Kết quả sẽ là:
```
Số: 1
Số: 2
Số: 4
Số: 5
```

### Ví dụ 2: Sử dụng trong vòng lặp `while`
```bash
count=0
while [ $count -lt 5 ]; do
    count=$((count + 1))
    if [ $count -eq 2 ]; then
        continue
    fi
    echo "Đếm: $count"
done
```
**Giải thích**: Tương tự như ví dụ trước, khi `count` bằng 2, lệnh `continue` sẽ được thực thi, và giá trị 2 sẽ không được in ra. Kết quả sẽ là:
```
Đếm: 1
Đếm: 3
Đếm: 4
Đếm: 5
```

## Mẹo
- Sử dụng `continue` khi bạn muốn bỏ qua một số điều kiện cụ thể trong vòng lặp mà không cần phải thoát khỏi vòng lặp hoàn toàn.
- Đảm bảo rằng bạn kiểm tra các điều kiện một cách cẩn thận để tránh việc bỏ qua các giá trị quan trọng.
- Lệnh `continue` có thể làm cho mã của bạn trở nên dễ đọc hơn bằng cách giảm bớt số lượng lệnh lồng nhau.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `continue` trong Bash!