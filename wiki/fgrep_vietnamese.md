# [Linux] Bash fgrep Cách sử dụng: Tìm kiếm chuỗi trong tệp

## Overview
Lệnh `fgrep` trong Bash được sử dụng để tìm kiếm các chuỗi cụ thể trong tệp mà không cần sử dụng biểu thức chính quy. Nó rất hữu ích khi bạn muốn tìm kiếm một chuỗi chính xác mà không cần phải lo lắng về các ký tự đặc biệt.

## Usage
Cú pháp cơ bản của lệnh `fgrep` như sau:
```
fgrep [options] [arguments]
```

## Common Options
- `-i`: Bỏ qua sự phân biệt chữ hoa chữ thường khi tìm kiếm.
- `-v`: In ra các dòng không chứa chuỗi tìm kiếm.
- `-c`: Đếm số dòng chứa chuỗi tìm kiếm và in ra số lượng.
- `-n`: In ra số dòng cùng với kết quả tìm kiếm.

## Common Examples
1. Tìm kiếm chuỗi "hello" trong tệp `file.txt`:
   ```bash
   fgrep "hello" file.txt
   ```

2. Tìm kiếm chuỗi "error" trong tệp `log.txt` mà không phân biệt chữ hoa chữ thường:
   ```bash
   fgrep -i "error" log.txt
   ```

3. Đếm số dòng chứa chuỗi "success" trong tệp `results.txt`:
   ```bash
   fgrep -c "success" results.txt
   ```

4. In ra các dòng không chứa chuỗi "test" trong tệp `data.txt`:
   ```bash
   fgrep -v "test" data.txt
   ```

5. Tìm kiếm chuỗi "warning" và in ra số dòng:
   ```bash
   fgrep -n "warning" log.txt
   ```

## Tips
- Sử dụng tùy chọn `-i` nếu bạn không chắc chắn về chữ hoa chữ thường trong chuỗi tìm kiếm.
- Kết hợp `fgrep` với các lệnh khác như `grep` hoặc `sort` để xử lý dữ liệu hiệu quả hơn.
- Đảm bảo rằng chuỗi tìm kiếm của bạn được đặt trong dấu ngoặc kép để tránh lỗi cú pháp.