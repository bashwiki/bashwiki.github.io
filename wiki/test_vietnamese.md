# [리눅스] Bash test 사용법

## Tổng quan
Lệnh `test` trong Bash được sử dụng để kiểm tra điều kiện và đánh giá các biểu thức. Lệnh này thường được sử dụng trong các câu lệnh điều kiện như `if`, `while`, hoặc `until` để xác định xem một điều kiện có đúng hay không. Nếu điều kiện đúng, lệnh `test` trả về mã thoát 0 (thành công), ngược lại, nó trả về mã thoát 1 (thất bại).

## Cách sử dụng
Cú pháp cơ bản của lệnh `test` như sau:

```bash
test EXPRESSION
```

Hoặc bạn có thể sử dụng cú pháp sau với dấu ngoặc vuông:

```bash
[ EXPRESSION ]
```

### Các tùy chọn phổ biến
- `-e FILE`: Kiểm tra xem tệp có tồn tại hay không.
- `-d FILE`: Kiểm tra xem tệp có phải là thư mục hay không.
- `-f FILE`: Kiểm tra xem tệp có phải là tệp thường hay không.
- `-z STRING`: Kiểm tra xem chuỗi có rỗng hay không.
- `-n STRING`: Kiểm tra xem chuỗi có không rỗng hay không.
- `STRING1 = STRING2`: Kiểm tra xem hai chuỗi có bằng nhau hay không.
- `STRING1 != STRING2`: Kiểm tra xem hai chuỗi có khác nhau hay không.

## Ví dụ
### Ví dụ 1: Kiểm tra sự tồn tại của một tệp
```bash
if test -e myfile.txt; then
    echo "Tệp myfile.txt tồn tại."
else
    echo "Tệp myfile.txt không tồn tại."
fi
```

### Ví dụ 2: Kiểm tra một chuỗi
```bash
my_string="Hello"
if test -n "$my_string"; then
    echo "Chuỗi không rỗng."
else
    echo "Chuỗi rỗng."
fi
```

## Mẹo
- Sử dụng dấu ngoặc vuông `[` thay cho lệnh `test` để làm cho mã dễ đọc hơn. Ví dụ: `[ -e myfile.txt ]` có thể dễ hiểu hơn so với `test -e myfile.txt`.
- Đảm bảo sử dụng dấu cách đúng cách giữa các tham số và dấu ngoặc để tránh lỗi cú pháp.
- Khi kiểm tra nhiều điều kiện, bạn có thể sử dụng các toán tử logic như `-a` (và) và `-o` (hoặc) để kết hợp các điều kiện.