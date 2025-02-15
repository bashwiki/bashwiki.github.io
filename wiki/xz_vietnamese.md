# [리눅스] Bash xz 사용법

## Tổng quan
Lệnh `xz` là một công cụ nén dữ liệu trong hệ điều hành Unix/Linux, được sử dụng để nén và giải nén các tệp tin. Nó sử dụng thuật toán nén LZMA (Lempel-Ziv-Markov chain algorithm), cho phép nén tệp tin với tỷ lệ nén cao hơn so với nhiều công cụ nén khác như `gzip` hay `bzip2`. Mục đích chính của lệnh `xz` là giảm kích thước tệp tin để tiết kiệm không gian lưu trữ và băng thông khi truyền tải.

## Cách sử dụng
Cú pháp cơ bản của lệnh `xz` như sau:

```bash
xz [tùy chọn] [tệp tin]
```

### Một số tùy chọn phổ biến:
- `-d`, `--decompress`: Giải nén tệp tin đã nén.
- `-k`, `--keep`: Giữ lại tệp tin gốc sau khi nén.
- `-v`, `--verbose`: Hiển thị thông tin chi tiết trong quá trình nén hoặc giải nén.
- `-f`, `--force`: Buộc ghi đè lên tệp tin đã tồn tại.
- `-9`: Sử dụng mức nén cao nhất (mức 1 đến 9, 9 là cao nhất).

## Ví dụ
### Ví dụ 1: Nén một tệp tin
Để nén một tệp tin có tên `file.txt`, bạn có thể sử dụng lệnh sau:

```bash
xz file.txt
```
Lệnh này sẽ tạo ra tệp tin nén có tên `file.txt.xz` và xóa tệp tin gốc `file.txt`.

### Ví dụ 2: Giải nén một tệp tin
Để giải nén tệp tin `file.txt.xz`, bạn có thể sử dụng lệnh sau:

```bash
xz -d file.txt.xz
```
Lệnh này sẽ khôi phục tệp tin gốc `file.txt` từ tệp tin nén.

## Mẹo
- Khi làm việc với nhiều tệp tin, bạn có thể nén chúng cùng một lúc bằng cách chỉ định nhiều tệp tin trong lệnh `xz`:

```bash
xz file1.txt file2.txt file3.txt
```

- Nếu bạn muốn giữ lại tệp tin gốc sau khi nén, hãy sử dụng tùy chọn `-k`:

```bash
xz -k file.txt
```

- Để nén một thư mục, bạn có thể kết hợp `tar` và `xz`:

```bash
tar -cvf - thư mục/ | xz > archive.tar.xz
```

Sử dụng lệnh `xz` một cách hiệu quả sẽ giúp bạn quản lý tệp tin dễ dàng hơn và tiết kiệm không gian lưu trữ.