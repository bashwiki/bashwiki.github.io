# [Linux] Bash diff cách sử dụng: So sánh sự khác biệt giữa hai tệp

## Overview
Lệnh `diff` trong Bash được sử dụng để so sánh nội dung của hai tệp hoặc hai thư mục. Nó hiển thị những khác biệt giữa chúng, giúp người dùng dễ dàng nhận biết các thay đổi.

## Usage
Cú pháp cơ bản của lệnh `diff` như sau:

```bash
diff [options] [arguments]
```

## Common Options
- `-u`: Hiển thị kết quả theo định dạng "unified", giúp dễ đọc hơn.
- `-i`: Bỏ qua sự khác biệt về chữ hoa và chữ thường.
- `-w`: Bỏ qua tất cả các khoảng trắng khi so sánh.
- `-r`: So sánh các thư mục một cách đệ quy.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `diff`:

1. So sánh hai tệp văn bản:
   ```bash
   diff file1.txt file2.txt
   ```

2. So sánh hai tệp với định dạng unified:
   ```bash
   diff -u file1.txt file2.txt
   ```

3. So sánh hai thư mục:
   ```bash
   diff -r dir1/ dir2/
   ```

4. So sánh hai tệp mà không phân biệt chữ hoa và chữ thường:
   ```bash
   diff -i file1.txt file2.txt
   ```

## Tips
- Sử dụng tùy chọn `-u` để có kết quả dễ đọc hơn, đặc biệt khi xem xét các thay đổi lớn.
- Khi so sánh thư mục, hãy luôn sử dụng tùy chọn `-r` để đảm bảo rằng tất cả các tệp con cũng được so sánh.
- Kiểm tra các tệp tạm thời hoặc bản sao lưu trước khi thực hiện các thay đổi lớn để tránh mất dữ liệu.