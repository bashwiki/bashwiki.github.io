# [리눅스] Bash shift 사용법

## Tổng quan
Lệnh `shift` trong Bash được sử dụng để dịch chuyển các tham số vị trí sang trái. Điều này có nghĩa là tham số đầu tiên ($1) sẽ bị loại bỏ, và các tham số còn lại sẽ được dịch chuyển lên một vị trí. Lệnh này rất hữu ích khi bạn cần xử lý một danh sách các tham số và muốn loại bỏ tham số đã xử lý.

## Cú pháp
Cú pháp cơ bản của lệnh `shift` như sau:

```bash
shift [n]
```

Trong đó:
- `n` là số lượng tham số bạn muốn dịch chuyển. Nếu không chỉ định `n`, lệnh sẽ mặc định dịch chuyển một tham số.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `shift`.

### Ví dụ 1: Dịch chuyển một tham số
```bash
#!/bin/bash
echo "Tham số ban đầu: $1 $2 $3"
shift
echo "Sau khi shift: $1 $2 $3"
```
Khi chạy script này với các tham số như sau:
```bash
./script.sh thamso1 thamso2 thamso3
```
Kết quả sẽ là:
```
Tham số ban đầu: thamso1 thamso2 thamso3
Sau khi shift: thamso2 thamso3 
```

### Ví dụ 2: Dịch chuyển nhiều tham số
```bash
#!/bin/bash
echo "Tham số ban đầu: $1 $2 $3 $4"
shift 2
echo "Sau khi shift 2: $1 $2 $3 $4"
```
Khi chạy script này với các tham số như sau:
```bash
./script.sh thamso1 thamso2 thamso3 thamso4
```
Kết quả sẽ là:
```
Tham số ban đầu: thamso1 thamso2 thamso3 thamso4
Sau khi shift 2: thamso3 thamso4 
```

## Mẹo
- Sử dụng lệnh `shift` trong vòng lặp để xử lý tất cả các tham số một cách tuần tự. Ví dụ:
  ```bash
  while [ "$#" -gt 0 ]; do
      echo "Xử lý tham số: $1"
      shift
  done
  ```
- Hãy cẩn thận khi sử dụng `shift`, vì nếu bạn dịch chuyển quá nhiều tham số, các tham số sẽ trở thành rỗng và có thể gây ra lỗi trong script của bạn.