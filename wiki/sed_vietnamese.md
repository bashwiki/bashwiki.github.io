# [Linux] Bash sed cách sử dụng: Thay thế và xử lý văn bản

## Tổng quan
Lệnh `sed` (stream editor) là một công cụ mạnh mẽ trong Bash, được sử dụng để xử lý và biến đổi văn bản trong các tệp hoặc đầu ra của các lệnh khác. Nó cho phép bạn thực hiện các thao tác như thay thế, xóa, và chèn văn bản một cách tự động.

## Cách sử dụng
Cú pháp cơ bản của lệnh `sed` như sau:
```bash
sed [options] [arguments]
```

## Các tùy chọn phổ biến
- `-e`: Chỉ định một lệnh để thực hiện.
- `-i`: Thay đổi tệp gốc mà không tạo tệp mới.
- `-n`: Ngăn không cho `sed` in ra tất cả các dòng, chỉ in những dòng được chỉ định bởi lệnh.
- `s/pattern/replacement/`: Thay thế `pattern` bằng `replacement`.

## Ví dụ thường gặp
1. **Thay thế một chuỗi trong tệp**:
   ```bash
   sed 's/old/new/g' filename.txt
   ```
   Lệnh này sẽ thay thế tất cả các từ "old" bằng "new" trong tệp `filename.txt`.

2. **Thay thế và lưu vào tệp gốc**:
   ```bash
   sed -i 's/old/new/g' filename.txt
   ```
   Lệnh này sẽ thực hiện thay thế và lưu trực tiếp vào tệp `filename.txt`.

3. **In ra các dòng chứa một từ cụ thể**:
   ```bash
   sed -n '/pattern/p' filename.txt
   ```
   Lệnh này sẽ chỉ in ra các dòng trong `filename.txt` chứa từ "pattern".

4. **Xóa các dòng chứa một từ cụ thể**:
   ```bash
   sed '/pattern/d' filename.txt
   ```
   Lệnh này sẽ xóa tất cả các dòng chứa "pattern" trong `filename.txt`.

## Mẹo
- Sử dụng tùy chọn `-i` cẩn thận, vì nó sẽ thay đổi tệp gốc mà không có bản sao lưu.
- Bạn có thể sử dụng nhiều lệnh `sed` bằng cách thêm nhiều `-e`:
  ```bash
  sed -e 's/old/new/g' -e 's/another/replace/g' filename.txt
  ```
- Để kiểm tra kết quả trước khi thay đổi, hãy bỏ tùy chọn `-i` để xem đầu ra trên màn hình.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `sed` trong Bash!