# [리눅스] Bash typeset 사용법

## Tổng quan
Lệnh `typeset` trong Bash được sử dụng để khai báo biến và thiết lập thuộc tính cho chúng. Nó cho phép người dùng xác định kiểu dữ liệu của biến, cũng như các thuộc tính như readonly (chỉ đọc) hoặc integer (số nguyên). Mặc dù `typeset` thường được sử dụng trong các shell như ksh và zsh, nó cũng có thể được sử dụng trong Bash để quản lý các biến một cách hiệu quả.

## Cú pháp
Cú pháp cơ bản của lệnh `typeset` như sau:
```bash
typeset [options] variable_name=value
```

### Các tùy chọn phổ biến
- `-i`: Đặt biến là số nguyên. Tất cả các giá trị gán cho biến này sẽ được coi là số nguyên.
- `-r`: Đặt biến là readonly, có nghĩa là giá trị của biến không thể thay đổi sau khi đã được gán.
- `-a`: Khai báo biến như một mảng.
- `-A`: Khai báo biến như một mảng liên kết (associative array).
- `-x`: Xuất biến ra môi trường (export), cho phép biến có thể được truy cập từ các shell con.

## Ví dụ
### Ví dụ 1: Khai báo biến số nguyên
```bash
typeset -i num=10
num=num+5
echo $num  # Kết quả: 15
```
Trong ví dụ này, biến `num` được khai báo là số nguyên và giá trị của nó được tự động tính toán.

### Ví dụ 2: Khai báo biến readonly
```bash
typeset -r constant=100
echo $constant  # Kết quả: 100
constant=200    # Lỗi: không thể thay đổi giá trị của biến readonly
```
Ở đây, biến `constant` được khai báo là readonly, do đó không thể thay đổi giá trị của nó sau khi đã được gán.

## Mẹo
- Sử dụng `typeset` để quản lý các biến trong các script phức tạp, giúp bạn dễ dàng kiểm soát kiểu dữ liệu và thuộc tính của biến.
- Khi làm việc với các mảng, hãy sử dụng tùy chọn `-a` hoặc `-A` để khai báo rõ ràng loại biến, giúp tránh nhầm lẫn trong quá trình lập trình.
- Hãy nhớ rằng `typeset` không phải là lệnh tích hợp trong tất cả các shell, vì vậy hãy kiểm tra tính tương thích nếu bạn đang viết script cho nhiều môi trường khác nhau.