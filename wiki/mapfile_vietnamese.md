# [Linux] Bash mapfile: Đọc nội dung tệp vào mảng

## Overview
Lệnh `mapfile` trong Bash được sử dụng để đọc nội dung của một tệp và lưu từng dòng vào một mảng. Điều này rất hữu ích khi bạn muốn xử lý dữ liệu từ tệp mà không cần phải đọc từng dòng một cách thủ công.

## Usage
Cú pháp cơ bản của lệnh `mapfile` như sau:

```bash
mapfile [options] [arguments]
```

## Common Options
- `-n N`: Chỉ đọc N dòng từ tệp.
- `-s N`: Bỏ qua N dòng đầu tiên trong tệp.
- `-t`: Bỏ qua ký tự xuống dòng ở cuối mỗi dòng.

## Common Examples
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `mapfile`.

### Ví dụ 1: Đọc toàn bộ tệp vào mảng
```bash
mapfile my_array < filename.txt
```
Lệnh này sẽ đọc tất cả các dòng từ `filename.txt` và lưu vào mảng `my_array`.

### Ví dụ 2: Đọc một số dòng nhất định
```bash
mapfile -n 5 my_array < filename.txt
```
Lệnh này sẽ chỉ đọc 5 dòng đầu tiên từ `filename.txt` vào mảng `my_array`.

### Ví dụ 3: Bỏ qua một số dòng đầu
```bash
mapfile -s 2 my_array < filename.txt
```
Lệnh này sẽ bỏ qua 2 dòng đầu tiên trong `filename.txt` và đọc các dòng còn lại vào mảng `my_array`.

### Ví dụ 4: Bỏ qua ký tự xuống dòng
```bash
mapfile -t my_array < filename.txt
```
Lệnh này sẽ đọc nội dung từ `filename.txt` vào mảng `my_array` mà không có ký tự xuống dòng ở cuối mỗi dòng.

## Tips
- Khi sử dụng `mapfile`, hãy chắc chắn rằng tệp bạn đang đọc có định dạng phù hợp để tránh lỗi.
- Sử dụng tùy chọn `-t` nếu bạn muốn loại bỏ ký tự xuống dòng, giúp bạn dễ dàng xử lý dữ liệu hơn.
- Kiểm tra kích thước của mảng sau khi sử dụng `mapfile` để đảm bảo rằng bạn đã đọc đúng số dòng mong muốn.