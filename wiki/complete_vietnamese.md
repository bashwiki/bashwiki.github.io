# [리눅스] Bash complete 사용법

## Tổng quan
Lệnh `complete` trong Bash được sử dụng để định nghĩa cách hoàn thành tự động cho các lệnh tùy chỉnh. Mục đích chính của lệnh này là giúp người dùng dễ dàng hoàn thành các tham số hoặc tùy chọn cho các lệnh mà họ đã tạo ra, từ đó nâng cao hiệu suất làm việc và giảm thiểu lỗi khi nhập lệnh.

## Cú pháp
Cú pháp cơ bản của lệnh `complete` như sau:

```bash
complete [options] [command]
```

### Các tùy chọn phổ biến:
- `-o`: Chỉ định các tùy chọn hoàn thành. Ví dụ: `-o nospace` để không thêm khoảng trắng sau khi hoàn thành.
- `-F`: Chỉ định một hàm hoàn thành tùy chỉnh sẽ được gọi khi hoàn thành lệnh.
- `-A`: Xác định loại đối tượng mà hoàn thành sẽ trả về, chẳng hạn như `file`, `command`, `user`, v.v.

## Ví dụ
### Ví dụ 1: Hoàn thành lệnh tùy chỉnh
Giả sử bạn có một lệnh tùy chỉnh có tên là `mycmd`, bạn muốn hoàn thành tự động cho nó với các tham số cụ thể:

```bash
_mycmd_completions() {
    local options="start stop restart"
    COMPREPLY=($(compgen -W "$options" -- "${COMP_WORDS[1]}"))
}

complete -F _mycmd_completions mycmd
```

Trong ví dụ này, khi bạn gõ `mycmd ` và nhấn Tab, Bash sẽ gợi ý các tham số `start`, `stop`, và `restart`.

### Ví dụ 2: Hoàn thành tên tệp
Bạn cũng có thể sử dụng lệnh `complete` để hoàn thành tên tệp cho một lệnh tùy chỉnh:

```bash
complete -o nospace -A file mycmd
```

Lệnh này sẽ cho phép hoàn thành tên tệp khi bạn gõ `mycmd ` và nhấn Tab, mà không thêm khoảng trắng sau tên tệp.

## Mẹo
- Hãy chắc chắn rằng các hàm hoàn thành của bạn được định nghĩa trước khi bạn gọi lệnh `complete`.
- Sử dụng `compopt` để thay đổi các tùy chọn hoàn thành trong một hàm hoàn thành.
- Kiểm tra các hoàn thành hiện có bằng cách sử dụng lệnh `complete -p` để xem tất cả các lệnh đã được cấu hình hoàn thành.

Lệnh `complete` là một công cụ mạnh mẽ giúp cải thiện trải nghiệm dòng lệnh của bạn, đặc biệt là khi làm việc với các lệnh tùy chỉnh. Hãy thử nghiệm và tùy chỉnh nó theo nhu cầu của bạn!