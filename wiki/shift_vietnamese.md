# [Linux] Bash shift Cách sử dụng: Thay đổi vị trí các tham số trong dòng lệnh

## Tổng quan
Lệnh `shift` trong Bash được sử dụng để thay đổi vị trí của các tham số trong dòng lệnh. Khi lệnh này được thực thi, nó sẽ loại bỏ tham số đầu tiên và dịch chuyển tất cả các tham số còn lại sang trái, giúp bạn dễ dàng xử lý các tham số còn lại trong một vòng lặp.

## Cách sử dụng
Cú pháp cơ bản của lệnh `shift` như sau:

```bash
shift [n]
```

Trong đó `n` là số lượng tham số mà bạn muốn dịch chuyển. Nếu không chỉ định `n`, mặc định `shift` sẽ dịch chuyển 1 tham số.

## Các tùy chọn phổ biến
- `n`: Số lượng tham số muốn dịch chuyển. Nếu không có tùy chọn này, lệnh sẽ dịch chuyển 1 tham số.

## Ví dụ phổ biến
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `shift`:

### Ví dụ 1: Dịch chuyển 1 tham số
```bash
#!/bin/bash
echo "Tham số đầu tiên: $1"
shift
echo "Tham số đầu tiên sau khi shift: $1"
```
Khi chạy script này với các tham số, tham số đầu tiên sẽ bị loại bỏ sau khi lệnh `shift` được thực thi.

### Ví dụ 2: Dịch chuyển nhiều tham số
```bash
#!/bin/bash
echo "Tham số đầu tiên: $1"
echo "Tham số thứ hai: $2"
shift 2
echo "Tham số đầu tiên sau khi shift 2: $1"
```
Trong ví dụ này, cả hai tham số đầu tiên và thứ hai sẽ bị loại bỏ.

### Ví dụ 3: Sử dụng trong vòng lặp
```bash
#!/bin/bash
while [ "$#" -gt 0 ]; do
    echo "Tham số: $1"
    shift
done
```
Script này sẽ in ra tất cả các tham số cho đến khi không còn tham số nào.

## Mẹo
- Sử dụng lệnh `shift` trong các vòng lặp để dễ dàng xử lý danh sách tham số.
- Kiểm tra số lượng tham số còn lại bằng cách sử dụng `$#` trước và sau khi gọi `shift`.
- Hãy cẩn thận khi sử dụng `shift` trong các script phức tạp, vì nó có thể làm mất các tham số quan trọng nếu không được quản lý đúng cách.