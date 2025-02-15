# [리눅스] Bash break 사용법

## Tổng quan
Lệnh `break` trong Bash được sử dụng để thoát khỏi một vòng lặp. Khi lệnh này được thực thi, nó sẽ dừng vòng lặp hiện tại và tiếp tục với câu lệnh tiếp theo sau vòng lặp đó. Lệnh `break` rất hữu ích khi bạn cần dừng vòng lặp sớm dựa trên một điều kiện nhất định.

## Cú pháp
Cú pháp cơ bản của lệnh `break` như sau:

```bash
break [n]
```

Trong đó:
- `n` (tùy chọn): Là số nguyên cho biết số vòng lặp cần thoát. Nếu không chỉ định, `break` sẽ thoát khỏi vòng lặp gần nhất.

## Ví dụ
Dưới đây là một vài ví dụ thực tế về cách sử dụng lệnh `break`.

### Ví dụ 1: Thoát khỏi vòng lặp `for`
```bash
for i in {1..10}; do
    if [ $i -eq 5 ]; then
        break
    fi
    echo $i
done
```
**Giải thích**: Trong ví dụ này, vòng lặp `for` sẽ in ra các số từ 1 đến 4. Khi `i` bằng 5, lệnh `break` sẽ được thực thi và vòng lặp sẽ dừng lại.

### Ví dụ 2: Thoát khỏi vòng lặp `while`
```bash
count=1
while true; do
    echo $count
    if [ $count -ge 3 ]; then
        break
    fi
    ((count++))
done
```
**Giải thích**: Ở đây, vòng lặp `while` sẽ in ra các số 1 đến 3. Khi `count` đạt giá trị 3, lệnh `break` sẽ được thực hiện, và vòng lặp sẽ dừng lại.

## Mẹo
- Sử dụng lệnh `break` một cách hợp lý để tránh việc thoát ra khỏi vòng lặp một cách không mong muốn. Đảm bảo rằng điều kiện để thực hiện lệnh `break` là rõ ràng và dễ hiểu.
- Khi làm việc với nhiều vòng lặp lồng nhau, bạn có thể sử dụng tham số `n` để chỉ định vòng lặp nào bạn muốn thoát. Ví dụ, `break 2` sẽ thoát khỏi hai vòng lặp bên ngoài.

Lệnh `break` là một công cụ mạnh mẽ trong Bash, giúp bạn kiểm soát luồng thực thi của các vòng lặp một cách hiệu quả.