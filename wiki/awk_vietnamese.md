# [Linux] Bash awk cách sử dụng: Trình xử lý văn bản mạnh mẽ

## Tổng quan
`awk` là một công cụ mạnh mẽ trong Bash dùng để xử lý và phân tích văn bản. Nó cho phép người dùng thực hiện các thao tác trên các dòng văn bản, như lọc, định dạng và tính toán, dựa trên các mẫu và điều kiện đã chỉ định.

## Cách sử dụng
Cú pháp cơ bản của lệnh `awk` như sau:
```bash
awk [options] [arguments]
```

## Các tùy chọn phổ biến
- `-F`: Chỉ định ký tự phân cách (delimiter) giữa các trường.
- `-v`: Đặt giá trị cho biến trước khi thực thi.
- `-f`: Chạy một tập tin chứa mã `awk`.
- `-e`: Chạy mã `awk` từ dòng lệnh.

## Ví dụ phổ biến
1. **In toàn bộ nội dung của một tệp:**
   ```bash
   awk '{print}' filename.txt
   ```

2. **Lọc các dòng chứa từ khóa cụ thể:**
   ```bash
   awk '/keyword/' filename.txt
   ```

3. **Tính tổng của một cột số:**
   ```bash
   awk '{sum += $1} END {print sum}' filename.txt
   ```

4. **Chỉ định ký tự phân cách và in cột thứ hai:**
   ```bash
   awk -F, '{print $2}' filename.csv
   ```

5. **Sử dụng biến để đếm số dòng:**
   ```bash
   awk -v count=0 '{count++} END {print count}' filename.txt
   ```

## Mẹo
- Sử dụng `-F` để dễ dàng làm việc với các tệp CSV hoặc TSV.
- Kết hợp `awk` với các lệnh khác như `grep` hoặc `sort` để tăng cường khả năng xử lý dữ liệu.
- Thực hành viết các đoạn mã `awk` trong tệp riêng để dễ dàng quản lý và tái sử dụng.