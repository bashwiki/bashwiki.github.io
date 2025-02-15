# [리눅스] Bash dirname 사용법

## Tổng quan
Lệnh `dirname` trong Bash được sử dụng để trích xuất phần thư mục của một đường dẫn tệp. Mục đích chính của lệnh này là giúp người dùng lấy được đường dẫn thư mục mà không cần phải xử lý thủ công. Điều này rất hữu ích khi bạn cần làm việc với các tệp và thư mục trong các kịch bản tự động hóa hoặc khi lập trình.

## Cách sử dụng
Cú pháp cơ bản của lệnh `dirname` như sau:

```bash
dirname [đường_dẫn_tệp]
```

Trong đó, `[đường_dẫn_tệp]` là đường dẫn đầy đủ đến tệp mà bạn muốn lấy phần thư mục. Lệnh này không có nhiều tùy chọn, nhưng bạn có thể sử dụng nó trong các kịch bản khác nhau để xử lý nhiều đường dẫn cùng một lúc.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `dirname`.

### Ví dụ 1: Lấy thư mục từ đường dẫn tệp
```bash
$ dirname /home/user/documents/file.txt
/home/user/documents
```
Trong ví dụ này, lệnh `dirname` trả về `/home/user/documents`, đó là phần thư mục của đường dẫn tệp đã cho.

### Ví dụ 2: Sử dụng với biến
```bash
$ FILE_PATH="/home/user/pictures/photo.jpg"
$ dirname "$FILE_PATH"
/home/user/pictures
```
Ở đây, chúng ta sử dụng biến `FILE_PATH` để chứa đường dẫn tệp và sau đó sử dụng `dirname` để lấy phần thư mục.

## Mẹo
- Khi làm việc với nhiều đường dẫn, bạn có thể sử dụng vòng lặp để áp dụng lệnh `dirname` cho từng đường dẫn trong một danh sách.
- Hãy nhớ rằng `dirname` sẽ trả về một chuỗi trống nếu đường dẫn tệp không chứa thư mục (ví dụ: nếu bạn chỉ cung cấp tên tệp mà không có đường dẫn).
- Nếu bạn cần làm việc với các tệp trong một thư mục cụ thể, hãy kết hợp `dirname` với các lệnh khác như `find` hoặc `xargs` để xử lý hàng loạt.

Lệnh `dirname` là một công cụ đơn giản nhưng mạnh mẽ trong Bash, giúp bạn dễ dàng quản lý và xử lý các đường dẫn tệp.