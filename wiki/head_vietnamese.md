# [리눅스] Bash head 사용법

## Tổng quan
Lệnh `head` trong Bash được sử dụng để hiển thị một số dòng đầu tiên của một tệp tin. Lệnh này rất hữu ích khi bạn chỉ muốn xem một phần nhỏ của nội dung tệp mà không cần mở toàn bộ tệp, giúp tiết kiệm thời gian và tài nguyên.

## Cú pháp
Cú pháp cơ bản của lệnh `head` như sau:

```bash
head [tùy chọn] [tệp tin]
```

### Các tùy chọn phổ biến
- `-n [số]`: Chỉ định số dòng bạn muốn hiển thị. Mặc định, `head` sẽ hiển thị 10 dòng đầu tiên.
- `-c [số]`: Hiển thị số byte đầu tiên thay vì số dòng.
- `-q`: Không hiển thị tên tệp tin khi hiển thị nhiều tệp.
- `-v`: Luôn hiển thị tên tệp tin trước khi hiển thị nội dung.

## Ví dụ
### Ví dụ 1: Hiển thị 10 dòng đầu tiên của một tệp
```bash
head myfile.txt
```
Lệnh trên sẽ hiển thị 10 dòng đầu tiên của tệp `myfile.txt`.

### Ví dụ 2: Hiển thị 5 dòng đầu tiên của một tệp
```bash
head -n 5 myfile.txt
```
Lệnh này sẽ hiển thị 5 dòng đầu tiên của tệp `myfile.txt`.

### Ví dụ 3: Hiển thị 20 byte đầu tiên của một tệp
```bash
head -c 20 myfile.txt
```
Lệnh này sẽ hiển thị 20 byte đầu tiên của tệp `myfile.txt`.

## Mẹo
- Sử dụng `head` kết hợp với các lệnh khác như `grep` hoặc `less` để lọc và xem nội dung tệp một cách hiệu quả hơn.
- Nếu bạn làm việc với nhiều tệp, bạn có thể chỉ định nhiều tệp trong cùng một lệnh `head` để xem nội dung của từng tệp một cách nhanh chóng.
- Để dễ dàng theo dõi và kiểm tra các tệp log lớn, bạn có thể sử dụng `head` để xem các dòng đầu tiên mà không cần mở toàn bộ tệp.