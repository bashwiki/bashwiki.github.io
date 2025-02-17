# [Linux] Bash local lệnh: Tạo biến cục bộ trong hàm

## Overview
Lệnh `local` trong Bash được sử dụng để khai báo các biến cục bộ trong một hàm. Các biến này chỉ tồn tại trong phạm vi của hàm đó và không ảnh hưởng đến các biến bên ngoài.

## Usage
Cú pháp cơ bản của lệnh `local` như sau:
```bash
local [options] [variable_name=value]
```

## Common Options
- Không có tùy chọn đặc biệt nào cho lệnh `local`, nhưng bạn có thể sử dụng nó với nhiều biến cùng một lúc.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `local`:

### Ví dụ 1: Khai báo biến cục bộ
```bash
my_function() {
    local my_var="Hello, World!"
    echo $my_var
}

my_function  # Kết quả: Hello, World!
echo $my_var  # Không có kết quả, vì my_var là biến cục bộ
```

### Ví dụ 2: Sử dụng nhiều biến cục bộ
```bash
my_function() {
    local var1="Value 1"
    local var2="Value 2"
    echo "$var1 and $var2"
}

my_function  # Kết quả: Value 1 and Value 2
```

### Ví dụ 3: Biến cục bộ với tham số
```bash
my_function() {
    local name=$1
    echo "Hello, $name!"
}

my_function "Alice"  # Kết quả: Hello, Alice!
```

## Tips
- Sử dụng `local` để tránh xung đột tên biến giữa các hàm.
- Luôn khai báo biến cục bộ trong hàm ngay khi bắt đầu để dễ quản lý.
- Kiểm tra phạm vi của biến bằng cách thử truy cập chúng bên ngoài hàm để đảm bảo chúng không tồn tại.