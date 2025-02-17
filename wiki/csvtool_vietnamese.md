# [Linux] Bash csvtool Cách sử dụng: Công cụ xử lý tệp CSV

## Tổng quan
Lệnh `csvtool` là một công cụ mạnh mẽ dùng để xử lý và thao tác với các tệp CSV (Comma-Separated Values). Nó cho phép người dùng thực hiện các thao tác như trích xuất, lọc và định dạng dữ liệu từ các tệp CSV một cách dễ dàng.

## Cách sử dụng
Cú pháp cơ bản của lệnh `csvtool` như sau:
```bash
csvtool [options] [arguments]
```

## Các tùy chọn phổ biến
- `cut`: Chọn các cột cụ thể từ tệp CSV.
- `format`: Định dạng lại dữ liệu trong tệp CSV.
- `head`: Hiển thị một số dòng đầu tiên của tệp CSV.
- `tail`: Hiển thị một số dòng cuối cùng của tệp CSV.
- `csv2tab`: Chuyển đổi tệp CSV sang định dạng bảng.

## Ví dụ phổ biến
1. **Cắt cột từ tệp CSV:**
   ```bash
   csvtool cut -c 1,3 data.csv
   ```
   Lệnh này sẽ trích xuất cột 1 và cột 3 từ tệp `data.csv`.

2. **Hiển thị 5 dòng đầu tiên của tệp CSV:**
   ```bash
   csvtool head -n 5 data.csv
   ```
   Lệnh này sẽ hiển thị 5 dòng đầu tiên của tệp `data.csv`.

3. **Chuyển đổi tệp CSV sang định dạng bảng:**
   ```bash
   csvtool csv2tab data.csv > data.tsv
   ```
   Lệnh này sẽ chuyển đổi tệp `data.csv` sang tệp `data.tsv` với định dạng bảng.

4. **Định dạng lại dữ liệu:**
   ```bash
   csvtool format '%s\t%s\n' data.csv
   ```
   Lệnh này sẽ định dạng lại dữ liệu trong `data.csv` với các trường được phân cách bằng tab.

## Mẹo
- Khi sử dụng `csvtool`, hãy chắc chắn rằng tệp CSV của bạn được định dạng đúng để tránh lỗi trong quá trình xử lý.
- Sử dụng tùy chọn `--help` để xem danh sách đầy đủ các tùy chọn và cú pháp của lệnh.
- Thực hiện các thao tác trên một bản sao của tệp CSV để tránh mất dữ liệu quan trọng.