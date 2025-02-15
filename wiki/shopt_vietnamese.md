# [리눅스] Bash shopt 사용법

## Tổng quan
`shopt` là một lệnh trong Bash cho phép người dùng quản lý các tùy chọn shell. Nó giúp người dùng bật hoặc tắt các tính năng mở rộng của shell, từ đó cải thiện khả năng sử dụng và hiệu suất của môi trường dòng lệnh. Các tùy chọn này có thể ảnh hưởng đến cách mà Bash xử lý các lệnh, biến và các tính năng khác.

## Cách sử dụng
Cú pháp cơ bản của lệnh `shopt` như sau:

```bash
shopt [OPTION] [NAME]
```

### Các tùy chọn phổ biến:
- `-s, --set`: Bật một tùy chọn.
- `-u, --unset`: Tắt một tùy chọn.
- `-p, --print`: In ra danh sách các tùy chọn hiện tại và trạng thái của chúng.

## Ví dụ
### Ví dụ 1: Bật tùy chọn `autocd`
Tùy chọn `autocd` cho phép người dùng chuyển đến một thư mục chỉ bằng cách gõ tên thư mục mà không cần sử dụng lệnh `cd`.

```bash
shopt -s autocd
```

Sau khi bật tùy chọn này, bạn có thể chỉ cần gõ tên thư mục để chuyển đến nó:

```bash
Documents
```

### Ví dụ 2: Kiểm tra trạng thái của tùy chọn
Để xem tất cả các tùy chọn hiện tại và trạng thái của chúng, bạn có thể sử dụng lệnh sau:

```bash
shopt
```

Điều này sẽ in ra danh sách tất cả các tùy chọn cùng với trạng thái bật hoặc tắt của chúng.

## Mẹo
- Sử dụng `shopt -p` để in ra các tùy chọn hiện tại mà bạn đã bật. Điều này hữu ích khi bạn muốn ghi lại cấu hình shell của mình.
- Hãy cẩn thận khi bật hoặc tắt các tùy chọn, vì một số tùy chọn có thể thay đổi cách mà Bash hoạt động một cách đáng kể. Hãy thử nghiệm trong một phiên shell tạm thời trước khi áp dụng vào môi trường làm việc chính của bạn.