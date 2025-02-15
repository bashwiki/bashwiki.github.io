# [리눅스] Bash cat 사용법

## Tổng quan
Lệnh `cat` (viết tắt của "concatenate") là một công cụ trong Bash được sử dụng để hiển thị nội dung của một hoặc nhiều tệp tin trên dòng lệnh. Lệnh này rất hữu ích cho việc đọc nội dung tệp, kết hợp nhiều tệp lại với nhau, và tạo ra các tệp mới từ nội dung của các tệp khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `cat` như sau:

```bash
cat [tùy chọn] [tệp tin...]
```

Một số tùy chọn phổ biến của lệnh `cat` bao gồm:

- `-n`: Đánh số dòng cho đầu ra.
- `-b`: Đánh số dòng không trống cho đầu ra.
- `-E`: Hiển thị ký tự kết thúc dòng (dấu `$`).
- `-s`: Giảm thiểu các dòng trống liên tiếp xuống chỉ còn một dòng trống.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `cat`:

1. Hiển thị nội dung của một tệp tin:

```bash
cat file.txt
```

2. Kết hợp nội dung của hai tệp tin và hiển thị ra màn hình:

```bash
cat file1.txt file2.txt
```

3. Tạo một tệp tin mới từ nội dung của một tệp tin khác và đánh số dòng:

```bash
cat -n file.txt > newfile.txt
```

## Mẹo
- Sử dụng `cat` kết hợp với các lệnh khác qua ống dẫn (pipe) để xử lý dữ liệu. Ví dụ, bạn có thể sử dụng `cat` với `grep` để tìm kiếm nội dung trong tệp:
  
  ```bash
  cat file.txt | grep "từ khóa"
  ```

- Tránh sử dụng `cat` để đọc các tệp tin lớn, vì nó có thể làm chậm hệ thống. Thay vào đó, hãy sử dụng lệnh `less` hoặc `more` để xem nội dung tệp một cách hiệu quả hơn.

- Khi kết hợp nhiều tệp tin, hãy chắc chắn rằng bạn đã kiểm tra thứ tự và nội dung của các tệp để tránh nhầm lẫn trong kết quả đầu ra.