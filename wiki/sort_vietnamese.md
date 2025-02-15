# [리눅스] Bash sort 사용법

## Tổng quan
Lệnh `sort` trong Bash được sử dụng để sắp xếp các dòng trong một tệp hoặc đầu vào từ dòng lệnh theo thứ tự nhất định. Mục đích chính của lệnh này là giúp người dùng dễ dàng tổ chức và tìm kiếm dữ liệu trong các tệp văn bản bằng cách sắp xếp chúng theo thứ tự tăng dần hoặc giảm dần.

## Cú pháp
Cú pháp cơ bản của lệnh `sort` như sau:

```bash
sort [tùy chọn] [tệp]
```

### Tùy chọn phổ biến
- `-r`: Sắp xếp theo thứ tự giảm dần.
- `-n`: Sắp xếp theo giá trị số (sử dụng cho các số thay vì chuỗi).
- `-k`: Chỉ định cột để sắp xếp (ví dụ: `-k 2` sẽ sắp xếp theo cột thứ hai).
- `-u`: Chỉ hiển thị các dòng duy nhất (loại bỏ các dòng trùng lặp).
- `-o`: Ghi kết quả vào tệp (ví dụ: `-o output.txt`).

## Ví dụ
### Ví dụ 1: Sắp xếp các dòng trong một tệp
Giả sử bạn có một tệp tên là `data.txt` chứa các dòng văn bản. Để sắp xếp các dòng này theo thứ tự tăng dần, bạn có thể sử dụng lệnh sau:

```bash
sort data.txt
```

### Ví dụ 2: Sắp xếp theo thứ tự giảm dần
Nếu bạn muốn sắp xếp các dòng trong tệp `data.txt` theo thứ tự giảm dần, bạn có thể sử dụng tùy chọn `-r` như sau:

```bash
sort -r data.txt
```

## Mẹo
- Khi làm việc với các tệp lớn, bạn có thể kết hợp lệnh `sort` với `uniq` để loại bỏ các dòng trùng lặp sau khi sắp xếp, như sau:

```bash
sort data.txt | uniq
```

- Để sắp xếp theo giá trị số, hãy đảm bảo sử dụng tùy chọn `-n` để tránh việc sắp xếp theo chuỗi, điều này có thể dẫn đến kết quả không như mong muốn:

```bash
sort -n numbers.txt
```

Sử dụng lệnh `sort` một cách hiệu quả sẽ giúp bạn quản lý và phân tích dữ liệu tốt hơn trong các tệp văn bản.