# [Linux] Bash gzip Cách sử dụng: Nén và giải nén tệp tin

## Overview
Lệnh `gzip` là một công cụ nén tệp tin trong hệ điều hành Unix và Linux. Nó giúp giảm kích thước của các tệp tin bằng cách sử dụng thuật toán nén, giúp tiết kiệm không gian lưu trữ và tăng tốc độ truyền tải dữ liệu.

## Usage
Cú pháp cơ bản của lệnh `gzip` như sau:

```
gzip [options] [arguments]
```

## Common Options
- `-d`, `--decompress`: Giải nén tệp tin.
- `-k`, `--keep`: Giữ lại tệp tin gốc sau khi nén.
- `-v`, `--verbose`: Hiển thị thông tin chi tiết về quá trình nén hoặc giải nén.
- `-r`, `--recursive`: Nén hoặc giải nén các tệp tin trong thư mục con.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `gzip`:

1. Nén một tệp tin:
   ```bash
   gzip file.txt
   ```

2. Giải nén một tệp tin đã nén:
   ```bash
   gzip -d file.txt.gz
   ```

3. Nén một tệp tin mà không xóa tệp gốc:
   ```bash
   gzip -k file.txt
   ```

4. Nén tất cả các tệp tin trong thư mục hiện tại:
   ```bash
   gzip *.txt
   ```

5. Giải nén tất cả các tệp tin `.gz` trong thư mục:
   ```bash
   gzip -d *.gz
   ```

## Tips
- Luôn kiểm tra kích thước tệp tin sau khi nén để đảm bảo rằng quá trình nén đã thành công.
- Sử dụng tùy chọn `-v` để theo dõi tiến trình nén hoặc giải nén, đặc biệt khi làm việc với nhiều tệp tin.
- Khi nén nhiều tệp tin, hãy cân nhắc sử dụng `tar` kết hợp với `gzip` để tạo ra một tệp tin nén duy nhất.