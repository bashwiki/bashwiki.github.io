# [리눅스] Bash printf 사용법

## Tổng quan
Lệnh `printf` trong Bash là một công cụ mạnh mẽ dùng để định dạng và in ra dữ liệu. Nó tương tự như hàm `printf` trong ngôn ngữ lập trình C, cho phép người dùng kiểm soát cách mà dữ liệu được hiển thị. `printf` có thể được sử dụng để in ra chuỗi, số, và các kiểu dữ liệu khác với định dạng tùy chỉnh.

## Cách sử dụng
Cú pháp cơ bản của lệnh `printf` như sau:

```bash
printf "định dạng" [giá trị...]
```

Trong đó:
- `"định dạng"`: Là chuỗi định dạng, nơi bạn có thể chỉ định cách mà các giá trị sẽ được in ra. Các ký tự định dạng phổ biến bao gồm:
  - `%s`: Chuỗi
  - `%d`: Số nguyên
  - `%f`: Số thực
  - `%x`: Số thập lục phân

- `[giá trị...]`: Là các giá trị mà bạn muốn in ra, tương ứng với các ký tự định dạng.

## Ví dụ
Dưới đây là một số ví dụ thực tế về cách sử dụng lệnh `printf`:

### Ví dụ 1: In ra chuỗi
```bash
printf "Xin chào, %s!\n" "Thế giới"
```
Kết quả sẽ là:
```
Xin chào, Thế giới!
```

### Ví dụ 2: In ra số với định dạng
```bash
printf "Số nguyên: %d, Số thực: %.2f\n" 10 3.14159
```
Kết quả sẽ là:
```
Số nguyên: 10, Số thực: 3.14
```

## Mẹo
- Sử dụng `\n` trong chuỗi định dạng để thêm dòng mới.
- Bạn có thể sử dụng các tham số để điều chỉnh độ rộng và độ chính xác của các giá trị được in ra. Ví dụ: `%5d` sẽ in số nguyên với độ rộng tối thiểu là 5 ký tự.
- `printf` không tự động thêm khoảng trắng giữa các giá trị, vì vậy bạn cần phải thêm chúng vào chuỗi định dạng nếu cần.

Sử dụng `printf` giúp bạn có thể kiểm soát tốt hơn cách mà dữ liệu được hiển thị trong Bash, từ đó nâng cao khả năng tương tác và hiển thị thông tin trong các script của bạn.