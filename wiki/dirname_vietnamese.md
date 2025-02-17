# [Linux] Bash dirname Cách sử dụng: Lấy đường dẫn thư mục của tệp

## Overview
Lệnh `dirname` trong Bash được sử dụng để trích xuất đường dẫn thư mục của một tệp hoặc thư mục. Nó giúp bạn lấy phần đường dẫn mà không bao gồm tên tệp, rất hữu ích trong các kịch bản tự động hóa hoặc khi bạn cần làm việc với đường dẫn.

## Usage
Cú pháp cơ bản của lệnh `dirname` như sau:
```
dirname [options] [arguments]
```

## Common Options
- `-z`: Xuất kết quả với ký tự phân cách null, hữu ích cho việc xử lý đường dẫn có khoảng trắng.
- `--help`: Hiển thị thông tin trợ giúp về lệnh `dirname`.
- `--version`: Hiển thị phiên bản của lệnh `dirname`.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `dirname`:

1. **Lấy đường dẫn thư mục của một tệp:**
   ```bash
   dirname /home/user/documents/file.txt
   ```
   Kết quả: `/home/user/documents`

2. **Lấy đường dẫn thư mục của một tệp có khoảng trắng trong tên:**
   ```bash
   dirname "/home/user/my documents/file.txt"
   ```
   Kết quả: `/home/user/my documents`

3. **Sử dụng với nhiều tệp:**
   ```bash
   dirname /home/user/documents/file1.txt /home/user/documents/file2.txt
   ```
   Kết quả: 
   ```
   /home/user/documents
   /home/user/documents
   ```

4. **Kết hợp với lệnh khác:**
   ```bash
   dirname $(pwd)/file.txt
   ```
   Kết quả: `/home/user/current_directory` (giả sử bạn đang ở thư mục `current_directory`).

## Tips
- Sử dụng `dirname` trong các kịch bản để tự động hóa việc xử lý đường dẫn.
- Kết hợp với `basename` để có được cả đường dẫn và tên tệp trong cùng một kịch bản.
- Hãy nhớ sử dụng dấu nháy kép khi đường dẫn có khoảng trắng để tránh lỗi.