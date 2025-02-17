# [Linux] Bash uniq Cách sử dụng: Loại bỏ các dòng trùng lặp trong tệp

## Overview
Lệnh `uniq` trong Bash được sử dụng để loại bỏ các dòng trùng lặp liên tiếp trong một tệp hoặc đầu ra của một lệnh khác. Nó rất hữu ích khi bạn muốn làm sạch dữ liệu và chỉ giữ lại các dòng duy nhất.

## Usage
Cú pháp cơ bản của lệnh `uniq` như sau:
```bash
uniq [options] [arguments]
```

## Common Options
- `-c`: Đếm số lần xuất hiện của mỗi dòng.
- `-d`: Hiển thị chỉ các dòng trùng lặp.
- `-u`: Hiển thị chỉ các dòng duy nhất.
- `-i`: Bỏ qua sự khác biệt giữa chữ hoa và chữ thường.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `uniq`:

1. **Loại bỏ các dòng trùng lặp trong tệp**:
   ```bash
   uniq input.txt output.txt
   ```

2. **Đếm số lần xuất hiện của mỗi dòng**:
   ```bash
   uniq -c input.txt
   ```

3. **Hiển thị chỉ các dòng trùng lặp**:
   ```bash
   uniq -d input.txt
   ```

4. **Hiển thị chỉ các dòng duy nhất**:
   ```bash
   uniq -u input.txt
   ```

5. **Bỏ qua sự khác biệt giữa chữ hoa và chữ thường**:
   ```bash
   uniq -i input.txt output.txt
   ```

## Tips
- Để `uniq` hoạt động chính xác, bạn nên sắp xếp tệp đầu vào trước khi sử dụng, vì `uniq` chỉ loại bỏ các dòng trùng lặp liên tiếp.
- Kết hợp `uniq` với lệnh `sort` để xử lý dữ liệu hiệu quả:
   ```bash
   sort input.txt | uniq > output.txt
   ```
- Sử dụng tùy chọn `-c` để có cái nhìn tổng quan về tần suất xuất hiện của các dòng trong tệp.