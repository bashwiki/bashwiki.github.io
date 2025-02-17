# [Linux] Bash sort cách sử dụng: Sắp xếp dữ liệu

## Overview
Lệnh `sort` trong Bash được sử dụng để sắp xếp các dòng trong một tệp hoặc đầu ra của một lệnh theo thứ tự nhất định. Nó có thể sắp xếp theo thứ tự tăng dần hoặc giảm dần và hỗ trợ nhiều tùy chọn để tùy chỉnh cách sắp xếp.

## Usage
Cú pháp cơ bản của lệnh `sort` như sau:

```bash
sort [options] [arguments]
```

## Common Options
Dưới đây là một số tùy chọn phổ biến của lệnh `sort`:

- `-r`: Sắp xếp theo thứ tự giảm dần.
- `-n`: Sắp xếp theo giá trị số.
- `-k`: Chỉ định cột để sắp xếp.
- `-u`: Loại bỏ các dòng trùng lặp.
- `-o`: Ghi kết quả vào tệp.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `sort`:

1. Sắp xếp một tệp theo thứ tự tăng dần:
   ```bash
   sort filename.txt
   ```

2. Sắp xếp một tệp theo thứ tự giảm dần:
   ```bash
   sort -r filename.txt
   ```

3. Sắp xếp theo giá trị số:
   ```bash
   sort -n numbers.txt
   ```

4. Sắp xếp theo cột thứ hai trong tệp:
   ```bash
   sort -k 2 filename.txt
   ```

5. Ghi kết quả sắp xếp vào một tệp mới:
   ```bash
   sort filename.txt -o sorted.txt
   ```

## Tips
- Khi làm việc với các tệp lớn, hãy cân nhắc sử dụng tùy chọn `-o` để ghi trực tiếp kết quả vào tệp thay vì in ra màn hình.
- Sử dụng tùy chọn `-u` để loại bỏ các dòng trùng lặp, giúp kết quả sắp xếp của bạn trở nên gọn gàng hơn.
- Kết hợp `sort` với các lệnh khác như `uniq` để xử lý dữ liệu hiệu quả hơn.