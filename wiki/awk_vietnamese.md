# [리눅스] Bash awk 사용법

## Tổng quan
`awk` là một ngôn ngữ lập trình mạnh mẽ được sử dụng chủ yếu để xử lý và phân tích dữ liệu văn bản. Nó cho phép người dùng thực hiện các tác vụ như lọc, định dạng và tính toán trên các dòng văn bản. `awk` rất hữu ích trong việc xử lý các tệp văn bản có cấu trúc, chẳng hạn như tệp CSV hoặc tệp log, giúp trích xuất thông tin cần thiết một cách nhanh chóng và hiệu quả.

## Cách sử dụng
Cú pháp cơ bản của lệnh `awk` như sau:

```bash
awk 'pattern { action }' file
```

- `pattern`: Điều kiện để xác định các dòng nào sẽ được xử lý. Nếu không có điều kiện, tất cả các dòng sẽ được xử lý.
- `action`: Các hành động sẽ được thực hiện trên các dòng khớp với điều kiện. Nếu không có hành động, `awk` sẽ in ra các dòng khớp.

### Tùy chọn phổ biến
- `-F`: Xác định ký tự phân cách (delimiter) cho các trường. Ví dụ: `-F,` để sử dụng dấu phẩy.
- `-v`: Gán giá trị cho biến trong `awk`. Ví dụ: `-v var=value`.
- `-f`: Chỉ định tệp chứa mã `awk` để thực thi.

## Ví dụ
### Ví dụ 1: In ra cột thứ hai của tệp
Giả sử bạn có một tệp `data.txt` với nội dung như sau:

```
John,25
Jane,30
Doe,22
```

Bạn có thể sử dụng lệnh sau để in ra cột thứ hai:

```bash
awk -F, '{ print $2 }' data.txt
```

Kết quả sẽ là:

```
25
30
22
```

### Ví dụ 2: Tính tổng giá trị trong cột thứ hai
Nếu bạn muốn tính tổng giá trị trong cột thứ hai, bạn có thể sử dụng lệnh sau:

```bash
awk -F, '{ sum += $2 } END { print sum }' data.txt
```

Kết quả sẽ là:

```
77
```

## Mẹo
- Sử dụng `-F` để chỉ định ký tự phân cách phù hợp với định dạng tệp của bạn, điều này sẽ giúp `awk` phân tích dữ liệu chính xác hơn.
- Khi làm việc với các tệp lớn, hãy cân nhắc sử dụng `awk` trong các ống (pipes) để xử lý dữ liệu theo từng bước, giúp tiết kiệm bộ nhớ.
- Tận dụng khả năng của `awk` để viết các script phức tạp hơn cho các tác vụ tự động hóa, giúp tiết kiệm thời gian và công sức trong công việc hàng ngày.