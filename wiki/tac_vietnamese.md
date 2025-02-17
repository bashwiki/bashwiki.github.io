# [Linux] Bash tac cách sử dụng: Đảo ngược nội dung tệp

## Overview
Lệnh `tac` trong Bash được sử dụng để hiển thị nội dung của một tệp theo thứ tự ngược lại, tức là dòng cuối cùng sẽ được hiển thị trước tiên và dòng đầu tiên sẽ được hiển thị cuối cùng.

## Usage
Cú pháp cơ bản của lệnh `tac` như sau:
```
tac [options] [arguments]
```

## Common Options
- `-r`, `--regex`: Sử dụng biểu thức chính quy để tách các dòng.
- `-s`, `--separator=STRING`: Chỉ định chuỗi phân tách giữa các dòng.
- `-b`, `--before`: Đảo ngược các dòng nhưng giữ nguyên thứ tự của các dòng phân tách.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `tac`:

1. **Đảo ngược nội dung của một tệp:**
   ```bash
   tac ten_tap.txt
   ```

2. **Lưu nội dung đảo ngược vào một tệp mới:**
   ```bash
   tac ten_tap.txt > ten_tap_moi.txt
   ```

3. **Sử dụng tùy chọn phân tách:**
   ```bash
   tac -s "," ten_tap.txt
   ```

4. **Sử dụng biểu thức chính quy để tách các dòng:**
   ```bash
   tac -r ten_tap.txt
   ```

## Tips
- Hãy chắc chắn rằng bạn đã kiểm tra nội dung tệp trước khi sử dụng `tac` để tránh nhầm lẫn.
- Khi làm việc với các tệp lớn, bạn có thể muốn kết hợp `tac` với `less` để dễ dàng xem nội dung:
  ```bash
  tac ten_tap.txt | less
  ```
- Sử dụng `tac` trong các kịch bản tự động để xử lý dữ liệu theo thứ tự ngược lại một cách hiệu quả.