# [Linux] Bash tr <Sử dụng tương đương>: Chuyển đổi ký tự trong văn bản

## Overview
Lệnh `tr` trong Bash được sử dụng để chuyển đổi hoặc xóa các ký tự trong văn bản. Nó rất hữu ích khi bạn cần thay đổi định dạng của dữ liệu đầu vào hoặc loại bỏ các ký tự không cần thiết.

## Usage
Cú pháp cơ bản của lệnh `tr` như sau:

```bash
tr [options] [arguments]
```

## Common Options
- `-d`: Xóa các ký tự được chỉ định.
- `-s`: Rút gọn các ký tự liên tiếp thành một ký tự duy nhất.
- `-c`: Chuyển đổi các ký tự không được chỉ định.
- `-t`: Thay thế các ký tự trong một chuỗi.

## Common Examples
Dưới đây là một số ví dụ thực tiễn về cách sử dụng lệnh `tr`:

1. **Chuyển đổi chữ thường thành chữ hoa:**
   ```bash
   echo "hello world" | tr 'a-z' 'A-Z'
   ```

2. **Xóa các ký tự không phải chữ số:**
   ```bash
   echo "abc123def456" | tr -d 'a-z'
   ```

3. **Rút gọn các khoảng trắng liên tiếp:**
   ```bash
   echo "This    is    a    test." | tr -s ' '
   ```

4. **Thay thế dấu phẩy bằng dấu chấm:**
   ```bash
   echo "1,2,3,4,5" | tr ',' '.'
   ```

## Tips
- Sử dụng `tr` với `echo` để thử nghiệm nhanh các chuyển đổi ký tự.
- Kết hợp `tr` với các lệnh khác như `grep` hoặc `sed` để xử lý văn bản phức tạp hơn.
- Hãy cẩn thận với các ký tự đặc biệt, vì chúng có thể ảnh hưởng đến kết quả của lệnh `tr`.