# [Linux] Bash printf Cách sử dụng: In định dạng văn bản

## Overview
Lệnh `printf` trong Bash được sử dụng để in ra văn bản theo định dạng cụ thể. Nó cho phép người dùng tạo ra các chuỗi văn bản có định dạng phức tạp hơn so với lệnh `echo`, giúp việc hiển thị thông tin trở nên rõ ràng và dễ đọc hơn.

## Usage
Cú pháp cơ bản của lệnh `printf` như sau:
```
printf [options] [arguments]
```

## Common Options
- `-v var`: Gán kết quả định dạng cho biến `var` thay vì in ra màn hình.
- `-f format`: Chỉ định định dạng cho chuỗi đầu ra.
- `--help`: Hiển thị thông tin trợ giúp về lệnh `printf`.
- `--version`: Hiển thị phiên bản của lệnh `printf`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `printf`:

1. **In một chuỗi đơn giản:**
   ```bash
   printf "Hello, World!\n"
   ```

2. **In số với định dạng:**
   ```bash
   printf "Số nguyên: %d\n" 42
   ```

3. **In số thập phân:**
   ```bash
   printf "Số thập phân: %.2f\n" 3.14159
   ```

4. **In nhiều đối số:**
   ```bash
   printf "Tên: %s, Tuổi: %d\n" "Nguyễn Văn A" 30
   ```

5. **Gán kết quả cho biến:**
   ```bash
   printf -v result "Kết quả: %.1f" 9.876
   echo "$result"
   ```

## Tips
- Sử dụng `\n` để thêm dòng mới trong chuỗi in ra.
- Để định dạng số, hãy sử dụng các ký tự định dạng như `%d` cho số nguyên và `%.2f` cho số thập phân.
- Hãy cẩn thận với khoảng trắng trong định dạng, vì nó có thể ảnh hưởng đến cách hiển thị kết quả.