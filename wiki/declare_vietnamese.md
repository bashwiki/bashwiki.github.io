# [Linux] Bash declare cách sử dụng: Khai báo biến trong Bash

## Overview
Lệnh `declare` trong Bash được sử dụng để khai báo biến và xác định thuộc tính của chúng. Nó cho phép người dùng kiểm soát cách mà các biến được xử lý trong shell, bao gồm việc xác định kiểu dữ liệu và các thuộc tính khác như readonly.

## Usage
Cú pháp cơ bản của lệnh `declare` như sau:
```bash
declare [options] [arguments]
```

## Common Options
- `-a`: Khai báo một mảng.
- `-i`: Khai báo một biến số nguyên, cho phép thực hiện phép toán số học.
- `-r`: Đặt biến thành readonly, không thể thay đổi giá trị sau khi đã được khai báo.
- `-x`: Đánh dấu biến là biến môi trường, có thể được sử dụng bởi các tiến trình con.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `declare`:

### Khai báo một biến đơn giản
```bash
declare myVar="Hello, World!"
echo $myVar
```

### Khai báo một mảng
```bash
declare -a myArray=("apple" "banana" "cherry")
echo ${myArray[1]}  # Kết quả: banana
```

### Khai báo một biến số nguyên
```bash
declare -i myInt=5
myInt+=10
echo $myInt  # Kết quả: 15
```

### Đặt biến readonly
```bash
declare -r myConst="This is a constant"
echo $myConst
# myConst="New value"  # Lệnh này sẽ gây lỗi vì myConst là readonly
```

### Khai báo biến môi trường
```bash
declare -x myEnvVar="Environment Variable"
echo $myEnvVar
```

## Tips
- Sử dụng `declare -p` để xem thông tin về biến đã khai báo, bao gồm kiểu và giá trị.
- Khi làm việc với mảng, hãy nhớ sử dụng cú pháp `${arrayName[index]}` để truy cập giá trị.
- Đặt biến thành readonly khi bạn muốn bảo vệ giá trị của nó khỏi việc bị thay đổi trong quá trình thực thi script.