# [Linux] Bash wc cách sử dụng: Đếm số dòng, từ và ký tự trong tệp

## Overview
Lệnh `wc` (word count) trong Bash được sử dụng để đếm số dòng, số từ và số ký tự trong một hoặc nhiều tệp. Đây là một công cụ hữu ích để phân tích nội dung của tệp văn bản.

## Usage
Cú pháp cơ bản của lệnh `wc` như sau:
```bash
wc [options] [arguments]
```

## Common Options
- `-l`: Đếm số dòng trong tệp.
- `-w`: Đếm số từ trong tệp.
- `-c`: Đếm số ký tự trong tệp.
- `-m`: Đếm số ký tự (tính cả ký tự Unicode).
- `-L`: Hiển thị độ dài của dòng dài nhất trong tệp.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `wc`:

1. Đếm số dòng trong một tệp:
   ```bash
   wc -l ten_tap.txt
   ```

2. Đếm số từ trong một tệp:
   ```bash
   wc -w ten_tap.txt
   ```

3. Đếm số ký tự trong một tệp:
   ```bash
   wc -c ten_tap.txt
   ```

4. Đếm số dòng, số từ và số ký tự cùng một lúc:
   ```bash
   wc ten_tap.txt
   ```

5. Đếm độ dài của dòng dài nhất trong một tệp:
   ```bash
   wc -L ten_tap.txt
   ```

## Tips
- Bạn có thể kết hợp nhiều tùy chọn trong một lệnh, ví dụ: `wc -l -w ten_tap.txt` để đếm số dòng và số từ cùng một lúc.
- Nếu bạn muốn đếm nội dung từ nhiều tệp, chỉ cần liệt kê tên các tệp sau lệnh `wc`, ví dụ: `wc ten_tap1.txt ten_tap2.txt`.
- Sử dụng `wc` cùng với các lệnh khác qua ống (pipe) để phân tích đầu ra, ví dụ: `cat ten_tap.txt | wc -l` để đếm số dòng trong tệp.