# [리눅스] Bash declare 사용법

## Tổng quan
Lệnh `declare` trong Bash được sử dụng để khai báo biến và xác định thuộc tính của chúng. Nó cho phép người dùng chỉ định kiểu dữ liệu cho biến, như là biến số nguyên, mảng, hoặc biến chỉ đọc. Lệnh này rất hữu ích trong việc quản lý và tổ chức mã nguồn, giúp tăng tính rõ ràng và bảo trì cho các script Bash.

## Cú pháp
Cú pháp cơ bản của lệnh `declare` như sau:

```bash
declare [options] [variable_name]
```

### Các tùy chọn phổ biến:
- `-a`: Khai báo một mảng.
- `-i`: Khai báo một biến số nguyên. Tất cả các phép toán trên biến này sẽ được thực hiện như số nguyên.
- `-r`: Khai báo một biến chỉ đọc, không thể thay đổi giá trị sau khi đã được gán.
- `-x`: Đánh dấu biến để xuất ra môi trường, cho phép biến có thể được truy cập từ các subprocess.

## Ví dụ
### Ví dụ 1: Khai báo biến số nguyên
```bash
declare -i num=5
num=num+10
echo $num  # Kết quả: 15
```
Trong ví dụ này, biến `num` được khai báo là một số nguyên. Khi thực hiện phép cộng, giá trị của `num` được tính toán như một số nguyên.

### Ví dụ 2: Khai báo mảng
```bash
declare -a fruits
fruits=("apple" "banana" "cherry")
echo ${fruits[1]}  # Kết quả: banana
```
Ở đây, biến `fruits` được khai báo là một mảng và chứa ba phần tử. Chúng ta có thể truy cập phần tử thứ hai của mảng bằng cách sử dụng chỉ số.

## Mẹo
- Sử dụng `declare -p` để in ra thông tin về biến và thuộc tính của nó. Ví dụ:
  ```bash
  declare -p fruits
  ```
- Khi làm việc với các script lớn, hãy sử dụng `declare -r` cho các biến không thay đổi để tránh việc vô tình thay đổi giá trị của chúng.
- Sử dụng `declare -x` cho các biến mà bạn muốn xuất ra môi trường, điều này rất hữu ích khi bạn cần các subprocess truy cập vào biến của bạn.

Lệnh `declare` là một công cụ mạnh mẽ trong Bash, giúp bạn quản lý và tổ chức các biến một cách hiệu quả.