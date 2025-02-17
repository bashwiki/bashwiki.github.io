# [Linux] Bash continue: Tiếp tục vòng lặp trong Bash

## Overview
Lệnh `continue` trong Bash được sử dụng để bỏ qua phần còn lại của vòng lặp hiện tại và tiếp tục với lần lặp tiếp theo. Điều này rất hữu ích khi bạn muốn bỏ qua một số điều kiện nhất định trong quá trình lặp.

## Usage
Cú pháp cơ bản của lệnh `continue` như sau:

```bash
continue [n]
```

Trong đó `n` là số lần lặp mà bạn muốn bỏ qua. Nếu không chỉ định `n`, lệnh sẽ tiếp tục với lần lặp tiếp theo ngay lập tức.

## Common Options
- `n`: Chỉ định số lần lặp mà bạn muốn bỏ qua. Nếu `n` là 1, vòng lặp sẽ tiếp tục với lần lặp tiếp theo ngay lập tức. Nếu `n` là 2, nó sẽ bỏ qua hai lần lặp, và cứ như vậy.

## Common Examples

### Ví dụ 1: Bỏ qua số chẵn
```bash
for i in {1..10}; do
    if (( i % 2 == 0 )); then
        continue
    fi
    echo $i
done
```
Kết quả: In ra các số lẻ từ 1 đến 10.

### Ví dụ 2: Bỏ qua số 5
```bash
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        continue
    fi
    echo $i
done
```
Kết quả: In ra các số từ 1 đến 10, nhưng bỏ qua số 5.

### Ví dụ 3: Sử dụng trong vòng lặp while
```bash
count=0
while [ $count -lt 10 ]; do
    count=$((count + 1))
    if [ $count -eq 3 ]; then
        continue
    fi
    echo $count
done
```
Kết quả: In ra các số từ 1 đến 10, nhưng bỏ qua số 3.

## Tips
- Sử dụng `continue` khi bạn muốn kiểm soát luồng của vòng lặp một cách linh hoạt.
- Kết hợp với các điều kiện để tối ưu hóa quá trình lặp.
- Hãy cẩn thận khi sử dụng `continue` trong các vòng lặp lồng nhau, vì nó chỉ ảnh hưởng đến vòng lặp gần nhất.