# [Linux] Bash break cách sử dụng: Dừng vòng lặp

## Overview
Lệnh `break` trong Bash được sử dụng để thoát khỏi vòng lặp hiện tại. Khi lệnh này được thực thi, nó sẽ dừng vòng lặp và tiếp tục với câu lệnh tiếp theo sau vòng lặp đó.

## Usage
Cú pháp cơ bản của lệnh `break` như sau:
```bash
break [n]
```
Trong đó `n` là số lượng vòng lặp cần thoát. Nếu không chỉ định `n`, lệnh sẽ thoát khỏi vòng lặp gần nhất.

## Common Options
- `n`: Số lượng vòng lặp cần thoát. Nếu `n` được chỉ định, `break` sẽ thoát khỏi vòng lặp thứ `n` tính từ vòng lặp hiện tại.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `break`:

### Ví dụ 1: Thoát khỏi vòng lặp `for`
```bash
for i in {1..5}; do
  if [ $i -eq 3 ]; then
    break
  fi
  echo "Số: $i"
done
```
Kết quả sẽ là:
```
Số: 1
Số: 2
```

### Ví dụ 2: Thoát khỏi vòng lặp `while`
```bash
count=1
while true; do
  if [ $count -gt 5 ]; then
    break
  fi
  echo "Đếm: $count"
  ((count++))
done
```
Kết quả sẽ là:
```
Đếm: 1
Đếm: 2
Đếm: 3
Đếm: 4
Đếm: 5
```

### Ví dụ 3: Sử dụng `break` với `n`
```bash
for i in {1..10}; do
  if [ $i -eq 4 ]; then
    break 2
  fi
  echo "Số: $i"
done
```
Kết quả sẽ là:
```
Số: 1
Số: 2
```

## Tips
- Sử dụng `break` khi bạn cần dừng vòng lặp sớm hơn điều kiện tự nhiên của nó.
- Hãy cẩn thận khi sử dụng `break n`, vì nó có thể thoát khỏi nhiều vòng lặp, điều này có thể gây khó khăn trong việc theo dõi luồng chương trình.
- Kết hợp `break` với `if` để kiểm soát tốt hơn khi nào bạn muốn thoát khỏi vòng lặp.