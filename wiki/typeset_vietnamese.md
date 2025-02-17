# [Linux] Bash typeset cách sử dụng: Định nghĩa biến trong Bash

## Tổng quan
Lệnh `typeset` trong Bash được sử dụng để định nghĩa và quản lý các biến, cho phép bạn thiết lập các thuộc tính cho biến như kiểu dữ liệu, phạm vi và khả năng đọc/ghi.

## Cách sử dụng
Cú pháp cơ bản của lệnh `typeset` như sau:
```bash
typeset [options] [arguments]
```

## Các tùy chọn phổ biến
- `-i`: Định nghĩa biến là số nguyên, cho phép thực hiện các phép toán số học.
- `-r`: Định nghĩa biến là chỉ đọc, không thể thay đổi giá trị sau khi đã được gán.
- `-x`: Định nghĩa biến là biến môi trường, có thể được truy cập từ các tiến trình con.
- `-a`: Định nghĩa biến là mảng, cho phép lưu trữ nhiều giá trị.

## Ví dụ thường gặp
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `typeset`:

### Định nghĩa biến số nguyên
```bash
typeset -i num=10
echo $((num + 5))  # Kết quả: 15
```

### Định nghĩa biến chỉ đọc
```bash
typeset -r readonly_var="Không thể thay đổi"
echo $readonly_var
# readonly_var="Giá trị mới"  # Lệnh này sẽ báo lỗi
```

### Định nghĩa biến môi trường
```bash
typeset -x env_var="Giá trị môi trường"
echo $env_var  # Kết quả: Giá trị môi trường
```

### Định nghĩa mảng
```bash
typeset -a my_array=("Giá trị 1" "Giá trị 2" "Giá trị 3")
echo ${my_array[1]}  # Kết quả: Giá trị 2
```

## Mẹo
- Sử dụng `typeset` để quản lý các biến trong script của bạn, giúp mã nguồn rõ ràng và dễ bảo trì hơn.
- Hãy cẩn thận khi sử dụng biến chỉ đọc, vì bạn sẽ không thể thay đổi giá trị của chúng sau khi đã được gán.
- Khi làm việc với mảng, hãy nhớ rằng chỉ số bắt đầu từ 0 trong Bash.