# [리눅스] Bash fgrep 사용법

## Tổng quan
`fgrep` là một lệnh trong Bash được sử dụng để tìm kiếm các chuỗi văn bản trong các tệp hoặc đầu ra của lệnh khác. Nó là một phiên bản của lệnh `grep`, nhưng `fgrep` không sử dụng biểu thức chính quy (regular expressions), mà chỉ tìm kiếm các chuỗi chính xác. Điều này làm cho `fgrep` trở thành một công cụ hữu ích khi bạn cần tìm kiếm các chuỗi cụ thể mà không cần phải lo lắng về các ký tự đặc biệt.

## Cú pháp
Cú pháp cơ bản của lệnh `fgrep` như sau:

```bash
fgrep [tùy chọn] chuỗi tìm kiếm [tệp...]
```

### Các tùy chọn phổ biến
- `-i`: Bỏ qua sự phân biệt chữ hoa chữ thường trong quá trình tìm kiếm.
- `-v`: In ra các dòng không chứa chuỗi tìm kiếm.
- `-c`: Đếm số dòng chứa chuỗi tìm kiếm và in ra số lượng.
- `-n`: In ra số dòng trước mỗi dòng chứa chuỗi tìm kiếm.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `fgrep`:

### Ví dụ 1: Tìm kiếm chuỗi trong tệp
Giả sử bạn có một tệp có tên `data.txt` và bạn muốn tìm kiếm chuỗi "error":

```bash
fgrep "error" data.txt
```

Lệnh trên sẽ in ra tất cả các dòng trong `data.txt` chứa chuỗi "error".

### Ví dụ 2: Tìm kiếm không phân biệt chữ hoa chữ thường
Nếu bạn muốn tìm kiếm chuỗi "Warning" mà không phân biệt chữ hoa chữ thường, bạn có thể sử dụng tùy chọn `-i`:

```bash
fgrep -i "warning" data.txt
```

Lệnh này sẽ tìm kiếm cả "Warning", "WARNING", "warning", v.v.

## Mẹo
- Khi sử dụng `fgrep`, hãy nhớ rằng nó chỉ tìm kiếm các chuỗi chính xác. Nếu bạn cần tìm kiếm với biểu thức chính quy, hãy sử dụng `grep` thay vì `fgrep`.
- Để tăng tốc độ tìm kiếm, bạn có thể sử dụng `fgrep` với các tệp lớn, vì nó không cần phải phân tích cú pháp biểu thức chính quy.
- Nếu bạn cần tìm kiếm nhiều chuỗi cùng một lúc, bạn có thể sử dụng tùy chọn `-e` để chỉ định nhiều chuỗi:

```bash
fgrep -e "chuỗi1" -e "chuỗi2" data.txt
```

Hy vọng bài viết này giúp bạn hiểu rõ hơn về cách sử dụng lệnh `fgrep` trong Bash!