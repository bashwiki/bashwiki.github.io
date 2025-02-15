# [리눅스] Bash readonly 사용법

## Tổng quan
Lệnh `readonly` trong Bash được sử dụng để đánh dấu một biến là không thể thay đổi. Khi một biến được đánh dấu là `readonly`, giá trị của nó sẽ không thể bị thay đổi trong suốt phiên làm việc hiện tại. Điều này hữu ích trong việc bảo vệ các biến quan trọng khỏi việc bị thay đổi ngẫu nhiên, giúp tránh các lỗi không mong muốn trong kịch bản hoặc chương trình.

## Cú pháp
Cú pháp cơ bản của lệnh `readonly` như sau:

```bash
readonly [tùy chọn] [tên_biến[=giá_trị]]
```

### Tùy chọn phổ biến
- `-p`: Hiển thị danh sách tất cả các biến hiện tại đang được đánh dấu là `readonly`.

## Ví dụ
Dưới đây là một số ví dụ minh họa cách sử dụng lệnh `readonly`.

### Ví dụ 1: Đánh dấu một biến là readonly
```bash
my_var="Giá trị ban đầu"
readonly my_var
```
Sau khi thực hiện lệnh trên, bạn không thể thay đổi giá trị của `my_var`. Nếu bạn cố gắng thực hiện lệnh sau:
```bash
my_var="Giá trị mới"
```
Bash sẽ thông báo lỗi: `bash: my_var: readonly variable`.

### Ví dụ 2: Hiển thị các biến readonly
```bash
readonly -p
```
Lệnh này sẽ hiển thị tất cả các biến hiện tại đang được đánh dấu là `readonly`, cùng với giá trị của chúng.

## Mẹo
- Sử dụng `readonly` cho các biến cấu hình hoặc các giá trị quan trọng mà bạn không muốn thay đổi trong suốt quá trình thực thi kịch bản.
- Hãy cẩn thận khi đánh dấu biến là `readonly`, vì bạn sẽ không thể thay đổi giá trị của nó sau đó. Nếu bạn cần thay đổi, bạn sẽ phải xóa biến đó và tạo lại nó.
- Bạn có thể sử dụng `declare -r` thay cho `readonly`, vì chúng có chức năng tương tự.

Hy vọng bài viết này giúp bạn hiểu rõ hơn về lệnh `readonly` trong Bash và cách sử dụng nó hiệu quả trong các kịch bản của bạn!