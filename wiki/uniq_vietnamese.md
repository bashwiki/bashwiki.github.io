# [리눅스] Bash uniq 사용법

## Tổng quan
Lệnh `uniq` trong Bash được sử dụng để loại bỏ các dòng trùng lặp trong một tệp hoặc đầu ra của một lệnh. Mục đích chính của `uniq` là giúp người dùng dễ dàng xử lý và phân tích dữ liệu bằng cách chỉ giữ lại các dòng duy nhất. Lệnh này thường được sử dụng kết hợp với lệnh `sort`, vì `uniq` chỉ loại bỏ các dòng trùng lặp liên tiếp.

## Cú pháp
Cú pháp cơ bản của lệnh `uniq` như sau:

```bash
uniq [tùy chọn] [tệp]
```

### Các tùy chọn phổ biến:
- `-c`: Đếm số lần xuất hiện của mỗi dòng và hiển thị số đó trước dòng.
- `-d`: Chỉ hiển thị các dòng trùng lặp.
- `-u`: Chỉ hiển thị các dòng duy nhất (không trùng lặp).
- `-i`: Bỏ qua sự khác biệt về chữ hoa và chữ thường khi so sánh các dòng.

## Ví dụ
### Ví dụ 1: Loại bỏ các dòng trùng lặp
Giả sử bạn có một tệp có tên `data.txt` với nội dung sau:

```
apple
banana
apple
orange
banana
```

Bạn có thể sử dụng lệnh `uniq` để loại bỏ các dòng trùng lặp như sau:

```bash
sort data.txt | uniq
```

Kết quả sẽ là:

```
apple
banana
orange
```

### Ví dụ 2: Đếm số lần xuất hiện của mỗi dòng
Nếu bạn muốn đếm số lần xuất hiện của mỗi dòng trong tệp `data.txt`, bạn có thể sử dụng tùy chọn `-c`:

```bash
sort data.txt | uniq -c
```

Kết quả sẽ là:

```
      2 apple
      2 banana
      1 orange
```

## Mẹo
- Luôn sử dụng `sort` trước khi sử dụng `uniq` để đảm bảo rằng các dòng trùng lặp được đặt cạnh nhau, vì `uniq` chỉ loại bỏ các dòng trùng lặp liên tiếp.
- Sử dụng tùy chọn `-i` nếu bạn muốn so sánh các dòng mà không phân biệt chữ hoa và chữ thường.
- Khi làm việc với các tệp lớn, hãy xem xét việc sử dụng `uniq` trong các ống lệnh để tiết kiệm bộ nhớ và thời gian xử lý.