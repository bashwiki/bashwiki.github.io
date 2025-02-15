# [리눅스] Bash diff 사용법

## Tổng quan
Lệnh `diff` trong Bash được sử dụng để so sánh nội dung của hai tệp tin hoặc hai thư mục. Mục đích chính của lệnh này là xác định sự khác biệt giữa hai tệp, giúp người dùng dễ dàng nhận diện các thay đổi, bổ sung hoặc xóa bỏ trong nội dung của chúng. Lệnh `diff` thường được sử dụng trong phát triển phần mềm để theo dõi các thay đổi trong mã nguồn.

## Cách sử dụng
Cú pháp cơ bản của lệnh `diff` như sau:

```bash
diff [tùy chọn] tệp1 tệp2
```

### Các tùy chọn phổ biến:
- `-u`: Hiển thị sự khác biệt theo định dạng "unified", giúp dễ đọc hơn.
- `-i`: Bỏ qua sự khác biệt về chữ hoa và chữ thường.
- `-w`: Bỏ qua sự khác biệt về khoảng trắng.
- `-r`: So sánh hai thư mục và hiển thị sự khác biệt giữa các tệp trong thư mục đó.

## Ví dụ
### Ví dụ 1: So sánh hai tệp tin
Giả sử bạn có hai tệp tin `file1.txt` và `file2.txt`, bạn có thể sử dụng lệnh sau để so sánh chúng:

```bash
diff file1.txt file2.txt
```

Kết quả sẽ hiển thị các dòng khác nhau giữa hai tệp tin.

### Ví dụ 2: So sánh hai thư mục
Nếu bạn muốn so sánh nội dung của hai thư mục `dir1` và `dir2`, bạn có thể sử dụng:

```bash
diff -r dir1 dir2
```

Lệnh này sẽ hiển thị tất cả các sự khác biệt giữa các tệp trong hai thư mục.

## Mẹo
- Khi làm việc với các tệp lớn, hãy sử dụng tùy chọn `-u` để có cái nhìn tổng quát hơn về sự khác biệt.
- Nếu bạn chỉ quan tâm đến sự khác biệt về nội dung mà không cần quan tâm đến khoảng trắng hoặc chữ hoa, hãy sử dụng các tùy chọn `-w` và `-i`.
- Để lưu kết quả của lệnh `diff` vào một tệp tin, bạn có thể sử dụng dấu chuyển hướng `>`:

```bash
diff file1.txt file2.txt > differences.txt
```

Điều này sẽ giúp bạn lưu lại các khác biệt để tham khảo sau này.