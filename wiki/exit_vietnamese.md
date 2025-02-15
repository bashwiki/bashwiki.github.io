# [리눅스] Bash exit 사용법

## Tổng quan
Lệnh `exit` trong Bash được sử dụng để thoát khỏi một shell hoặc một script. Khi lệnh này được thực thi, nó sẽ kết thúc phiên làm việc hiện tại và trả về một mã trạng thái cho shell cha. Mã trạng thái này thường được sử dụng để chỉ ra kết quả của quá trình thực thi, với giá trị 0 thường biểu thị thành công và các giá trị khác biểu thị lỗi.

## Cách sử dụng
Cú pháp cơ bản của lệnh `exit` như sau:

```bash
exit [MÃ_TRẠNG_THÁI]
```

- **MÃ_TRẠNG_THÁI**: Đây là một số nguyên từ 0 đến 255. Nếu không chỉ định, lệnh `exit` sẽ sử dụng mã trạng thái của lệnh cuối cùng được thực thi.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `exit`.

### Ví dụ 1: Thoát khỏi một script với mã trạng thái thành công
```bash
#!/bin/bash
echo "Đang thực hiện một số công việc..."
# Thực hiện công việc ở đây
exit 0
```
Trong ví dụ này, script sẽ in ra thông báo và sau đó thoát với mã trạng thái 0, cho biết rằng mọi thứ đã diễn ra thành công.

### Ví dụ 2: Thoát khỏi một script với mã trạng thái lỗi
```bash
#!/bin/bash
echo "Đã xảy ra lỗi!"
exit 1
```
Trong ví dụ này, script sẽ thông báo rằng đã có lỗi xảy ra và thoát với mã trạng thái 1, cho biết có vấn đề trong quá trình thực thi.

## Mẹo
- **Kiểm tra mã trạng thái**: Sau khi chạy một lệnh, bạn có thể kiểm tra mã trạng thái của lệnh đó bằng cách sử dụng biến đặc biệt `$?`. Ví dụ:
  ```bash
  some_command
  if [ $? -ne 0 ]; then
      echo "Lệnh đã thất bại!"
      exit 1
  fi
  ```
- **Sử dụng exit trong các hàm**: Nếu bạn đang viết các hàm trong script, hãy sử dụng lệnh `return` để trả về mã trạng thái từ hàm và `exit` để thoát khỏi toàn bộ script.
- **Mã trạng thái có ý nghĩa**: Hãy sử dụng các mã trạng thái khác nhau để biểu thị các loại lỗi khác nhau, điều này giúp dễ dàng xác định nguyên nhân khi có vấn đề xảy ra.

Lệnh `exit` là một công cụ quan trọng trong việc quản lý quá trình và trạng thái của script trong Bash, giúp bạn kiểm soát tốt hơn các tình huống xảy ra trong quá trình thực thi.