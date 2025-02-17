# [Linux] Bash let: Thực hiện phép toán số học

## Overview
Lệnh `let` trong Bash được sử dụng để thực hiện các phép toán số học đơn giản. Nó cho phép bạn tính toán và gán giá trị cho các biến mà không cần phải sử dụng dấu `$` trước tên biến.

## Usage
Cú pháp cơ bản của lệnh `let` như sau:

```bash
let [options] [arguments]
```

## Common Options
- `-n`: Không in ra giá trị của biểu thức.
- `-e`: Kích hoạt chế độ lỗi, dừng thực thi nếu có lỗi xảy ra trong phép toán.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `let`:

### Ví dụ 1: Cộng hai số
```bash
let "a = 5 + 3"
echo $a  # Kết quả: 8
```

### Ví dụ 2: Trừ hai số
```bash
let "b = 10 - 4"
echo $b  # Kết quả: 6
```

### Ví dụ 3: Nhân hai số
```bash
let "c = 7 * 6"
echo $c  # Kết quả: 42
```

### Ví dụ 4: Chia hai số
```bash
let "d = 20 / 5"
echo $d  # Kết quả: 4
```

### Ví dụ 5: Sử dụng biến
```bash
x=10
y=5
let "result = x + y"
echo $result  # Kết quả: 15
```

## Tips
- Sử dụng dấu ngoặc kép để bao quanh biểu thức phức tạp để tránh lỗi cú pháp.
- Bạn có thể sử dụng `let` để thực hiện nhiều phép toán trong cùng một lệnh bằng cách phân tách chúng bằng dấu phẩy.
- Hãy nhớ rằng `let` không in ra kết quả, vì vậy bạn cần sử dụng `echo` để xem giá trị của biến sau khi thực hiện phép toán.