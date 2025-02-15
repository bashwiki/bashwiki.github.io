# [리눅스] Bash rev 사용법

## Tổng quan
Lệnh `rev` trong Bash được sử dụng để đảo ngược các ký tự trong mỗi dòng của đầu vào. Điều này có nghĩa là nếu bạn có một chuỗi văn bản, lệnh `rev` sẽ thay đổi thứ tự các ký tự trong từng dòng, giúp bạn dễ dàng thực hiện các tác vụ liên quan đến việc xử lý chuỗi.

## Cú pháp
Cú pháp cơ bản của lệnh `rev` như sau:

```bash
rev [tùy chọn] [tệp]
```

### Tùy chọn phổ biến
- `-` : Đọc từ đầu vào chuẩn (stdin) thay vì từ một tệp.
- `tệp` : Tên tệp mà bạn muốn đảo ngược nội dung.

## Ví dụ
### Ví dụ 1: Đảo ngược một chuỗi văn bản từ đầu vào
Bạn có thể sử dụng lệnh `rev` để đảo ngược một chuỗi văn bản nhập từ bàn phím như sau:

```bash
echo "Hello World" | rev
```
Kết quả sẽ là:
```
dlroW olleH
```

### Ví dụ 2: Đảo ngược nội dung trong một tệp
Giả sử bạn có một tệp tên là `example.txt` với nội dung như sau:
```
Hello
World
```
Bạn có thể đảo ngược nội dung của tệp này bằng lệnh:

```bash
rev example.txt
```
Kết quả sẽ là:
```
olleH
dlroW
```

## Mẹo
- Sử dụng `rev` kết hợp với các lệnh khác trong Bash để thực hiện các tác vụ phức tạp hơn. Ví dụ, bạn có thể sử dụng `cat` để đọc nhiều tệp và sau đó áp dụng `rev` để đảo ngược nội dung của chúng.
- Hãy cẩn thận khi sử dụng lệnh `rev` trên các tệp lớn, vì việc đảo ngược nội dung có thể tốn thời gian và tài nguyên hệ thống.