# [Linux] Bash rev: Đảo ngược chuỗi ký tự

## Overview
Lệnh `rev` trong Bash được sử dụng để đảo ngược thứ tự các ký tự trong mỗi dòng của đầu vào. Điều này có nghĩa là nếu bạn có một chuỗi văn bản, lệnh này sẽ biến nó thành chuỗi ngược lại.

## Usage
Cú pháp cơ bản của lệnh `rev` như sau:
```
rev [options] [arguments]
```

## Common Options
- `-h`, `--help`: Hiển thị thông tin trợ giúp về lệnh `rev`.
- `-V`, `--version`: Hiển thị phiên bản của lệnh `rev`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `rev`:

1. **Đảo ngược một chuỗi văn bản từ đầu vào tiêu chuẩn**:
   ```bash
   echo "Hello World" | rev
   ```
   Kết quả sẽ là: `dlroW olleH`

2. **Đảo ngược nội dung của một tệp**:
   ```bash
   rev filename.txt
   ```
   Lệnh này sẽ đảo ngược từng dòng trong tệp `filename.txt`.

3. **Đảo ngược nhiều dòng văn bản**:
   ```bash
   echo -e "Line 1\nLine 2\nLine 3" | rev
   ```
   Kết quả sẽ là:
   ```
   enil 1
   enil 2
   enil 3
   ```

## Tips
- Bạn có thể kết hợp lệnh `rev` với các lệnh khác trong Bash để xử lý văn bản phức tạp hơn.
- Hãy chắc chắn rằng bạn đã kiểm tra đầu vào của mình, vì lệnh `rev` sẽ chỉ đảo ngược ký tự mà không thay đổi nội dung khác.