# [리눅스] Bash readarray 사용법

## Tổng quan
Lệnh `readarray` trong Bash được sử dụng để đọc dữ liệu từ một tệp hoặc đầu vào tiêu chuẩn và lưu trữ chúng vào một mảng. Mỗi dòng trong tệp hoặc đầu vào sẽ trở thành một phần tử trong mảng, giúp cho việc xử lý dữ liệu dòng dễ dàng hơn trong các kịch bản lập trình shell.

## Cú pháp
Cú pháp cơ bản của lệnh `readarray` như sau:

```bash
readarray [options] array_name
```

### Tùy chọn phổ biến
- `-t`: Loại bỏ ký tự newline (`\n`) ở cuối mỗi dòng khi lưu vào mảng.
- `-n N`: Chỉ đọc N dòng đầu tiên từ đầu vào.
- `-s N`: Bỏ qua N dòng đầu tiên trong đầu vào.

## Ví dụ
### Ví dụ 1: Đọc từ tệp
Giả sử bạn có một tệp tên là `data.txt` với nội dung như sau:

```
line 1
line 2
line 3
```

Bạn có thể sử dụng `readarray` để đọc nội dung của tệp này vào một mảng:

```bash
readarray lines < data.txt
echo "${lines[0]}"  # Xuất ra: line 1
echo "${lines[1]}"  # Xuất ra: line 2
```

### Ví dụ 2: Đọc từ đầu vào tiêu chuẩn
Bạn cũng có thể sử dụng `readarray` để đọc dữ liệu từ đầu vào tiêu chuẩn. Ví dụ:

```bash
echo -e "apple\nbanana\ncherry" | readarray -t fruits
echo "${fruits[0]}"  # Xuất ra: apple
echo "${fruits[1]}"  # Xuất ra: banana
```

## Mẹo
- Sử dụng tùy chọn `-t` để loại bỏ ký tự newline, điều này sẽ giúp bạn dễ dàng xử lý các phần tử trong mảng mà không cần phải cắt bỏ ký tự này sau khi đọc.
- Nếu bạn chỉ cần một số dòng nhất định từ đầu vào, hãy kết hợp các tùy chọn `-n` và `-s` để kiểm soát số lượng dòng được đọc.
- Đảm bảo rằng tên mảng không trùng với các biến khác trong script của bạn để tránh xung đột.