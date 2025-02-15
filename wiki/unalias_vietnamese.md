# [리눅스] Bash unalias 사용법

## Tổng quan
Lệnh `unalias` trong Bash được sử dụng để xóa bỏ các alias đã được định nghĩa trước đó trong phiên làm việc hiện tại. Alias là các tên thay thế cho các lệnh hoặc chuỗi lệnh, giúp người dùng tiết kiệm thời gian và công sức khi gõ lệnh. Tuy nhiên, đôi khi bạn có thể cần xóa một alias để tránh xung đột hoặc để sử dụng lệnh gốc.

## Cách sử dụng
Cú pháp cơ bản của lệnh `unalias` như sau:

```bash
unalias [tùy chọn] [alias_name]
```

### Tùy chọn phổ biến:
- `-a`: Xóa tất cả các alias đã được định nghĩa trong phiên làm việc hiện tại.
- `-p`: Hiển thị danh sách tất cả các alias hiện có mà không xóa chúng.

## Ví dụ
### Ví dụ 1: Xóa một alias cụ thể
Giả sử bạn đã định nghĩa một alias cho lệnh `ls` như sau:

```bash
alias ls='ls --color=auto'
```

Nếu bạn muốn xóa alias này, bạn có thể sử dụng lệnh:

```bash
unalias ls
```

### Ví dụ 2: Xóa tất cả các alias
Nếu bạn muốn xóa tất cả các alias đã được định nghĩa, bạn có thể sử dụng tùy chọn `-a`:

```bash
unalias -a
```

Điều này sẽ xóa tất cả các alias trong phiên làm việc hiện tại.

## Mẹo
- Hãy cẩn thận khi sử dụng lệnh `unalias`, đặc biệt là với tùy chọn `-a`, vì điều này sẽ xóa tất cả alias mà bạn đã tạo và có thể làm gián đoạn quy trình làm việc của bạn.
- Bạn có thể kiểm tra các alias hiện có bằng lệnh `alias` trước khi quyết định xóa chúng.
- Để đảm bảo rằng alias không bị xóa một cách vô tình, hãy xem xét việc lưu trữ các alias quan trọng trong tệp cấu hình như `.bashrc` hoặc `.bash_profile`.