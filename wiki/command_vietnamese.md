# [리눅스] Bash command 사용법

## Tổng quan
Lệnh `command` trong Bash được sử dụng để thực thi một lệnh mà không bị ảnh hưởng bởi các alias hoặc hàm có cùng tên. Điều này hữu ích khi bạn muốn đảm bảo rằng bạn đang chạy một lệnh gốc, không phải là một phiên bản đã được định nghĩa lại.

## Cách sử dụng
Cú pháp cơ bản của lệnh `command` như sau:

```bash
command [OPTION]... COMMAND [ARGUMENTS]...
```

### Tùy chọn phổ biến
- `-v` hoặc `--verbose`: Hiển thị thông tin chi tiết về lệnh được thực thi.
- `-p`: Tìm kiếm lệnh trong PATH mặc định, bỏ qua các alias và hàm.

## Ví dụ
### Ví dụ 1: Thực thi lệnh `ls` mà không bị ảnh hưởng bởi alias
Giả sử bạn đã định nghĩa một alias cho lệnh `ls`, bạn có thể sử dụng `command` để chạy lệnh gốc:

```bash
alias ls='ls --color=auto'
command ls
```

### Ví dụ 2: Sử dụng tùy chọn `-v`
Bạn có thể sử dụng tùy chọn `-v` để xem thông tin chi tiết về lệnh:

```bash
command -v ls
```

## Mẹo
- Sử dụng lệnh `command` khi bạn không chắc chắn về việc một lệnh có thể đã được định nghĩa lại hay không. Điều này giúp bạn tránh được những lỗi không mong muốn khi thực thi các lệnh trong Bash.
- Kết hợp với các lệnh khác để kiểm tra xem một lệnh có phải là một alias hay không bằng cách sử dụng `type`:

```bash
type ls
command ls
```

Việc sử dụng lệnh `command` sẽ giúp bạn có sự kiểm soát tốt hơn trong môi trường dòng lệnh của Bash.