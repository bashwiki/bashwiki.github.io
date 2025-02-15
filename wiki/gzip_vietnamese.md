# [리눅스] Bash gzip 사용법

## Tổng quan
`gzip` là một công cụ nén tệp trong môi trường Unix/Linux, được sử dụng để giảm kích thước của các tệp bằng cách sử dụng thuật toán nén DEFLATE. Mục đích chính của `gzip` là tiết kiệm không gian lưu trữ và giảm thời gian truyền tải tệp qua mạng. Khi nén, `gzip` tạo ra các tệp có phần mở rộng `.gz`.

## Cách sử dụng
Cú pháp cơ bản của lệnh `gzip` như sau:

```bash
gzip [tùy chọn] [tệp]
```

### Các tùy chọn phổ biến:
- `-d`, `--decompress`: Giải nén tệp `.gz`.
- `-k`, `--keep`: Giữ lại tệp gốc sau khi nén.
- `-v`, `--verbose`: Hiển thị thông tin chi tiết về quá trình nén.
- `-r`, `--recursive`: Nén tất cả các tệp trong thư mục con.

## Ví dụ
### Ví dụ 1: Nén một tệp
Để nén một tệp có tên `file.txt`, bạn có thể sử dụng lệnh sau:

```bash
gzip file.txt
```
Sau khi thực hiện lệnh này, tệp `file.txt` sẽ được nén và tạo ra tệp `file.txt.gz`.

### Ví dụ 2: Giải nén một tệp
Để giải nén tệp `file.txt.gz`, bạn có thể sử dụng lệnh sau:

```bash
gzip -d file.txt.gz
```
Lệnh này sẽ khôi phục lại tệp gốc `file.txt`.

## Mẹo
- Sử dụng tùy chọn `-k` nếu bạn muốn giữ lại tệp gốc sau khi nén. Ví dụ: `gzip -k file.txt`.
- Để nén tất cả các tệp trong một thư mục, bạn có thể sử dụng tùy chọn `-r`: `gzip -r /path/to/directory`.
- Kiểm tra kích thước tệp trước và sau khi nén để đánh giá hiệu quả nén bằng cách sử dụng lệnh `ls -lh`.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `gzip` trong Bash!