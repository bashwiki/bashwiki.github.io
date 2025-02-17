# [Linux] Bash return <Sử dụng tương đương>: Trả về mã thoát của một lệnh

## Overview
Lệnh `return` trong Bash được sử dụng để trả về mã thoát từ một hàm. Mã thoát này thường được sử dụng để xác định xem hàm đã thực thi thành công hay không, với giá trị 0 thường biểu thị thành công và các giá trị khác biểu thị lỗi.

## Usage
Cú pháp cơ bản của lệnh `return` như sau:
```
return [options] [n]
```

## Common Options
- `n`: Mã thoát mà bạn muốn trả về. Nếu không chỉ định, mã thoát cuối cùng của lệnh sẽ được sử dụng.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `return`:

### Ví dụ 1: Trả về mã thoát mặc định
```bash
my_function() {
    echo "Đang thực hiện một số công việc..."
    return 0
}
my_function
echo "Mã thoát: $?"  # In ra mã thoát của hàm
```

### Ví dụ 2: Trả về mã thoát tùy chỉnh
```bash
my_function() {
    echo "Có lỗi xảy ra!"
    return 1
}
my_function
echo "Mã thoát: $?"  # In ra mã thoát của hàm
```

### Ví dụ 3: Sử dụng trong một hàm kiểm tra
```bash
check_file() {
    if [[ -f $1 ]]; then
        echo "Tập tin tồn tại."
        return 0
    else
        echo "Tập tin không tồn tại."
        return 1
    fi
}
check_file "test.txt"
echo "Mã thoát: $?"  # In ra mã thoát của hàm
```

## Tips
- Sử dụng mã thoát 0 để chỉ ra rằng hàm đã thực thi thành công và các giá trị khác để chỉ ra lỗi.
- Kiểm tra mã thoát ngay sau khi gọi hàm để đảm bảo bạn nhận được kết quả chính xác.
- Kết hợp lệnh `return` với các lệnh điều kiện để tạo ra các hàm mạnh mẽ và có thể xử lý lỗi tốt hơn.