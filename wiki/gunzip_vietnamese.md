# [Linux] Bash gunzip Cách sử dụng: Giải nén tệp tin nén

## Overview
Lệnh `gunzip` được sử dụng để giải nén các tệp tin nén có định dạng `.gz`. Đây là một công cụ hữu ích trong việc quản lý và tiết kiệm dung lượng lưu trữ cho các tệp tin lớn.

## Usage
Cú pháp cơ bản của lệnh `gunzip` như sau:
```
gunzip [options] [arguments]
```

## Common Options
- `-c`: Giải nén tệp tin và xuất kết quả ra stdout (màn hình).
- `-f`: Buộc giải nén, ghi đè lên các tệp tin đã tồn tại.
- `-k`: Giữ lại tệp tin nén gốc sau khi giải nén.
- `-r`: Giải nén tệp tin trong thư mục và các thư mục con.

## Common Examples
- Giải nén một tệp tin đơn giản:
  ```bash
  gunzip file.txt.gz
  ```

- Giải nén và giữ lại tệp tin nén:
  ```bash
  gunzip -k file.txt.gz
  ```

- Giải nén tất cả các tệp tin nén trong thư mục hiện tại:
  ```bash
  gunzip *.gz
  ```

- Giải nén tệp tin và xuất ra stdout:
  ```bash
  gunzip -c file.txt.gz > file.txt
  ```

## Tips
- Luôn kiểm tra dung lượng ổ đĩa trước khi giải nén các tệp tin lớn để tránh tình trạng đầy ổ đĩa.
- Sử dụng tùy chọn `-k` nếu bạn muốn giữ lại tệp tin nén gốc cho các mục đích sao lưu.
- Kết hợp `gunzip` với các lệnh khác trong một chuỗi để tự động hóa quy trình xử lý tệp tin.