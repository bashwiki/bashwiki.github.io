# [리눅스] Bash local 사용법

## Tổng quan
Lệnh `local` trong Bash được sử dụng để khai báo biến cục bộ trong một hàm. Biến cục bộ chỉ có thể được truy cập và sử dụng trong phạm vi của hàm mà nó được định nghĩa, giúp tránh xung đột với các biến toàn cục hoặc các biến trong các hàm khác. Điều này rất hữu ích khi bạn muốn giữ cho các biến của mình không bị ảnh hưởng bởi các phần khác của script.

## Cách sử dụng
Cú pháp cơ bản của lệnh `local` như sau:

```bash
local [tùy chọn] tên_biến=[giá_trị]
```

### Tùy chọn thông thường
- `tên_biến`: Tên của biến mà bạn muốn khai báo là cục bộ.
- `giá_trị`: Giá trị mà bạn muốn gán cho biến cục bộ.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `local`.

### Ví dụ 1: Khai báo biến cục bộ trong hàm
```bash
my_function() {
    local my_var="Hello, World!"
    echo $my_var
}

my_function
echo $my_var  # Không có giá trị, vì my_var là biến cục bộ
```
Trong ví dụ này, biến `my_var` được khai báo là cục bộ trong hàm `my_function`. Khi gọi hàm, nó in ra giá trị của `my_var`, nhưng khi cố gắng in ra bên ngoài hàm, nó không có giá trị.

### Ví dụ 2: Sử dụng biến cục bộ để tránh xung đột
```bash
global_var="I'm global"

my_function() {
    local global_var="I'm local"
    echo $global_var
}

my_function  # In ra: I'm local
echo $global_var  # In ra: I'm global
```
Trong ví dụ này, biến `global_var` được khai báo cả ở cấp toàn cục và cục bộ. Hàm `my_function` sẽ in ra giá trị của biến cục bộ, trong khi biến toàn cục vẫn giữ nguyên giá trị của nó.

## Mẹo
- Sử dụng `local` để giảm thiểu khả năng xung đột giữa các biến trong các hàm khác nhau.
- Luôn khai báo biến cục bộ trong hàm ngay sau khi bắt đầu hàm để đảm bảo rằng biến chỉ tồn tại trong phạm vi đó.
- Sử dụng biến cục bộ để làm cho mã của bạn dễ đọc và bảo trì hơn, vì nó giúp xác định rõ ràng phạm vi của các biến.